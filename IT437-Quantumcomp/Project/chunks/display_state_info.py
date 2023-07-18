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
def display_info():
    info_text = '''
    Info about the plot:
    This plot represents the probability percentage or amplitude of each computational basis state in the quantum state.

    - Probability Percentage vs Basis: This bar chart shows the probability percentage of each basis state.
    - Amplitude vs Basis: This bar chart shows the amplitude (magnitude) of each basis state.

    Note: The state display below the plot provides the complex representation of each basis state.

    '''

    info_window = tk.Toplevel()
    info_window.title('Info')
    info_label = tk.Label(info_window, text=info_text, padx=10, pady=10)
    info_label.pack()
