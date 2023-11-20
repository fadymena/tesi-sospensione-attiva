import control as ctl
import matplotlib.pyplot as plt

import transfere_functions as fn

G1 = fn.get_G1()
G2 = fn.get_G2()

t1, yout1 = ctl.step_response(G1)
plt.figure(figsize=(9, 8))

plt.subplot(2, 1, 1)
plt.plot(t1, yout1)
plt.title("Risposta al gradino di G1")
plt.ylabel("Ampiezza (metri)")
plt.xlabel("Tempo (secondi)")
plt.xlim(-1, 55)
plt.grid()

t2, yout2 = ctl.step_response(G2)
plt.subplot(2, 1, 2)
plt.plot(t2, yout2)
plt.title("Risposta al gradino di G2", pad=20)
plt.ylabel("Ampiezza (metri)")
plt.xlabel("Tempo (secondi)")
plt.xlim(-1, 55)
plt.grid()
plt.tight_layout()
plt.show()
