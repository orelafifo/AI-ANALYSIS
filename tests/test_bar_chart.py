import pytest
import matplotlib.pyplot as plt
import pandas as pd

def plot_stacked_bar(grouped_data):
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped_data.plot(kind='bar', stacked=True, ax=ax, colormap='viridis')

    # Add data labels inside bars
    for container in ax.containers:
        for bar in container:
            height = bar.get_height()
            if height > 0:
                x = bar.get_x() + bar.get_width() / 2
                y = bar.get_y() + height / 2
                label = f"{height:.2f}"
                ax.text(x, y, label, ha='center', va='center', fontsize=10, color='white')

    # Add title and labels
    plt.title('Average AIPI Indicator Scores by Economic Status of Countries', fontsize=12)
    plt.xlabel('Economic Status of Countries', fontsize=10)
    plt.ylabel('Average Index Score', fontsize=10)

    # Legend positioning
    plt.legend(title='AIPI Indicators', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    return fig, ax

def test_stacked_bar_chart():
    file_path = 'data/aipidata.xlsx'
    ai_df = pd.read_excel(file_path, skiprows=1)
    ai_df.rename(columns={'Digitial Infrastructure': 'Digital Infrastructure'}, inplace=True)
    
    # Group data
    economic_status = ['AE', 'EM', 'LIC']
    indicators = ['Digital Infrastructure', 'Innovation and Economic Integration', 
                  'Human Capital and Labor Market Policies', 'Regulation and Ethics']
    grouped_data = ai_df.groupby('type')[indicators].mean().loc[economic_status]
    
    # Call the plot function
    fig, ax = plot_stacked_bar(grouped_data)

    # Check if the figure was created
    assert fig is not None, "Graph was not generated"
    
    # Check if the figure has at least one container (i.e. data is plotted)
    assert len(ax.containers) > 0, "No containers in the plot, data was not plotted"

    # Check that the graph contains at least one non-zero bar
    bar_heights = [bar.get_height() for container in ax.containers for bar in container]
    assert any(height > 0 for height in bar_heights), "Graph contains no non-zero bars"



