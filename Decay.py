import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to simulate radioactive decay
def radioactive_decay(initial_atoms, decay_constant, time_span_years, time_step_years):
    time_points = np.arange(0, time_span_years, time_step_years)
    remaining_atoms = initial_atoms * np.exp(-decay_constant * time_points)
    return time_points, remaining_atoms

# Streamlit UI
st.title('Radioactive Decay Simulation')

# User input
initial_atoms = st.number_input('Enter initial number of atoms:', min_value=1, value=1000)
decay_constant = st.number_input('Enter decay constant:', min_value=0.0, value=0.00043)
time_span_years = st.number_input('Enter time span (in years):', min_value=1, value=5000)
time_step_years = st.number_input('Enter time step (in years):', min_value=1, value=10)

# Simulation
time_points, remaining_atoms = radioactive_decay(initial_atoms, decay_constant, time_span_years, time_step_years)

# Plot results
fig, ax = plt.subplots()
ax.plot(time_points, remaining_atoms)
ax.set_title('Radioactive Decay Simulation')
ax.set_xlabel('Time (years)')
ax.set_ylabel('Remaining Atoms')
ax.grid(True)

# Show plot in Streamlit
st.pyplot(fig)