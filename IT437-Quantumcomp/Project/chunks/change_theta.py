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
def change_theta(num,window,circuit,key):
    """
    Changes the global variable theta and destroys the window
    """
    global theta
    theta= num*np.pi
    if key == 'x':
        circuit.rx(theta,0)
        theta=0
    elif key == 'y':
        circuit.ry(theta,0)
        theta=0
    else:
        circuit.rz(theta,0)
        theta=0
    window.destroy()