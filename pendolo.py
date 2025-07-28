import numpy as np
import matplotlib.pyplot as plt


L = 1.00
g = 9.81

true_T = 2 * np.pi * np.sqrt(L / g)


N = 20   # numero di misure
errore_std = 0.5    # deviazione standard dell'errore (in secondi)

# Genera misure con rumore casuale
misure = np.random.normal(loc=true_T, scale=errore_std, size=N)

media = np.mean(misure)
dev_std = np.std(misure, ddof=1)

print(f"Periodo teorico: {true_T:.3f} s")
print(f"Media misure: {media:.3f} s")
print(f"Errore: {dev_std:.3f} s")

# istogramma
plt.figure(figsize=(6,5))

bins = int(np.ceil(np.log2(N) + 1))

plt.hist(misure, bins = bins, density = True, label='Misure simulate')
plt.axvline(true_T, color='red', linestyle='--', label=f'Periodo teorico: {true_T:.4}')
plt.axvline(media, color='green', linestyle='-.', label=f'Media: {media:.4} $\pm$ {dev_std:.3} [s]')
plt.xlabel('periodo [s]')
plt.ylabel('conteggi')
plt.title(f'Simulazione misure del periodo del pendolo - {N} simulazioni')
plt.legend()
plt.xlim(-0.5, 5)
plt.tight_layout()
plt.show()
