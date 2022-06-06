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
title = "Polarisation du champ électrique"

#description = """RÃ©solution de l'Ã©quation diffÃ©rentielle rÃ©gissant $x$ en fonction des paramÃ¨tres du systÃ¨me"""

#===========================================================
# --- Initial parameters  ---------------------
#===========================================================

parameters = {
    'Rapport' : widgets.FloatSlider(value=1, description = 'Rapport $E_{0x}/E_{0y}$', min=0.5, max=1),
    'Phi' : widgets.FloatSlider(value=np.pi/2, description = 'Déphasage entre $E_x$ et $E_y$', min=0,max=2*np.pi),
    }
w = 0.06


#===========================================================
# --- Functions to plot-------------------------------------
#===========================================================


def EX(w):
	EX=[]
	z=0
	temps = np.linspace(500,0,100)
	for t in temps :
		z=1*np.cos(w*t)
		EX.append(z)
	return EX

def EY(Rapport,w,Phi):
	z=0
	EY=[]
	temps = np.linspace(500,0,100)
	for t in temps :
		z=Rapport*np.cos(w*t+Phi)
		EY.append(z)
	return EY

#===========================================================
# --- Plot of the updated curves ---------------------------
#===========================================================

def plot_data(Rapport, Phi):
    lines['Test'].set_data(EX(w),EY(Rapport,w,Phi))
    fig.canvas.draw_idle()

#===========================================================
# --- Initialization of the plot ---------------------------
#===========================================================

fig = plt.figure(figsize=(6,6.5))
fig.suptitle(title)
#plot of the text
#fig.text(0.01, .9, widgets.justify(description), multialignment='left', verticalalignment='top')

ax = fig.add_axes([0.15, 0.3, 0.75, 0.6])
ax.axhline(0, color='k')

lines = {}
lines['Test'],= ax.plot([], [], lw=2, color='red')



ax.set_xlim(-1,1)
ax.set_ylim(-1,1)

ax.set_xlabel("$E_y$")
ax.set_ylabel("$E_x$")

param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.35, 0.07, 0.4, 0.05])
#choose_widget = widgets.make_choose_plot(lines, box=[0.015, 0.25, 0.2, 0.15])
reset_button = widgets.make_reset_button(param_widgets)

if __name__=='__main__':
   plt.show()

