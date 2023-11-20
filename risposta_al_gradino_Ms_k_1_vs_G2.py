import control as ctl
import matplotlib.pyplot as plt

import transfere_functions as fn

G1 = fn.get_G1()
G2 = fn.get_G2()
R = fn.get_R()
L_s = G1 * R
M_s = G2 / (1 + L_s)

t, yout = ctl.step_response(M_s)
fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
ax1.plot(t, yout)
ax1.set_title("Risposta al gradino di M(s), k = 1")
ax1.set(ylabel='Ampiezza (metri)')
ax1.set(ylim=(-1, 1), xlim=(-1, 10))
ax1.grid()
t2, yout2 = ctl.step_response(G2)
ax2.plot(t2, yout2)
ax2.set_title("Risposta al gradino di G2(s)")
ax2.set(ylabel='Ampiezza (metri)', xlabel='Tempo (secondi)')
ax2.set(ylim=(-1, 1), xlim=(-1, 10))
ax2.grid()

plt.tight_layout()
plt.show()
