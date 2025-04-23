"""Interactive Linear Graph Plotter"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App title
st.title("Interactive Linear Graph Plotter")

with st.sidebar:
    st.header("Linear Graph App!")
    st.write("y = mx + b")

st.markdown("Enter values for the linear equation: **y = mx + b**")
m = st.number_input("Slope (m)", step=0.5, format="%.2f")
b = st.number_input("Y-Intercept (b)", step=0.5, format="%.2f")

# Zoom controls
st.markdown("### Adjust Zoom/Scale")
x_range = st.slider("X-axis Range", min_value=1, max_value=20, value=10, step=1)
y_range = st.slider("Y-axis Range", min_value=1, max_value=20, value=10, step=1)

# Plot button
plot = st.button("Plot Slope")

if plot:
    # Create figure
    fig, ax = plt.subplots(figsize=(5, 5), dpi=40)

    # Define x and y range based on user input
    x = np.linspace(-x_range, x_range, 400)
    y = m * x + b

    # Plot the linear equation
    ax.plot(x, y, label=f"y = {m}x + {b}", color='blue')

    # Grid lines with minor ticks for 0.5 spacing
    ax.grid(which='major', linestyle='-', linewidth=0.5)
    ax.minorticks_on()
    ax.grid(which='minor', linestyle=':', linewidth=0.3)

    # Set axis ticks (whole integers)
    ax.set_xticks(range(-x_range, x_range + 1, 1))
    ax.set_yticks(range(-y_range, y_range + 1, 1))

    # Smaller tick labels
    ax.tick_params(axis='both', labelsize=8)

    # Axis lines at zero
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Axis limits
    ax.set_xlim(-x_range, x_range)
    ax.set_ylim(-y_range, y_range)

    # Label axes
    ax.set_xlabel("x", loc='right')
    ax.set_ylabel("y", loc='top')

    # Display the plot
    st.pyplot(fig)
