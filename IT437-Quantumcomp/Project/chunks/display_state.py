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
def display_state():
    """
    Display the probability percentage vs basis, amplitude vs basis, and the state information within the GUI
    """
    global backend
    
    # Execute the circuit and obtain the statevector
    job = execute(circuit, backend=backend, shots=1)
    result = job.result()
    statevector = result.get_statevector(circuit)
    
    # Compute the probability percentages
    probabilities = np.abs(statevector) ** 2
    
    # Create the basis labels for x-axis
    basis_labels = [f"|{i}>" for i in range(len(statevector))]
    
    # Create the probability percentage vs basis plot
    fig1 = plt.figure(figsize=(8, 6))
    plt.bar(range(len(statevector)), probabilities, color='steelblue')
    plt.xticks(range(len(statevector)), basis_labels, fontsize=10)
    plt.xlabel('Basis', fontsize=12)
    plt.ylabel('Probability Percentage', fontsize=12)
    plt.title('Probability Percentage vs Basis', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Create the amplitude vs basis plot
    fig2 = plt.figure(figsize=(8, 6))
    plt.bar(range(len(statevector)), np.abs(statevector), color='darkorange')
    plt.xticks(range(len(statevector)), basis_labels, fontsize=10)
    plt.xlabel('Basis', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.title('Amplitude vs Basis', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Create the state display string
    state_text = "Qubit: "
    for i, probability in enumerate(probabilities):
        computational_basis_state = f"|{i}⟩"
        state_amplitude = f"({statevector[i].real:.3f}+{statevector[i].imag:.3f}j)"
        state_text += f"{state_amplitude}{computational_basis_state} "
        if i < len(probabilities) - 1:
            state_text += "+ "
    state_text = state_text.strip()  # Remove trailing whitespace
     # Insert the state display string into the text widget
    state_display.config(state='normal')
    state_display.delete('1.0', tkinter.END)  # Clear the text widget
    state_display.insert(tkinter.END, state_text + '\n')
    state_display.config(state='disabled')
    
    # Create Tkinter windows to display the plots and state information
    window1 = tk.Toplevel()
    canvas1 = FigureCanvasTkAgg(fig1, master=window1)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    info_button1 = tk.Button(window1, text="Info", command=display_info)
    info_button1.pack(pady=10)

    window2 = tk.Toplevel()
    canvas2 = FigureCanvasTkAgg(fig2, master=window2)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    info_button2 = tk.Button(window2, text="Info", command=display_info)
    info_button2.pack(pady=10)
    # Add some additional styling to the plots
    plt.tight_layout()
    fig1.patch.set_alpha(0)  # Make the figure background transparent
    fig2.patch.set_alpha(0)
    # state_window = tk.Toplevel()
    # state_display = tk.Text(state_window, height=5, width=50)
    # state_display.insert(tk.END, state_text)
    # state_display.pack()

    # state_window.mainloop()
           
