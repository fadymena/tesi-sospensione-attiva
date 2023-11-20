import matplotlib.pyplot as plt

punti_x = [-5, -19.85, -20.15, -29.85, -30.15, -39.85, -40.15]
x = [-i for i in range(0, 45, 5)]
punti_y = [0 for i in range(len(punti_x))]
plt.figure(figsize=(9, 4))
plt.scatter(punti_x, punti_y, marker='x')
plt.plot([0, 0], [10, -10], linestyle='--')
plt.plot([-5, -5], [10, -10], linestyle='--')
plt.grid()
plt.title("Posizionamento dei poli")
plt.xlim(-45, 5)
plt.ylim(-3, 3)
plt.xticks(x)
plt.xlabel("Reale")
plt.ylabel("Immaginario")
plt.tight_layout()
plt.show()
