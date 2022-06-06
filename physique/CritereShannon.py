import numpy as np
import matplotlib.pyplot as plt
import widgets
#from math import *

## CONSTANTES

T = 1.0

## FONCTIONS
def signal(t):
    return np.sin(2.*np.pi*t/T)

def fourier(tstep, signal):
    n = signal.size
    fourier = np.fft.rfft(signal)
    freq_e = np.fft.rfftfreq(n, tstep)
    return freq_e, fourier


# Echantillonnage
parameters = {'Te' : widgets.FloatSlider(value=0.01, description='$T_e(s)$', min=1e-3, max=1),
}

def plot_data(Te):
    D = 50. # Duree d'observation
    fe = 1/Te # Frequence d'echantillonnage
    N = int(D * fe) + 1 # Nombre de points enregistres
    te = np.linspace(0., (N-1)/fe, N) # Grille d'echantillonnage
    tp = np.linspace(0., D, 100000) # Grille plus fine pour tracer l'allure du signal parfait
    FSE = np.abs(fourier(Te, signal(te)))
    FSR = np.abs(fourier(D/100000, signal(tp)))

    lines['Signal echantillonné'].set_data(te, signal(te))
    lines['Signal réel'].set_data(tp, signal(tp))
    lines['Fréquence Signal echantillonné'].set_data(FSE[0], FSE[1]/max(FSE[1]))
    lines['Fréquence Signal réel'].set_data(FSR[0], FSR[1]/max(FSR[1]))
    ax1.set_ylim(min(signal(tp)-0.1),max(signal(tp)+0.1))
    ax1.set_xlim(0,5*T)
    ax2.set_ylim(-0.1,1.1)
    ax2.set_xlim(0,FSR[0,3*FSR[1].argmax()])

    fig.canvas.draw_idle()
## Trace du signal
fig,axes=plt.subplots(2,1)
ax1 = plt.subplot(2,1,1)
ax2 = plt.subplot(2,1,2)

plt.grid()
ax1.set_xlabel("Temps t (s)")
ax1.set_ylabel("Amplitude $x(t)$")

ax2.set_xlabel("Frequence f (Hz)")
ax2.set_ylabel("Amplitude Normalisée")
# plt.ylim((-1.1,1.4))
plt.legend(loc='upper right')


lines = {}
lines['Signal echantillonné'], = ax1.plot([], [], lw=1, color='red',  marker='o', label = 'Signal échantillonné',markersize = '4')
lines['Signal réel'], = ax1.plot([], [], lw=2, color='blue', label = "Signal réel")
lines['Fréquence Signal echantillonné'], = ax2.plot([], [], lw=1, color='red',  marker='o', label = 'Signal échantillonné',markersize = '3')
lines['Fréquence Signal réel'], = ax2.plot([], [], lw=2, color='blue', label = "Signal réel")
# texts=  fig.text(0.75, 0.8, '$x=$', fontsize=10,ha='center')
ax2.legend(loc ='upper right')
ax1.set_title("Echantillonage d'un signal analogique")

##Définition d'un slider
param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.2, 0.05, 0.40, 0.05])
## Définition d'un bouton reset

reset_button = widgets.make_reset_button(param_widgets,box=[0.7, 0.05, 0.10, 0.05])

if __name__=='__main__':
    plt.subplots_adjust(left=0.1,bottom=0.2,right=0.9,top=0.9,wspace=0.3,hspace=0.4)
    plt.show()



