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
#Define Layout
#Define the  Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both', expand=True)

#Define display frame layout
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify="left")
display.pack(padx=3,pady=4)

# Create the state_display text widget
state_display = tkinter.Text(display_frame, width=80, height=2, font=button_font)
state_display.pack(padx=3, pady=4)

# Add a label for the state display
state_label = tkinter.Label(display_frame, text="State Display", font=button_font)
state_label.pack(pady=(10, 0))

# Define the layout for state_display and state_label
state_label.pack(pady=(10, 0))
state_display.pack(padx=3, pady=(0, 4))


#First Row of buttons
#First Row of buttons
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X', command= lambda:[display_gate('x'),circuit.x(0)])
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y', command= lambda:[display_gate('y'),circuit.y(0)])
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z', command= lambda:[display_gate('z'),circuit.z(0)])

x_gate.grid(row=0,column=0,ipadx=45, pady=1,sticky='ew')
y_gate.grid(row=0,column=1,ipadx=45, pady=1,sticky='ew')
z_gate.grid(row=0,column=2,ipadx=53, pady=1, sticky='WE')

#Second Row of Buttons
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RX', command = lambda:[display_gate('Rx'), user_input(circuit,'x')])
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RY', command = lambda:[display_gate('Ry'), user_input(circuit,'y')])
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='RZ', command = lambda:[display_gate('Rz'), user_input(circuit,'z')])
Rx_gate.grid(row=1,column=0, columnspan=1, pady=1, sticky='WE')
Ry_gate.grid(row=1,column=1, columnspan=1, pady=1, sticky='WE')
Rz_gate.grid(row=1,column=2, columnspan=1, pady=1, sticky='WE')

#Third Row of buttons
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S', command= lambda:[display_gate('S'),circuit.s(0)])
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD', command= lambda:[display_gate('SD'),circuit.sdg(0)])
hadamard = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H', command= lambda:[display_gate('h'),circuit.h(0)])
s_gate.grid(row=2,column=0, columnspan=1, pady=1, sticky='WE')
sd_gate.grid(row=2,column=1, pady=1, sticky='WE')
hadamard.grid(row=2,column=2, rowspan=2, pady=1, sticky='WENS')

#Fourth row of buttons
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T', command= lambda:[display_gate('T'),circuit.t(0)])
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD', command= lambda:[display_gate('TD'),circuit.tdg(0)])
t_gate.grid(row=3,column=0, pady=1, sticky='WE')
td_gate.grid(row=3,column=1, pady=1, sticky='WE')

#Quit and Visualize button
quit = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Quit', command=root.destroy)
visualize = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Visualize', command =lambda:visualize_circuit(circuit,root))
quit.grid(row=4,column=0, columnspan=2,ipadx=5, pady=1, sticky='WE')
visualize.grid(row=4,column=2, columnspan=1,ipadx=8, pady=1, sticky='WE')

#Clear button
clear_button = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Clear', command= lambda:clear(circuit))
clear_button.grid(row=6,column=2, columnspan=1, sticky='WE')

#About button
about_button = tkinter.Button(button_frame, font=button_font, bg=buttons, text='About', command= lambda:about())
about_button.grid(row=6,column=0, columnspan=2, sticky='WE')

# ...

# Additional buttons and menu
display_circuit_button = tkinter.Button(button_frame, text="Circuit diagram",  bg=buttons, font=button_font, command=lambda: display_circuit())
display_circuit_button.grid(row=5, column=0, columnspan=2, sticky='WENS')
# Create the info button for the circuit diagram
# info_button_circuit = tk.Button(root, text="Circuit Info", command=display_info_circuit)
# info_button_circuit.pack(pady=10)

display_state_button = tkinter.Button(button_frame, text="Display state",  bg=buttons, font=button_font, command=lambda: display_state())
display_state_button.grid(row=5, column=2, columnspan=1, sticky='WENS')
