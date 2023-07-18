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
def display_circuit():
    """
    Display the circuit diagram
    """
    global circuit
    
    # Create a new window for the circuit diagram
    window = tk.Toplevel()
    window.title('Circuit Diagram')
    
    # Create the circuit diagram using circuit_drawer
    circuit_diagram = circuit_drawer(circuit, output='mpl')
    
    # Create a canvas to display the circuit diagram
    canvas = FigureCanvasTkAgg(circuit_diagram, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    # Create the info button
    info_button = tk.Button(window, text="Info", command=display_info_circuit)
    info_button.pack(pady=10)
