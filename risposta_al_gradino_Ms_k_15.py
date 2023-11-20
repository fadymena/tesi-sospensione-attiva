import control as ctl
import matplotlib.pyplot as plt

import transfere_functions as fn

M_s = fn.get_M_s()
t, yout = ctl.step_response(M_s)
plt.figure(figsize=(9, 4))
plt.plot(t, yout)
plt.title("Risposta al gradino di M(s), k = 15")
plt.ylabel("Ampiezza (metri)")
plt.xlabel("Tempo (secondi)")
plt.ylim(-0.04, 0.03)
plt.xlim(-1, 10)
plt.grid()
plt.show()
