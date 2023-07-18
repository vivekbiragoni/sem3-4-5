#define function for about
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
def about():
    """
    Displays information about the Qubit Rotation Simulator.
    """

    info = tkinter.Tk()
    info.title('About')
    info.geometry('650x470')
    info.resizable(0, 0)

    text = tkinter.Text(info, height=20, width=20)

    # Create Label
    label = tkinter.Label(info, text="QuantumVizier: Visualizing the Quantum World")
    label.config(font=("Arial", 14))

    text_to_display = """
    Qubit Rotation Simulator
    
    Created by: Vivek, Tejdeep, Sagar
    Using: Qiskit, Python, Tkinter
    
    The Bloch Sphere is a visual representation of the state space of a single 
    qubit in quantum computing. It provides a geometric representation of the 
    possible states a qubit can be in.
    
    Gate Buttons and Qiskit Commands:
    
    X: Flip the state of the qubit
       Command: circuit.x(0)
    
    Y: Rotate the state vector about the Y-axis
       Command: circuit.y(0)
    
    Z: Flip the phase of the qubit by PI radians
       Command: circuit.z(0)
    
    Rx: Parameterized rotation about the X-axis
        Command: circuit.rx(angle, 0)
    
    Ry: Parameterized rotation about the Y-axis
        Command: circuit.ry(angle, 0)
    
    Rz: Parameterized rotation about the Z-axis
        Command: circuit.rz(angle, 0)
    
    S: Rotate the state vector about the Z-axis by PI/2 radians
       Command: circuit.s(0)
    
    T: Rotate the state vector about the Z-axis by PI/4 radians
       Command: circuit.t(0)
    
    Sd: Rotate the state vector about the Z-axis by -PI/2 radians
        Command: circuit.sdg(0)
    
    Td: Rotate the state vector about the Z-axis by -PI/4 radians
        Command: circuit.tdg(0)
    
    H: Create the state of superposition
       Command: circuit.h(0)
    
    Note: For Rx, Ry, and Rz gates, the rotation angle (theta) allowed range is [-2*PI, 2*PI].
    
    If a visualization error occurs, the application will close automatically,
    indicating that visualization of your circuit is not possible.
    
    Please note that only up to ten operations can be visualized at a time.
    """

    label.pack()
    text.pack(fill='both', expand=True)

    # Inserting the text
    text.insert(tkinter.END, text_to_display)

    # Run
    info.mainloop()