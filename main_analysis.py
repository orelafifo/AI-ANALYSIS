import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'data/aipidata.xlsx'  # Path to the data folder
ai_df = pd.read_excel(file_path, skiprows=1)
ai_df.rename(columns={'Digitial Infrastructure': 'Digital Infrastructure'}, inplace=True) # Rename mispelt column
print(ai_df.columns)
print(ai_df.head())

# Group by economic status
economic_status = ['AE', 'EM', 'LIC']
grouped_data = ai_df.groupby('type')[['Digital Infrastructure', 'Innovation and Economic Integration', 
     'Human Capital and Labor Market Policies', 'Regulation and Ethics']].mean()

# Filter for specified economic status only
grouped_data = grouped_data.loc[economic_status]

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))
grouped_data.plot(kind='bar', stacked=True, ax=ax, colormap='viridis')

# Add data labels inside bars
for container in ax.containers: # Loop through the containers of the bars
    for bar in container:
        height = bar.get_height()
        if height > 0:  # Add label only if height is non-zero
            x = bar.get_x() + bar.get_width() / 2
            y = bar.get_y() + height / 2
            label = f"{height:.2f}"  # Data labels set to  2 decimal place

            ax.text(x, y, label, ha='center', va='center', fontsize=10, color='white')

# Add title and labels
plt.title('Average AIPI Indicator Scores by Economic Status of Countries', fontsize=12)
plt.xlabel('Economic Status of Countries', fontsize=10)
plt.ylabel('Average Index Score', fontsize=10)

# Position legend outside graph
plt.legend(title='AIPI Indicators', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout for better fit
plt.tight_layout()

plt.savefig('aipi_stacked_bar_chart.png')
plt.show()

# Create the boxplot 
plt.figure(figsize=(10, 6))
ai_df.boxplot(by='type', column=['AIPI'], grid=False, showmeans=False, patch_artist=True)

# Add faint dotted lines
plt.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.5)

plt.title('Distribution of AI preparedness Index (AIPI) Scores by Economic Status', fontsize=12)
plt.suptitle('')  # Remove default Pandas boxplot title
plt.xlabel('Economic Status of Countries', fontsize=10)
plt.ylabel('AI Preparedness Index (AIPI)', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Save and display the plot
plt.tight_layout()
plt.savefig('aipi_boxplot.png', bbox_inches='tight', pad_inches=0.5)
plt.show()

# Prepare the data
economic_status = ['AE', 'EM', 'LIC']
indicators = ['Digital Infrastructure', 'Innovation and Economic Integration', 'Human Capital and Labor Market Policies', 'Regulation and Ethics']

# Filter data by economic status and get mean values of the 4 indicators
grouped_data = ai_df.groupby('type')[indicators].mean().loc[economic_status]

# Prepare Radar Chart
# Define the number of variables (indicators)
num_vars = len(indicators)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Close the circle making sure to repeat the first value
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), dpi=150, subplot_kw=dict(polar=True))

# Plot each economic group
for status in economic_status:
    values = grouped_data.loc[status].tolist()
    values += values[:1]  # Close the circle
    ax.plot(angles, values, label=status, linewidth=2, linestyle='solid')
    ax.fill(angles, values, alpha=0.25)  # Fill area under the line


# Set the labels for each axis
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(indicators, fontsize=12)


# Set the title and legend
ax.set_title('Average AI Preparedness Across Economic Status by Indicator', fontsize=14, color='black', fontweight='bold', pad=30)
plt.legend(title='Economic Status', loc='upper right', bbox_to_anchor=(1.2, 1))

# Show the plot
plt.tight_layout()
plt.savefig('aipi_radar_chart.png', bbox_inches='tight')
plt.show()

# Define the indicators 
indicators = ['Digital Infrastructure', 'Innovation and Economic Integration', 
              'Human Capital and Labor Market Policies', 'Regulation and Ethics']

# Create a scatter plot for each indicator
fig, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=150)  # Arrangement 

# Map index to the correct subplot
for i, indicator in enumerate(indicators):
    row, col = divmod(i, 2)  
    ax = axes[row, col]
    
    # Scatter plot
    ax.scatter(ai_df[indicator], ai_df['AIPI'], alpha=0.7, edgecolors='k', color='pink')
    
    # Add titles, labels, and grid
    ax.set_title(f'AIPI vs. {indicator}', fontsize=11, pad=15)
    ax.set_xlabel(indicator, fontsize=9, labelpad=10)
    ax.set_ylabel('AI Preparedness Index (AIPI)', fontsize=9, labelpad=10)
    ax.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.7)

# Adjust layout 
plt.tight_layout(pad=3.0) 


# Save and show the plot
plt.savefig('aipi_scatter_plots_adjusted.png', bbox_inches='tight', pad_inches=0.5)
plt.show()

