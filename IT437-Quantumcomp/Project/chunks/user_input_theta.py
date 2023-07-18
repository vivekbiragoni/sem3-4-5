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
def user_input(circuit,key):
    """
    Take the user input for rotation angle for parameterized
    Rotation gates Rx,Ry,Rz.
    """

    #Initialize and define the properties of window
    get_input = tkinter.Tk()
    get_input.title('Get theta')    
    get_input.geometry('540x315')
    get_input.resizable(0,0)

    val1= tkinter.Button(get_input, height=2, width=10, bg= buttons, font=("Arial,10") ,text='PI/4', command= lambda:change_theta(0.25,get_input,circuit,key ))
    val1.grid(row=0, column=0)

    val2= tkinter.Button(get_input, height=2, width=10, bg= buttons, font=("Arial,10") ,text='PI/2', command= lambda:change_theta(0.50,get_input,circuit,key ))
    val2.grid(row=0, column=1)

    val3= tkinter.Button(get_input, height=2, width=10, bg= buttons, font=("Arial,10") ,text='PI', command= lambda:change_theta(1.0,get_input,circuit,key ))
    val3.grid(row=0, column=2)

    val4= tkinter.Button(get_input, height=2, width=10, bg= buttons, font=("Arial,10") ,text='2*PI', command= lambda:change_theta(2.0,get_input,circuit,key ))
    val4.grid(row=0, column=3, sticky ='W')

    nval1= tkinter.Button(get_input, height=2, width=10, bg= buttons, font=("Arial,10") ,text='-PI/4', command= lambda:change_theta(-0.25,get_input,circuit,key ))
    nval1.grid(row=1, column=0)

    nval2= tkinter.Button(get_input, height=2, width=10, bg= buttons, font=("Arial,10") ,text='-PI/2', command= lambda:change_theta(-0.50,get_input,circuit,key ))
    nval2.grid(row=1, column=1)

    nval3= tkinter.Button(get_input, height=2, width=10, bg= buttons, font=("Arial,10") ,text='-PI', command= lambda:change_theta(-1.0,get_input,circuit,key ))
    nval3.grid(row=1, column=2)

    nval4= tkinter.Button(get_input, height=2, width=10, bg= buttons, font=("Arial,10") ,text='-2*PI', command= lambda:change_theta(-2.0,get_input,circuit,key ))
    nval4.grid(row=1, column=3, sticky ='W')

    text_object= tkinter.Text(get_input, height=20, width=20, bg="light cyan")

    note = """
    give the value for theta
    the value has the range [-2*PI,2*PI]
    """

    text_object.grid(sticky='WE',columnspan=4)
    text_object.insert(END,note)


    get_input.mainloop()
