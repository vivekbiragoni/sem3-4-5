from qiskit import QuantumCircuit
import qiskit
from qiskit.visualization import visualize_transition #import os  (check import os , not required mostly)
import numpy as np
import tkinter
from tkinter import LEFT, END, DISABLED, NORMAL
import warnings
from qiskit import execute
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from qiskit import Aer
from qiskit.visualization import circuit_drawer
from qiskit.visualization import plot_bloch_vector
from tkinter import messagebox
warnings.filterwarnings('ignore')
import display_circuit, display_state, change_theta, clear, initialise,visualize_circuit, user_input_theta
import gui, about

# Define the backend
backend = Aer.get_backend('statevector_simulator')

#Define Window
root = tkinter.Tk()
root.title('QuantumVizier')

#set size
root.geometry('440x565')
root.resizable(1,1)

# #Define color and fonts
background = '#2c94c8'
buttons = '#66C2FF'
special_buttons = '#bc3454'
button_font = ('Verdana', 18)
display_font = ('Arial', 32)

# Inititalize the Quantum circuit
def initialize_circuit():
	global circuit
	circuit =QuantumCircuit(1)

initialize_circuit()
theta =0

#Run main loop
root.mainloop()