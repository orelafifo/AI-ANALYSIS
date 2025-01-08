import pytest 
import pandas as pd 
import matplotlib.pyplot as plt 

def test_scatter_plots():
    file_path = 'data/aipidata.xlsx'
    ai_df = pd.read_excel(file_path, skiprows=1)

    # Rename columns
    ai_df.rename(columns={'Digitial Infrastructure': 'Digital Infrastructure'}, inplace=True)
    
    indicators = ['Digital Infrastructure', 'Innovation and Economic Integration', 
                  'Human Capital and Labor Market Policies', 'Regulation and Ethics']
    
    # Create scatter plots
    fig, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=150)
    for i, indicator in enumerate(indicators):
        row, col = divmod(i, 2)
        ax = axes[row, col]
        ax.scatter(ai_df[indicator], ai_df['AIPI'], alpha=0.7, edgecolors='k', color='pink')
        ax.set_title(f'AIPI vs. {indicator}', fontsize=11)
        ax.set_xlabel(indicator, fontsize=9)
        ax.set_ylabel('AI Preparedness Index (AIPI)', fontsize=9)
        ax.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.7)
    
    # Check if the figure was created
    assert fig is not None, "Scatter plot was not created"
