# Statistical Processing Control Demo - Fridge Temperature Evaluation
# Author: Oscar Yang

# Program Description:
# This program reads FridgeTemp.csv data from a remote URL and plots a statistical 
# processing control chart of the temperature in Celsius. The control chart shows 
# the mean, upper control limit, and lower control limit for the data, which are 
# calculated using the mean and standard deviation. The purpose of this program is 
# to demonstrate how to create a control chart using matplotlib in Python.

# Required libraries: pandas, numpy, matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data into a pandas dataframe
url = "https://raw.githubusercontent.com/yangoscar/IndustrialEngineeringMethodologies/main/FridgeTemp.csv"
data = pd.read_csv(url)

# Calculate mean and standard deviation
mean = np.mean(data['FridgeTempCelsius'])
std_dev = np.std(data['FridgeTempCelsius'])

# Calculate control limits
upper_control_limit = mean + 1.5 * std_dev
lower_control_limit = mean - 1.5 * std_dev

# Create statistical processing control chart using matplotlib
fig, ax = plt.subplots()
ax.plot(data['FridgeTempCelsius'])
ax.axhline(y=mean, color='r', linestyle='-')
ax.axhline(y=upper_control_limit, color='g', linestyle='--')
ax.axhline(y=lower_control_limit, color='g', linestyle='--')
plt.xlabel("Days")
plt.ylabel("Temperature (Celsius)")
plt.title("Statistical Processing Control Demo - Fridge Temperature Evaluation")
plt.show()