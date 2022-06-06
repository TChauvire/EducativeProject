# -*- coding: utf-8 -*-

"""
Courbe interactive : Diffusion d'une tache d'encre sur un papier filtre
"""

## Importation des bibliotheques

import matplotlib.pyplot as plt
import numpy as np
import widgets
import scipy.constants as constants
from matplotlib import rc
## Definition des parametres fixes initiaux



##Paramètres
parameters = {'D' : widgets.IntSlider(value=8, description=r'$D (m^2s^{-1})$', min=1, max=20),
              't' : widgets.IntSlider(value=0.01 , description=r'$t (s)$', min=0.01, max=20),
              'A' : widgets.FloatSlider(value=150, description=r'$A (m^{-2}})$', min=50, max=200)}


## Creation de la fenetre

fig=plt.figure(figsize=(12,6))
ax = fig.add_axes([0.1, 0.2, 0.35, 0.7])
ax.set_xlim(-50,50)
ax.set_ylim(0,200)
plt.xlabel(r'$x (m)$')                     # titre de l'axe des abscisses
plt.ylabel(r'Densité de particule $(m^{-3})$')                                  # titre de l'axe des ordonnÃ©es
plt.title("Equation de diffusion et évolution")
plt.grid(True)                                          # quadrille le graphique

x=np.linspace(-50,50,10000)

##Défintion des fonctions

def Diffusion(x,A,t,D):
    return ((A/np.sqrt(D*t)*np.exp(-(x**2)/(4*D*t))))



def plot_data(A,t,D):
    lines.set_data(x,Diffusion(x,A,t,D))
    fig.canvas.draw_idle()


lines = {}
lines, = ax.plot([], [],color='red',lw=2)
ax.legend()

##Définition d'un slider

param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.60, 0.15, 0.30, 0.15])

## Définition d'un bouton reset

reset_button = widgets.make_reset_button(param_widgets,box=[0.32, 0.05, 0.10, 0.05])

## Affichage du tout


if __name__=='__main__':
    plt.show()


