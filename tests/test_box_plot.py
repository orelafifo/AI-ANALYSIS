import pytest 
import pandas as pd
import matplotlib.pyplot as plt 

def test_boxplot():
    file_path = 'data/aipidata.xlsx'
    ai_df = pd.read_excel(file_path, skiprows=1)
    
    # Create the boxplot
    fig = plt.figure(figsize=(10, 6))
    ai_df.boxplot(by='type', column=['AIPI'], grid=False, showmeans=False, patch_artist=True)
    plt.tight_layout()
    
    # Check if the plot was created
    assert fig is not None, "Boxplot was not created"
