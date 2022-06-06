'''


Script adapté de :
https://www.f-legrand.fr/pynum/capacites/thermodynamique.html#diagramme-de-distribution-d-un-diacide
Informations
------------
Authors: Timothee Chauvire
Some scripts to create the buttons and sliders taken from https://github.com/araoux/python_agregation (written by P Cladé, A Raoux and F Levrier)

WARNING this program requires the widgets.py file to work
'''

import numpy as np
import matplotlib.pyplot as plt
import widgets


parameters = {
    'pKa1' : widgets.FloatSlider(value=4, description = 'pKa$_1$', min=0, max=14),
    'pKa2' : widgets.FloatSlider(value=10, description = 'pKa$_1$', min=0, max=14),
    }
def Concentrations(Ca,pH,pKa1,pKa2):
    Ka1 = 10**(-pKa1)
    Ka2 = 10**(-pKa2)
    h = 10**(-pH)
    AH2 = Ca/(1+Ka1*Ka2/h**2+Ka1/h)
    AH = Ka1/h*AH2
    A = Ka2/h*AH
    return AH2,AH,A

def plot_data(pKa1,pKa2):
    Ca = 0.01
    pH = np.linspace(0, 14, 1000)
    C = Concentrations(Ca,pH,pKa1,pKa2)
    lines['AH2'].set_data(pH,C[0])
    lines['AH'].set_data(pH,C[1])
    lines['A'].set_data(pH,C[2])
    ax.set_xlim(min(pH),max(pH))
    ax.set_ylim(0,Ca)
    fig.canvas.draw_idle()


if __name__ == "__main__":
    fig=plt.figure()
    ax = fig.add_axes([0.15, 0.25, 0.6, 0.65])
    lines = {}
    lines['AH2'], = ax.plot([],[],label='[$AH_2$]',color='C0',ls='-')
    lines['AH'], = ax.plot([],[],label='[$AH^-$]',color='C1',ls='-')
    lines['A'], = ax.plot([],[],label='[$A^{2-}$]',color='C2',ls='-')
    param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.25, 0.05, 0.4, 0.05])
    reset_button = widgets.make_reset_button(param_widgets,box=[0.75, 0.05, 0.15, 0.05])
    fig.suptitle("Diagramme Diacide", fontweight='bold')
    fig.legend(loc='center right',fontsize='x-large')
    ax.grid(True)
    ax.set_xlabel('pH',fontsize=16)
    ax.set_ylabel(r'$C\ (\rm mol.L^{-1})$',fontsize=16)
    fig.tight_layout()
    plt.show()