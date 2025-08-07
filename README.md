# Bubble Sort Meets the Birthday Problem

> **Implementation of the research paper:  
> ["Relating bubble sort to birthday problem"](https://arxiv.org/abs/2404.11170) by Jichu Jiang (2024)**  
> Preprint submitted to Elsevier – Beihang University

---

## Overview

This project implements and explores the key ideas presented in the paper *Relating bubble sort to birthday problem* by Jichu Jiang. The paper proposes a novel probabilistic connection between:

- **Bubble Sort** – a classical sorting algorithm, and  
- **The Birthday Problem** – a fundamental problem in probability theory.

The connection is made via the **Rayleigh distribution**, which emerges asymptotically from both the number of passes in bubble sort and the birthday collision probabilities.

---

## Main Contributions from the Paper

1. **Bounding Bubble Sort with the Birthday Problem**  
   The number of passes in bubble sort is shown to be bounded using birthday collision probabilities.

2. **Rayleigh Distribution Emergence**  
   Both the scaled birthday problem and the scaled bubble sort passes converge in distribution to the Rayleigh distribution.

3. **Asymptotic Analysis**  
   The paper derives:
   - Closed-form approximations for the CDF/PMF of bubble sort passes.
   - Moments, variance, and characteristic functions.
   - Precise error bounds via Stirling and Euler–Maclaurin expansions.

4. **Performance Degradation of Optimized Bubble Sort**  
   Some classical optimizations (like early stopping when no swaps occur) can degrade performance asymptotically.

---

## What This Repository Contains

- Mathematical translations of the paper's key formulas (CDF/PMF/moments).
- Simulations comparing the actual distribution of bubble sort passes to the Rayleigh distribution.
- Plots and error analyses as in Figure 1 and 2 of the paper.
- Symbolic derivations of the asymptotic expansions.

---

## Implementation Goals

- [x] Simulate the number of passes in bubble sort over random permutations  
- [x] Estimate the empirical CDF and compare it to the Rayleigh distribution  
- [x] Reproduce key plots and verify approximations from the paper  
- [ ] Extend the model to analyze bubble sort variants  
- [ ] Apply this framework to analyze related sorting problems

