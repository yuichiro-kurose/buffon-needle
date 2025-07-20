# To run this program, you need to install the following libraries:
# pip install matplotlib numpy

import matplotlib
matplotlib.use('TkAgg') # Specify the backend to ensure a window can be shown
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Simulation Parameters ---
# Distance between the parallel lines
LINE_DISTANCE = 2.0
# Length of the needle
NEEDLE_LENGTH = 1.0
# Animation update interval in milliseconds (1ms = 0.1s)
ANIMATION_INTERVAL = 100

# --- Simulation State ---
# Counter for the total number of needles dropped
total_needles = 0
# Counter for the number of needles that crossed a line
crossed_needles = 0

# --- Setup the Plot ---
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.set_title("Buffon's Needle Simulation", fontsize=16)

# Set plot limits to provide some margin
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)

# Remove axis ticks for a cleaner look
ax.set_xticks([])
ax.set_yticks([])

# Draw the parallel lines
ax.axhline(y=0, color='black', linestyle='-', linewidth=2)
ax.axhline(y=LINE_DISTANCE, color='black', linestyle='-', linewidth=2)

# Prepare a text box for displaying statistics
stats_text = ax.text(
  0.02, 0.98, '', transform=ax.transAxes,
  fontsize=12, verticalalignment='top',
  bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
)

def update(frame):
  """
  This function is called for each frame of the animation.
  It simulates dropping one needle and updates the plot and statistics.
  """
  global total_needles, crossed_needles

  # Increment the total needle count
  total_needles += 1

  # --- Simulate dropping one needle ---
  y_center = np.random.uniform(0, LINE_DISTANCE)
  x_center = np.random.uniform(-1.5, 1.5)
  theta = np.random.uniform(0, np.pi)

  y_tip = y_center + (NEEDLE_LENGTH / 2) * np.sin(theta)
  y_tail = y_center - (NEEDLE_LENGTH / 2) * np.sin(theta)
  
  is_crossed = (y_tail <= 0) or (y_tip >= LINE_DISTANCE)

  if is_crossed:
    crossed_needles += 1
    line_color = 'red'
  else:
    line_color = 'blue'

  # --- Draw the needle on the plot ---
  x_tip = x_center + (NEEDLE_LENGTH / 2) * np.cos(theta)
  x_tail = x_center - (NEEDLE_LENGTH / 2) * np.cos(theta)
  ax.plot([x_tail, x_tip], [y_tail, y_tip], color=line_color, linewidth=0.5)

  # --- Update the statistics text (MODIFIED SECTION) ---
  num_A = crossed_needles # Crossed
  num_B = total_needles - crossed_needles # Not Crossed

  # Calculate the approximation of Pi for L=1, D=2
  # Pi approx. = Total / Crossed
  pi_approximation = total_needles / num_A if num_A > 0 else float('nan')

  # Calculate the ratio of Crossed / Total
  # Theoretical value should approach 1/π ≈ 0.318
  crossed_div_total = num_A / total_needles if total_needles > 0 else 0

  # Create the text content with the new format
  text_content = (
    f"Total Needles: {total_needles}\n"
    f"--------------------\n"
    f"Crossed: {num_A}\n"
    f"Not Crossed: {num_B}\n"
    f"--------------------\n"
    f"Approximation of π\n"
    f"(Crossed / Total): {crossed_div_total:.6f}\n" # Note: This value approximates 1/π
    f"(Total / Crossed): {pi_approximation:.6f}"
  )
  
  # Update the text on the plot
  stats_text.set_text(text_content)


# --- Create and run the animation ---
ani = FuncAnimation(
  fig, update, interval=ANIMATION_INTERVAL, cache_frame_data=False
)

# Display the plot window
plt.tight_layout()
plt.show()
