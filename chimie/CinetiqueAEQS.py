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

def derive(Y,t,k1,k2):
    return np.array([-k1*Y[0],k1*Y[0]-k2*Y[1],k2*Y[1]])


def plot_data(Rapport):
    k1 = 1.0
    k2 = Rapport*k1
    params = (k1,k2)
    T=10
    N=1000
    t = np.linspace(0,T,N)
    y0 = [1,0,0]
    Y = integ.odeint(derive,y0,t,args =params)
    derivA = np.gradient(Y[:,0], t)
    derivB = np.gradient(Y[:,1], t)
    derivC = np.gradient(Y[:,2], t)


    lines['A1'].set_data(t,Y[:,0])
    lines['B1'].set_data(t,Y[:,1])
    lines['C1'].set_data(t,Y[:,2])
    lines['A2'].set_data(t,derivA)
    lines['B2'].set_data(t,derivB)
    lines['C2'].set_data(t,derivC)

    ax1.set_xlim(min(t),max(t))
    ax1.set_ylim(0,max(max(Y[:,0]),max(Y[:,2])))
    ax2.set_xlim(min(t),max(t))
    ax2.set_ylim(min(min(derivA),min(derivB),min(derivC)),max(max(derivA),max(derivB),max(derivC)))
    fig.canvas.draw_idle()

if __name__ == "__main__":
    parameters = {
    'Rapport' : widgets.FloatSlider(value=1, description = 'Rapport $k_2/k_1$', min=0.5, max=10),
    }
    fig,axes=plt.subplots(2,1)
    ax1 = plt.subplot(2,1,1)
    ax2 = plt.subplot(2,1,2)
    ax1.set_title('Concentrations',fontsize=12,color='k',fontweight='bold')
    ax2.set_title('Vitesses',fontsize=12,color='k',fontweight='bold')
    ax1.set_ylabel("$Concentration (Mol.L^{-1})$",fontsize=10)
    ax1.set_xlabel("Temps (s)",fontsize=10, labelpad=-4)
    ax2.set_ylabel("$Vitesse (Mol.L^{-1}.s^{-1})$",fontsize=10)
    ax2.set_xlabel("Temps (s)",fontsize=10, labelpad=-4)
    ax1.tick_params(axis='both', which='major', labelsize=8)
    ax2.tick_params(axis='both', which='major', labelsize=8)


    lines = {}
    lines['A1'], = ax1.plot([],[],label='[A]',color='C0',ls='-')
    lines['B1'], = ax1.plot([],[],label='[B]',color='C1',ls='-')
    lines['C1'], = ax1.plot([],[],label='[C]',color='C2',ls='-')
    lines['A2'], = ax2.plot([],[],label='$\dfrac{d[A]}{dt}$',color='C0',ls='-')
    lines['B2'], = ax2.plot([],[],label='$\dfrac{d[B]}{dt}$',color='C1',ls='-')
    lines['C2'], = ax2.plot([],[],label='$\dfrac{d[C]}{dt}$',color='C2',ls='-')
    ax1.legend(loc = 'upper right',fontsize='small')
    ax2.legend(loc = 'lower right',fontsize='small')
    param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.25, 0.05, 0.4, 0.05])
    reset_button = widgets.make_reset_button(param_widgets,box=[0.75, 0.05, 0.1, 0.05])
    plt.subplots_adjust(left=0.125,bottom=0.2,right=0.9,top=0.9,wspace=0.3,hspace=0.5)
    plt.show()



