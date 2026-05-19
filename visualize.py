import matplotlib.pyplot as plt
from database import get_data

def plot_indicator(country, indicator, title, ylabel):
    rows = get_data(country, indicator)
    
    if not rows:
        print(f"Aucune donnée pour {country} - {indicator}")
        return
    
    years = [row[0] for row in rows]
    values = [row[1] for row in rows]
    
    plt.figure(figsize=(12, 6))
    plt.plot(years, values, marker='o', linewidth=2, color='#2196F3')
    plt.fill_between(years, values, alpha=0.1, color='#2196F3')
    plt.title(f"{title} — {country}", fontsize=14, fontweight='bold')
    plt.xlabel("Année")
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{country}_{indicator}.png")
    plt.close()
    print(f"Graphique sauvegardé : {country}_{indicator}.png")