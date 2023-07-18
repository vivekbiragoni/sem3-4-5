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
def display_info_circuit():
    info_text = '''
    Info about the Circuit Diagram:
    The circuit diagram represents the sequence of gates applied to the qubits in the quantum circuit.

    - Each box corresponds to a gate, and the lines represent the qubits.
    - The arrows indicate the direction of information flow.
    - The labels on the gates provide information about the gate type and parameters.

    Note: The circuit diagram provides a visual representation of the quantum circuit.

    '''

    info_window = tk.Toplevel()
    info_window.title('Info')
    info_label = tk.Label(info_window, text=info_text, padx=10, pady=10)
    info_label.pack()
# def display_circuit():
#     """
#     Display the circuit diagram
#     """
#     global circuit
#     print(circuit)
#     circuit_drawer(circuit, output='mpl').show()