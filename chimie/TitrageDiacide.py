'''
Ce code a été récupéré sur : https://www.astrolabe-science.fr/courbes-titrage-acido-basiques-python/ . Je remercie les auteurs pour avoir partagé leur travail.
Ce code a été modifié et rendu interactif par Raphael Rullan.

L'aspect mathématique du code se base sur l'article : https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/pdf/10.1002/cem.719
On étudie ici le dosage d'un diacide AH2. Les couples considérés sont : AH2/AH- AH-/A2-.
On considére la base B.

Explication des maths :
    en appliquant au système la conservation de la masse et l'électroneutralité de la solution on peut trouver 2 équations. En utilisant les formules des constantes d'équilibre
    Ka1, Ka2, Ke, on peut arriver à déterminer sans approximation la concentration en H3O+ à tout instant. L'équation final trouvée est un polynome de degré 4 (d'où la forme du code)


Je remercie Vincent Wieczny pour m'avoir fourni le module Widgets

Edited _ Timothee Chauvire June 04th 2022
'''



import numpy as np
import numpy.polynomial.polynomial as nppol# pour le polynôme
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker # pour le format des étiquettes en x (remplacer le point décimal par la virgule)
import widgets
# Paramêtres acido-basiques

parameters = {'Ca' : widgets.FloatSlider(value=0.12, description='concentration initiale en acide (mol/L)', min=0.00001, max=1),
              'Cb'  : widgets.FloatSlider(value = 0.1, description='concentration du titrant (mol/L)', min = 0.00001, max =1),
              'pKa1'  : widgets.FloatSlider(value = 3.9, description='pKa du couple 1', min = 0, max = 14),
              'pKa2' : widgets.FloatSlider(value = 10, description='pKa du couple 2', min = 0, max = 14),
              'Va' : widgets.FloatSlider(value = 10., description='Volume initial (mL)', min = 1, max = 100),}


Ke=1e-14# produit ionique de l'eau


#réglage perso de la grille secondaire du graphe :
fig=plt.figure(figsize=(12,10))

ax = fig.add_subplot(3, 1, (1, 2))
ax.grid(which='minor', alpha=0.2)



def plot_data(pKa1, pKa2, Va, Ca, Cb):
    # valeurs déduites des paramêtres :
    Ka1=10**(-pKa1)
    Ka2=10**(-pKa2)
    Vbmin=0
    Veq=Ca*Va/Cb
    Vbmax=np.int(4*Veq)
    volume = np.linspace(Vbmin, Vbmax, 1024,endpoint=True)
    def concentration(Vb):#Calcule [H3O+]
        a=Ka1+Cb*Vb/(Vb+Va)# a, b et c les coefficients du polynôme
        b= Ke+Ka1*(Ca*Va-Cb*Vb)/(Vb+Va)-Ka1*Ka2
        c=Ka1*Ke+Ka1*Ka2*(2*Ca*Va-Cb*Vb)/(Va+Vb)
        d=Ke*Ka1*Ka2
        vm = nppol.polyroots([-d,-c,-b,a,1])#chercher les racines du polynôme
        positive=filter(lambda x: x>0,filter(np.isreal,vm))
        C=next(positive)
        return C

    def titrage(Vbmin,Vbmax):# calcul du pH
        ph=-np.log10(np.vectorize(concentration)(volume))
        return volume,ph
    V = titrage(Vbmin, Vbmax)[0]
    pH = titrage(Vbmin, Vbmax)[1]
    a['Courbe pH'].set_data(V, pH)
    ax.set_xlim(0, Vbmax)
    ax.set_ylim(0, 14)#limites des axes
    ax.set_yticks(np.arange(0, 14, 1))# ajuster l'espace entre valeurs axe y
    ax.set_xticks(np.arange(0, Vbmax, np.int(Vbmax/10)))# ajuster l'espace entre valeurs axe x

a = {}
a['Courbe pH'], = plt.plot([], [],'b-', label="Evolution pH")
plt.title("Titrage pH-métrique d'un diacide")
plt.xlabel(r'Volume $V_b$ de base versé (mL)')
plt.ylabel("pH")
plt.grid()



param_widgets = widgets.make_param_widgets(parameters, plot_data, slider_box=[0.3, 0.05, 0.45, 0.15])
reset_button = widgets.make_reset_button(param_widgets,box=[0.85, 0.1, 0.08, 0.05])


plt.show()