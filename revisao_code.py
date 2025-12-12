# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 09:16:40 2025

@author: SKYLAB
"""

import streamlit as st
#st.title ("Olá Maria Dos Anjos")#
from streamlit_option_menu import option_menu
import pandas as pd
#import matplotlib as mpl
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np


with st.sidebar:
    escolha = option_menu (
        "Navegação", ["Iniciar", "Editar", "Salvar", "Enviar"], menu_icon="cost", icons=["house", "bar-chart", "search", "graph-up-arrow"], default_index=0)
    
if escolha == "Iniciar":
    st.title ("Inicinado!")
    df= pd.DataFrame({"X":[1,2],"Y":[2,3]})
    st.write (df.describe())
      
    
if escolha == "Editar":
    st.title ("Editando!")
    x = np.linspace(-5,2,100)
    y1 = x**3 + 5*x**2 + 10
    y2 = 3*x**2 + 10*x
    y3 = 6*x +10
    fig, ax = plt.subplots()
    ax.plot (x,y1, color="blue", label="y(x)")
    ax.plot (x,y2, color="red", label="y'(x)")
    ax.plot (x,y3, color="green", label="y''(x)")
    ax.set_xlabel("tempo")
    ax.set_xlabel("espaço")
    ax.legend()
    st.pyplot(fig)
   
    
if escolha == "Salvar":
    st.title ("Salvando!")
    
    
if escolha == "Enviar":
    st.title ("Enviando!")
    s = pd.Series(
    [909976, 8615246, 2872086, 2273305],  # valores
    index=["Estocolmo", "Londres", "Roma", "Paris"],  # índice
    name="População"
        )
    s
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    s.plot(ax=axes[0], kind='line', title='linha')
    s.plot(ax=axes[1], kind='bar', title='linha')
    s.plot(ax=axes[2], kind='box', title='box')
    s.plot(ax=axes[3], kind='pie', title='circular')
    st.pyplot(fig)



    
