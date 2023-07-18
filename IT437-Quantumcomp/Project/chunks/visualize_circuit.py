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
def visualize_circuit(circuit, window):
    """
    Visualizes the single qubit rotations corresponding to applied gates in a separate tkinter window.
    Handles any possible visualization error and provides informative error messages.
    """
    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.VisualizationError as e:
        error_message = f"An error occurred during visualization: {str(e)}"
        # Display the error message to the user using messagebox.showerror
        messagebox.showerror("Visualization Error", error_message)
        # Destroy the window or perform any necessary cleanup
        window.destroy()