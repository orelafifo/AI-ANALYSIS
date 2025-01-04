import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'data/aipidata.xlsx'  # Relative path to the data folder
ai_df = pd.read_excel(file_path, skiprows=1)
print(ai_df.head())
print(ai_df.columns)