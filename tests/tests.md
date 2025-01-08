# Unit tests for AI Preparedness Index Analysis

## Introduction
This test suite describes the unit tests used to ensure to esure that the AI preparedness index analysis pipeline is correct. It goes through stages such as: data loading, data cleaning, data processing and the data visualisation process.

### 1. Data loading and cleaning
- **test_load_data**: Ensures data is loaded correctly from data/aipidata.xlsx 
- **column_data_types**: Validates that columns have the correct data type.
- **test_handle_missing_data**: Ensures that missing values are not fillled or dropped and ignored in statistical tests.

### 2. Data processing 
- **test_group_data**: Verifies that the 4 AIPI indicators are grouped bu the specified economic statuses only.

### 3. Plotting and visualisation
- **test_stacked_bar**: Checks if the stacked bar chart is plotted correctly with non-zero values.
- **test_box_plot**: Verifies that the box plot is generated with the AIPI as the dependent variable 
- **test_scatter_plot**: Verifies that the scatter plot is generated with the correct indicators.






