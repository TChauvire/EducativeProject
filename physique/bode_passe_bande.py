import numpy as np
import matplotlib.pyplot as plt

"""
Tracer des diagrammes de Bode pour un passe-bande (ordre 2)
"""
R1 = 470 #Ohm, faire varier entre 100 et 10000

L = 45.91e-3 #Henry
C = 1e-7 #Farad
omega_0 = 1/np.sqrt(L*C)
Q1 = (1/R1)*np.sqrt(L/C)

points = 1000000

omega = np.linspace(0.1, 10000000, points)
x = omega/omega_0
G1 = -10*np.log10(1+(Q1*(x-1/x))**2)

#Attention ! pour la phase, il faut réfléchir aux bornes
phase1 = - np.arctan(Q1*(x-1/x))

# On trace le diagramme de Bode :
fig, axes = plt.subplots(2)
fig.suptitle("Diagramme de Bode d'un filtre passe-bande")
#Pour le gain
axes[0].plot(omega,G1,label="Q = {}".format(round(Q1,2)))
axes[0].set_xscale('log')
axes[0].grid()
axes[0].set_ylabel("Gain [dB]")
axes[0].legend()
#Pour la phase
axes[1].plot(omega,phase1)
axes[1].set_xscale('log')
axes[1].grid()
axes[1].set_xlabel("ω [s^-1], en échelle log")
axes[1].set_ylabel("Phase")
plt.show()
