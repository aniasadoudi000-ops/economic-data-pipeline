import requests
import os
from dotenv import load_dotenv
from database import init_db, save_data
from visualize import plot_indicator

load_dotenv()

COUNTRIES = ["FR", "US", "DE"]
INDICATORS = {
    "NY.GDP.MKTP.CD": ("PIB", "PIB en USD"),
    "FP.CPI.TOTL.ZG": ("Inflation", "Inflation en %"),
    "SL.UEM.TOTL.ZS": ("Chomage", "Taux de chômage en %")
}

def fetch_data(country, indicator):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=20"
    response = requests.get(url)
    data = response.json()
    
    if len(data) < 2:
        print(f"Pas de données pour {country} - {indicator}")
        return
    
    for entry in data[1]:
        if entry["value"] is not None:
            save_data(country, indicator, entry["date"], entry["value"])
            
    print(f"Données sauvegardées : {country} - {indicator}")

if __name__ == "__main__":
    init_db()
    
    for country in COUNTRIES:
        for indicator, (name, ylabel) in INDICATORS.items():
            fetch_data(country, indicator)
            plot_indicator(country, indicator, name, ylabel)
    
    print("Pipeline terminé. Graphiques générés.")