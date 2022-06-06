import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import scipy.misc
import scipy.integrate

# plt.xkcd()

"""
Tracer des diagrammes de Bode pour un passe-haut
"""
R = 1000 #Ohm, faire varier entre 100 et 10000
C = 10e-6 #Farad
omega_c = 1/(R*C)
points = 10000

omega = np.linspace(0.1, 10000, points)
G = 20*np.log10((omega/omega_c)/(np.sqrt(1+omega**2/omega_c**2)))
#Attention ! pour la phase, il faut réfléchir aux bornes
phase = (np.pi)/2 - np.arctan(omega/omega_c)
coupure = np.zeros(points) - 3

fig, axes = plt.subplots(2)
fig.suptitle("Diagramme de Bode d'un filtre passe-haut")
#Pour le gain
axes[0].plot(omega,G)
axes[0].plot(omega,coupure,'--')
axes[0].set_xscale('log')
axes[0].grid()
axes[0].set_ylabel("Gain")
#Pour la phase
axes[1].plot(omega,phase)
axes[1].set_xscale('log')
axes[1].grid()
axes[1].set_xlabel("ω, en échelle log")
axes[1].set_ylabel("Phase")
plt.show()
