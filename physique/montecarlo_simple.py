#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats as stats

#Nombre de tirages simulés
N=1000
#Definition des incertitudes types de chaque variable
uCb0 = 0.0001 #
uVb0 = 0.001 #
uVa0 = 0.001 #
#Variables d'entrée
#Il faut préciser la forme des variables d'entrée : np.random.uniform -> fonction de répartition rectangulaire
# np.random.triangular -> fonction de repartition triangulaire
Cb0 = 0.01 ; # en mol.L-1
Vb0 = 0.1 ; # en L
Va0 = 0.1 ; # en L
Cb = np.random.uniform (Cb0-uCb0,Cb0+uCb0,N)
Vb = np.random.uniform (Vb0-uVb0,Vb0+uVb0,N)
Va = np.random.triangular(Va0-uVa0,Va0,Va0+uVa0,N)
#Vb = np.random.normal(0.1, 0.01,N)

#print(Va)
Ca=Cb*Vb/Va
#écart-type réduit
uCa = np.std(Ca,ddof=1)
CaMoy= np.average(Ca)


Ccla=0.01
uCla=Ccla*np.sqrt((uCb0/(Cb0*np.sqrt(3)))**2+(uVb0/(np.sqrt(3)*Vb0))**2+(uVa0/(np.sqrt(6)*Va0))**2)

#abscisse
x = np.linspace(np.min(Ca),np.max(Ca),100)
Gauss = stats.norm.pdf(x, CaMoy, uCa)
GaussCla = stats.norm.pdf(x, Ccla, uCla)

plt.hist(Ca, bins='auto',density = True, label = "Monte-Carlo")
plt.plot(x, Gauss, 'k-', label = "Gaussienne (Montecarlo)")

plt.plot(x, GaussCla, 'k-',color='C1', label = "Gaussienne (Calcul Littéral)")
plt.title('Simulation de {} titrages \n Ca = {:.3e} mol/L \n u(Ca) (Montecarlo) = {:.1e} \n u(Ca) (Propagation) =  {:.1e}'.format(N,CaMoy,uCa,uCla),fontsize=12,color='k',fontweight='bold')
plt.xlabel('Ca en mol.$L^{-1}$')
current_values = plt.gca().get_xticks()
plt.gca().set_xticks(current_values)
plt.gca().set_xticklabels(['{:.3}'.format(x) for x in current_values])
plt.ylabel('Densité de probabilité (u.a.)')
plt.legend(loc = 'best',fontsize='small')
plt.tight_layout()
plt.show()
