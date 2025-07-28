import numpy as np
from scipy.stats import rayleigh, kstest
from statistical_test import get_params, get_ks_statistic
import matplotlib.pyplot as plt
import math
import random

def simulate_birthday_collision(n_days=365):
    seen = set()
    for i in range(1, n_days + 1):
        birthday = random.randint(0, n_days - 1)
        if birthday in seen:
            return i 
        seen.add(birthday)
    return n_days 

def run_experiment(n_samples=100000, n_days=365):
    collisions = [simulate_birthday_collision(n_days) for _ in range(n_samples)]
    T_n = [c / math.sqrt(n_days) for c in collisions]
    return T_n

def plot_rayleigh_comparison(T_n, filename="results/birthday_vs_rayleigh.png"):
    plt.figure(figsize=(10, 5))
    
    # Subplot gauche : Rayleigh fit
    plt.subplot(1, 2, 1)
    plt.hist(T_n, bins=50, density=True, alpha=0.6, label="T_n (Birthday problem)")
    x_vals = np.linspace(0, max(T_n), 500)
    fitted_params = rayleigh.fit(T_n)
    plt.plot(x_vals, rayleigh.pdf(x_vals, *fitted_params), lw=2, label="Rayleigh ajustée")
    plt.title("Distribution T_n vs Rayleigh ajustée")
    plt.xlabel("T_n")
    plt.ylabel("Densité")
    plt.legend()

    # Subplot droite : Rayleigh standard
    plt.subplot(1, 2, 2)
    plt.hist(T_n, bins=50, density=True, alpha=0.6, label="T_n (Birthday problem)")
    plt.plot(x_vals, rayleigh.pdf(x_vals), lw=2, linestyle="--", label="Rayleigh standard")
    plt.title("Distribution T_n vs Rayleigh standard")
    plt.xlabel("T_n")
    plt.ylabel("Densité")
    plt.legend()

    plt.tight_layout()
    plt.savefig(filename)
    print(f"📊 Graphique sauvegardé dans : {filename}")

def test_rayleigh(T_n):
    stat, p_value = kstest(T_n, 'rayleigh', args=rayleigh.fit(T_n))
    print(f"KS stat: {stat:.4f}, p-value: {p_value:.4f}")

if __name__ == "__main__":
    T_n = run_experiment(n_samples=1000000, n_days=365)
    plot_rayleigh_comparison(T_n)
    test_rayleigh(T_n)