#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Showing the importance of the rate determining step and the steady state approximation.
The mechanism proposed is

    A ->k1 B ->k2 C
    By default    k1 = k2 = 1
    You can vary the ratio k1/k2 with the slider.

Informations
------------
Authors: Timothee Chauvire
Some scripts to create the buttons and sliders taken from https://github.com/araoux/python_agregation (written by P Cladé, A Raoux and F Levrier)

WARNING this program requires the widgets.py file to work
"""

# Importation of libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.integrate as integ
import widgets

# Definition des paramètres :
k1 = 26       # endo          L.mol-1.h-1
km1 = 150     # retro endo    h-1
k2 = 5.8e-2   # exo           L.mol-1.h-1
km2 = 1.6e-2  # retro exo     h-1
C0 = 1        # même concentration initiale pour les deux réactifs


def derive(Y,t,k1,k2,km1,km2):
    return np.array([-(k1+k2)*Y[0]**2+km1*Y[1]+km2*Y[2],k1*Y[0]**2-km1*Y[1],k2*Y[0]**2-km2*Y[2]])


def plot_data(k1,k2,km1,km2):
    params = (k1,k2,km1,km2)
    T=100
    N=100000
    t = np.linspace(0,T,N)
    y0 = [1,0,0]
    Y = integ.odeint(derive,y0,t,args =params)
    lines['A1'].set_data(t,Y[:,0])
    lines['B1'].set_data(t,Y[:,1])
    lines['C1'].set_data(t,Y[:,2])
    ax1.set_xlim(1e-4,max(t))
    ax1.set_ylim(0,max(max(Y[:,0]),max(Y[:,2])))
    fig.canvas.draw_idle()

if __name__ == "__main__":
    parameters = {
    'k1' : widgets.FloatSlider(value=26, description = '$k_1$', min=0.5, max=200),
    'km1' : widgets.FloatSlider(value=150, description = '$k_{-1}$', min=0.5, max=200),
    'k2' : widgets.FloatSlider(value=5.8e-2, description = '$k_2$', min=0, max=10),
    'km2' : widgets.FloatSlider(value=1.6e-2, description = '$k_{-2}$', min=0, max=10),

    }
    fig = plt.figure(figsize=(12,6))
    ax1 = fig.add_axes([0.15, 0.25, 0.75, 0.6])
    ax1.axhline(0, color='k')

    ax1.set_title("Controle Cinétique et controle thermodynamique : Reaction de Diels Alder",fontsize=12,color='k',fontweight='bold',pad=10)
    ax1.set_ylabel("Concentration $(Mol.L^{-1})$",fontsize=10)
    ax1.set_xlabel("Temps (h)",fontsize=10)# labelpad=-4)
    ax1.set_xscale("log")
    ax1.tick_params(axis='both', which='major', labelsize=8)

    lines = {}
    lines['A1'], = ax1.plot([],[],label='[Réactif]',color='C0',ls='-')
    lines['B1'], = ax1.plot([],[],label='[endo]',color='C1',ls='-')
    lines['C1'], = ax1.plot([],[],label='[exo]',color='C2',ls='-')
    ax1.legend(loc = 'upper right',fontsize='small')
    param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.25, 0.05, 0.4, 0.1])
    reset_button = widgets.make_reset_button(param_widgets,box=[0.75, 0.05, 0.1, 0.05])
    plt.show()



