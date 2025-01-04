import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'data/aipidata.xlsx'  # Relative path to the data folder
ai_df = pd.read_excel(file_path, skiprows=1)
ai_df.rename(columns={'Digitial Infrastructure': 'Digital Infrastructure'}, inplace=True) # Rename mispelt column
print(ai_df.columns)
print(ai_df.head())