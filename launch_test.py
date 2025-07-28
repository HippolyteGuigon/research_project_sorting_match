import math
import multiprocessing as mp
import matplotlib.pyplot as plt
import numpy as np
from create_random_list import create_random_list
from bubble_sort import bubble_sort
from kolmogorov_smirnoff_test import get_params, get_ks_statistic
from scipy.stats import rayleigh

n_samples = 10000
n_elements = 1000

def generate_pass_count(_):
    random_list = create_random_list(n_elements, 0, 1000)
    _, nb_passes = bubble_sort(random_list)
    return nb_passes

def main():
    with mp.Pool(mp.cpu_count()) as pool:
        number_passes = pool.map(generate_pass_count, range(n_samples))

    x_n = [(n_elements - p) / math.sqrt(n_elements) for p in number_passes]
    plot_comparison(x_n)
    params = get_params(x_n)
    stat, p_value = get_ks_statistic(x_n, params)

    print(f"KS stat = {stat:.4f}, p-value = {p_value:.4f}")

def plot_comparison(x_n, filename="rayleigh_vs_data.png"):
    # Histogramme des données
    plt.figure(figsize=(10, 5))

    # Subplot gauche : histogramme + densité Rayleigh
    plt.subplot(1, 2, 1)
    plt.hist(x_n, bins=40, density=True, alpha=0.6, label="X_n (simulé)")

    x_vals = np.linspace(0, max(x_n), 500)
    pdf_vals = rayleigh.pdf(x_vals, *rayleigh.fit(x_n))  # fitted Rayleigh
    plt.plot(x_vals, pdf_vals, lw=2, label="Rayleigh ajustée")

    plt.title("Données vs Rayleigh ajustée")
    plt.xlabel("X_n")
    plt.ylabel("Densité")
    plt.legend()

    # Subplot droite : comparer avec vraie Rayleigh standard
    plt.subplot(1, 2, 2)
    plt.hist(x_n, bins=40, density=True, alpha=0.6, label="X_n (simulé)")
    std_rayleigh_vals = rayleigh.pdf(x_vals)  # standard Rayleigh: loc=0, scale=1
    plt.plot(x_vals, std_rayleigh_vals, lw=2, label="Rayleigh standard", linestyle="--")

    plt.title("Données vs Rayleigh standard")
    plt.xlabel("X_n")
    plt.ylabel("Densité")
    plt.legend()

    plt.tight_layout()
    plt.savefig(filename)
    print(f"📊 Graphique sauvegardé dans: {filename}")

if __name__ == "__main__":
    main()
