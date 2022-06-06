# -*- coding: utf-8 -*-

"""
Courbe intÃ©ractive : exemplde de l'influence des diffÃ©rents paramÃ¨tres d'un circuit RLC sÃ©rie sur la bande passante.

On trace u = f(omega) en donnant une valeur initiale de R, C et L et on peut suivre l'Ã©volution de la courbe en "bougeant" Ã  l'aide d'un curseur les valeurs de R, C et L dans des domaines finis.

A changer : Le nom et le nombre de variables ; leur domaine de variation et leur valeurs initiales ; la formule de la courbe Ã  tracer
"""

## Importation des bibliotheques

import matplotlib.pyplot as plt
import numpy as np
import widgets
import scipy.constants as constants
from matplotlib import rc
## Definition des parametres fixes initiaux

eo = 5


##Paramètres
parameters = {'R' : widgets.IntSlider(value=100, description='$R (ohm)$', min=10, max=10000),
              'L' : widgets.IntSlider(value=100 , description='$L (mH)$', min=1, max=1000),
              'C' : widgets.FloatSlider(value=0.01, description='$C (microF)$', min=0.001, max=1)}


## Creation de la fenetre

fig=plt.figure(figsize=(12,6))
ax = fig.add_axes([0.2, 0.2, 0.35, 0.7])
plt.xlabel("pulsation $(rad.s^{-1})$")                     # titre de l'axe des abscisses
plt.ylabel("$Gain=\dfrac{U}{E_0}$")                                  # titre de l'axe des ordonnÃ©es
plt.title("Courbe de la résonance en tension d'un RLC série.")
plt.legend()
plt.grid(True)                                          # quadrille le graphique


omega = np.arange(0, 1e5, 1e1)                    # omega allant de 1000 Ã  100000 par pas de 10


##Défintion des fonctions

def Fonction_transfert(omega,R,L,C):
    w0 = 1/np.sqrt(L*1E-3 *C*1E-6)
    Q = 1/R*np.sqrt(L*1E-3 /(C*1E-6))
    H = eo/(np.sqrt((1-(omega/w0)**2)**2+(((omega/w0)/Q))**2))
    return Q, H



def plot_data(R,L,C):
    H = Fonction_transfert(omega, R, L, C)[1]
    lines.set_data(omega,H)
    texts.set_text('Facteur de qualité : Q = {:.1e}'.format(Fonction_transfert(omega, R, L, C)[0]))
    ax.set_xlim(min(omega),max(omega))
    ax.set_ylim(min(H),max(H))
    fig.canvas.draw_idle()


lines = {}
lines, = ax.plot([], [],color='red',lw=2)
texts=  fig.text(0.75, 0.8, '$x=$', fontsize=10,ha='center')
ax.legend()


##Définition d'un slider

param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.65, 0.45, 0.20, 0.15])

## Définition d'un bouton reset

reset_button = widgets.make_reset_button(param_widgets,box=[0.65, 0.25, 0.10, 0.05])

## Affichage du tout


if __name__=='__main__':
#    fig.tight_layout()
    plt.show()


