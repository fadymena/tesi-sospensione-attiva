import control as ctl
import matplotlib.pyplot as plt

import transfere_functions as fn

G1 = fn.get_G1()
G2 = fn.get_G2()
R = fn.get_R()
plt.figure(figsize=(18, 8))
plt.title("Risposta al gradino di M(s)", pad=25)
plt.ylabel("Ampiezza (metri)", labelpad=30)
plt.xlabel("Tempo (secondi)", labelpad=20)
plt.yticks([])
plt.xticks([])
for k in range(1, 16):
    L_s = G1 * R * k
    M_s = G2 / (1 + L_s)
    t, yout = ctl.step_response(M_s)
    plt.subplot(3, 5, k)
    plt.plot(t, yout)
    plt.title("k = " + str(k), pad=5)

    plt.ylim(-1, 1)
    plt.xlim(-1, 10)
    plt.grid()
plt.tight_layout()
plt.show()
