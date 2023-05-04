from qiskit import QuantumCircuit
import qiskit
from qiskit.visualization import visualize_transition #import os  (check import os , not required mostly)
import numpy as np
import tkinter
from tkinter import LEFT, END, DISABLED, NORMAL
import warnings

warnings.filterwarnings('ignore')

#Define Window
root = tkinter.Tk()
root.title('Qbit Rotation Simulator')

#set size
root.geometry('435x330')
root.resizable(0,0)

# #Define color and fonts
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial', 18)
display_font = ('Arial', 32)

# Inititalize the Quantum circuit
def initialize_circuit():
	global circuit
	circuit =QuantumCircuit(1)

initialize_circuit()
theta =0

	

#Define functions

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


def clear(circuit):
    """
    Clears the display!
    Reinitializes the quantum circuit for fresh calculations
    Checks if the gate button are disabled, if so , enables the buttons
    """
    #clear the display 
    display.delete(0,END)

    #reset the circuit to initial state |0>
    initialize_circuit()

    #checks if the button are disabled, if so , enables them
    if x_gate['state']== DISABLED:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard]
        for gate in gates:
            gate.config(state=NORMAL)

#define function for about
def about():
    """
    Displays the info about Project"
    """
    
    info = tkinter.Tk()
    info.title('About')
    info.geometry('650x470')
    info.resizable(0,0)

    text = tkinter.Text(info, height=20, width= 20)

    #Create Label
    label= tkinter.Label(info, text= "About Qbit Rotation Simulator: ")
    label.config(font=("Arial",14))


    text_to_display ="""
    About: Visualization tool for a single qubit rotation on block sphere

    By: Qubits Muskeeters
    Created using : Qiskit, Python, Tkinter

    Info about gate buttons and corresponding qiskit commands:

    X= flips the states of qubits -                             circuit.x()
    Y= rotates the state vector about Y-axis -                  circuit.y()
    Z= flips the phase of PI radians -                          circuit.z()
    Rx= parameterized rotation about the X axis -               circuit.rx()
    Ry= parameterized rotation about the Y axis -               circuit.ry()
    Rz= parameterized rotation about the Z axis -               circuit.rz()
    S= rotates the state vector about Z axis by PI/2 radians -  circuit.s()
    T= rotates the state vector about Z axis by PI/4 radians -  circuit.t()
    Sd= rotates the state vector about Z axis by -PI/2 radians- circuit.sdg()
    Td= rotates the state vector about Z axis by -PI/4 radians- circuit.tdg()
    H= creates the state of Superposition -                     circuit.h()

    For Rx,Ry and Rz,
    theta(rotation_angle) allowed range in the app is [-2*PI,2*PI]

    In case of a Visualization Error, the app closes automatically.
    This indicates that visualization of your circuit is not possible.

    At a time, only ten operations can be visualized.
    """

    label.pack()
    text.pack(fill='both',expand =True)

    #Inserting the text
    text.insert(END,text_to_display)

    #run
    info.mainloop()
def visualize_circuit(circuit,window):
    """
    Visualizes the single qubit rotations corresponding to applied gates in a separate tkinter window.
    Handles any possible visualization error
    """
    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()

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

def user_input(circuit,key):
    """
    Take the user input for rotation angle for parameterized
    Rotation gates Rx,Ry,Rz.
    """

    #Initialize and define the properties of window
    get_input = tkinter.Tk()
    get_input.title('Get theta')    
    get_input.geometry('360x210')
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

#Define Layout
#Define the  Frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both', expand=True)

#Define display frame layout
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify="left")
display.pack(padx=3,pady=4)

#First Row of buttons
#First Row of buttons
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X', command= lambda:[display_gate('x'),circuit.x(0)])
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y', command= lambda:[display_gate('y'),circuit.y(0)])
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z', command= lambda:[display_gate('z'),circuit.z(0)])
x_gate.grid(row=0,column=0,ipadx=45, pady=1)
y_gate.grid(row=0,column=1,ipadx=45, pady=1)
z_gate.grid(row=0,column=2,ipadx=53, pady=1, sticky='E')

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
clear_button.grid(row=5,column=0, columnspan=3, sticky='WE')

#About button
about_button = tkinter.Button(button_frame, font=button_font, bg=buttons, text='About', command=about)
about_button.grid(row=6,column=0, columnspan=3, sticky='WE')


#Run main loop
root.mainloop()
