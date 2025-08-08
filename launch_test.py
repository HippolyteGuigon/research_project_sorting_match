import math
import multiprocessing as mp
import matplotlib.pyplot as plt
import numpy as np
from create_random_list import create_random_list
from bubble_sort import bubble_sort
from statistics.statistical_test import get_ks_statistic
from scipy.stats import rayleigh
from tqdm import tqdm
import pickle
import os

n_samples = 50
n_elements = 25000

def generate_pass_count(_):
    random_list = create_random_list(n_elements)
    _, nb_passes = bubble_sort(random_list)
    return nb_passes

def main():
    with mp.Pool(mp.cpu_count()) as pool:
        number_passes = []
        with tqdm(total=n_samples) as pbar:
            for result in pool.imap_unordered(generate_pass_count, range(n_samples)):
                number_passes.append(result)
                pbar.update()
    if os.path.exists("number_passes.pkl"):
        with open("number_passes.pkl", "rb") as f:
            hist_pass = pickle.load(f)
    else:
        hist_pass = []
    
    hist_pass=hist_pass+number_passes

    x_n = [(n_elements - p) / math.sqrt(n_elements) for p in hist_pass]

    with open("number_passes.pkl", "wb") as f:
        pickle.dump(hist_pass, f)

    stat, p_value = get_ks_statistic(x_n)
    plot_comparison(x_n, p_value=p_value)
    
    print(f"KS stat = {stat:.4f}, p-value = {p_value:.4f}")

def plot_comparison(x_n, filename=None, p_value=None):
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats import rayleigh
    filename = f"result/rayleigh_vs_data_{len(x_n)}.png"
    plt.figure(figsize=(7, 5))

    # Histogramme normalisé
    plt.hist(x_n, bins=40, density=True, alpha=0.6, label="Histogramme de $X_n$")

    # Densité Rayleigh standard (loc=0, scale=1)
    x_vals = np.linspace(0, max(x_n), 500)
    rayleigh_standard_pdf = rayleigh.pdf(x_vals, loc=0, scale=1)
    plt.plot(x_vals, rayleigh_standard_pdf, lw=2, linestyle='--', label="Rayleigh standard")

    plt.title("Comparaison entre $X_n$ et loi de Rayleigh standard")
    plt.xlabel(f"Distribution de $X_n$, n = {len(x_n)}")
    plt.ylabel("Densité")
    plt.legend()
    
    if p_value is not None:
        plt.text(0.6, 0.9, f"p-value = {p_value:.4f}", transform=plt.gca().transAxes)

    plt.tight_layout()
    plt.savefig(filename)
    print(f"📊 Graphique sauvegardé dans : {filename}")

if __name__ == "__main__":
    while True:
        main()
