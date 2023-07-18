#Define functions
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

def display_gate(gate_input):
    """
    Adds corresponding gate notation in the display to track all operations
    If the number of operation reaches 10, all gate buttons are disabled
    """
    #Insert the defined gate
    display.insert(END,gate_input)

    #Check if the number of operations has reached ten, if yes,
    #disable all the gate buttons
    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates =list(input_gates)
    search_word = ["R","D"]
    count_double_valued_gates =[list_input_gates.count(i) for i in search_word]
    num_gates_pressed -= sum(count_double_valued_gates)
    if num_gates_pressed ==10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard]
        for gate in gates:
            gate.config(state = DISABLED)