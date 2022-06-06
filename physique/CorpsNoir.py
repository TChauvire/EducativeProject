#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import widgets
import scipy.constants as constants
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)
title = "Densité d'énergie du corps noir en fonction de la température"

#description = """RÃ©solution de l'Ã©quation diffÃ©rentielle rÃ©gissant $x$ en fonction des paramÃ¨tres du systÃ¨me"""

#===========================================================
# --- Initial parameters  ---------------------
#===========================================================

parameters = {
    'T' : widgets.FloatSlider(value=4000, description = 'Température en Kelvin', min=2000, max=5778),
     }
h=6.63E-34
c=3E8
k=1.38E-23
longueur=np.linspace(20000,100,1000)


#===========================================================
# --- Functions to plot-------------------------------------
#===========================================================

#def Frequence(lamda,T):
#	lamda = lamda/10**6
#	v = c/lamda
#	print(8*np.pi*h*v**3/(c**3*(np.exp(h*v/(k*T))-1)))
#	return 8*np.pi*h*v**3/(40*c**3*(np.exp(h*v/(k*T))-1))


def Frequence2(longueur,T):
	longueur = longueur/10**9  #On passe en nanometre
	v = c/longueur #La fréquence c'est c/lambda
	u = (2*h*c**2/longueur**5)*(1/(np.exp(h*c/(longueur*k*T))-1))
	return u

#===========================================================
# --- Plot of the updated curves ---------------------------
#===========================================================

def plot_data(T):
    freq = Frequence2(longueur,T)
    lines['Test'].set_data(longueur,freq)
    fig.canvas.draw_idle()
    ax.set_ylim(0, max(freq))
    indicemaximum = [i for i, j in enumerate(freq) if j == max(freq)]
    texts.set_text('$\lambda_{max}$ = '+'{} nm'.format(int(longueur[indicemaximum])))
#===========================================================
# --- Initialization of the plot ---------------------------
#===========================================================

fig = plt.figure(figsize=(12,6))
fig.suptitle(title)
#plot of the text
#fig.text(0.01, .9, widgets.justify(description), multialignment='left', verticalalignment='top')

ax = fig.add_axes([0.15, 0.3, 0.75, 0.6])
ax.axhline(0, color='k')

lines = {}
lines['Test'],= ax.plot([], [], lw=2, color='red')





ax.set_xlabel("Longueur d'onde ($\mu m$)")
ax.set_ylabel("Densité spectrale d'énergie (W.m$^{-2}.nm^{-1}$")
ax.set_xlim(0,max(longueur)/3)


texts=  fig.text(0.75, 0.8, '$x=$', fontsize=10,ha='center')


param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.35, 0.07, 0.4, 0.05])
#choose_widget = widgets.make_choose_plot(lines, box=[0.015, 0.25, 0.2, 0.15])
reset_button = widgets.make_reset_button(param_widgets)

if __name__=='__main__':
   plt.show()

