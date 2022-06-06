#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import widgets
import scipy.constants as constants
from matplotlib import rc

title = "Effet Doppler et détection synchrone"

## Initial Parameters

parameters = {
    'v' : widgets.FloatSlider(value=0, description = 'Vitesse ($cm/s$)', min=0, max=20),
    'Echelle_T': widgets.FloatSlider(value=1e-4, description = 'Calibre T', min=1e-5, max=1e-2),
    }
c = 340 #Vitesse des ondes dans le milieu (cm/s)
f=40000 #Fréquence en hertz$


## Functions to plot
#x est le rapport entre la pulsation et la pulsation de coupure
def Signal_emis(t):
	u = np.sin(2*np.pi*f*t)
	return(u)

def Signal_recu(v,t):
	f1=f*(1+v/c)
	u= np.sin(2*np.pi*f1*t)
	return(u)

def Signaux_multiplies(v,t):
	return(Signal_emis(t)*Signal_recu(v,t) )


def Signal_filtre(v,t):
	return(np.cos(2*3.1416*t*f*(v/c)))


## This function is called when the sliders are changed
def plot_data(v,Echelle_T):
    t1= np.linspace(0,Echelle_T,1000)
    lines['Signal émis'].set_data(t1,Signal_emis(t1))
    lines['Signal reçus'].set_data(t1,Signal_recu(v,t1))
    lines['Signaux multipliés'].set_data(t1,Signaux_multiplies(v,t1))
    lines['Signal filtré'].set_data(t1,Signal_filtre(v,t1))
    ax1.set_xlim(0,max(t1))
    ax2.set_xlim(0,max(t1))
    ax3.set_xlim(0,max(t1))
    ax1.set_ylim(-1.05, 1.05)
    ax2.set_ylim(-1.05, 1.05)
    ax3.set_ylim(-1.05, 1.05)
    fig.canvas.draw_idle()

fig,axes=plt.subplots(3,1)
ax1 = plt.subplot(3,1,1)
ax2 = plt.subplot(3,1,2)
ax3 = plt.subplot(3,1,3)

##plot of the text
lines = {}
lines['Signal émis'], = ax1.plot([], [], lw=2, color='red')
lines['Signal reçus'], = ax1.plot([], [], lw=2, color='blue')
lines['Signaux multipliés'], = ax2.plot([], [], lw=2, color='red')
lines['Signal filtré'], = ax3.plot([], [], lw=2, color='red')
ax1.set_xlabel('t(s)')
ax2.set_xlabel('t(s)')
ax3.set_xlabel('t(s)')
ax1.set_ylabel("Signaux de \n l'émetteur et \n du récepteur")
ax2.set_ylabel('Amplitude du \n signal multiplié')
ax3.set_ylabel('Amplitude du \n signal filtré')
param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.35, 0.9, 0.4, 0.05])

if __name__=='__main__':
	plt.subplots_adjust(left=0.15,bottom=0.1,
	right=0.9,top=0.85,wspace=0.3,hspace=0.5)
	plt.show()
