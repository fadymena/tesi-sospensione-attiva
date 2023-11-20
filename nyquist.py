import control as ctl
import matplotlib.pyplot as plt
import numpy as np

import transfere_functions as fn

G = fn.get_L_s()
omega = np.logspace(-12, 12, 20000)
plt.figure(figsize=(9, 4))
plt.title("Diagramma di Nyquist della funzione d'anello L(s)")
plt.yticks([])
plt.xticks([])

plt.subplot(121)
ctl.nyquist_plot(G, omega)
plt.yticks([-20, -10, -5, 0, 5, 10, 20])

plt.subplot(122)
ctl.nyquist_plot(G, omega)
plt.ylabel('')
plt.xlim(-1.5, 0.25)
plt.yticks(np.arange(-0.5, 1, 0.5))
plt.ylim(-1, 1)
plt.tight_layout()
plt.show()
