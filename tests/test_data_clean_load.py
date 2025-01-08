import pytest
import pandas as pd

def test_load_data():
    file_path = 'data/aipidata.xlsx'
    ai_df = pd.read_excel(file_path, skiprows=1)
    
    # Test if the data is loaded correctly
    assert ai_df is not None, "Data should be loaded successfully"
    assert not ai_df.empty, "Dataframe should not be empty"

def test_column_data_types():
    file_path = 'data/aipidata.xlsx'
    ai_df = pd.read_excel(file_path, skiprows=1)
    
    # Rename columns
    ai_df.rename(columns={'Digitial Infrastructure': 'Digital Infrastructure'}, inplace=True)
    
    # Check column data types for columns used
    expected_types = {
        'Country': 'object',
        'AIPI': 'float64',
        'type': 'object',
        'Digital Infrastructure': 'float64',
        'Innovation and Economic Integration': 'float64',
        'Human Capital and Labor Market Policies': 'float64',
        'Regulation and Ethics': 'float64'
    }

    for column, expected_type in expected_types.items():
        assert ai_df[column].dtype == expected_type, f"Column {column} does not have the expected type {expected_type}"



def test_handle_missing_data():
    # Load data
    ai_df = pd.read_excel('data/aipidata.xlsx', skiprows=1)

    # Makes sure missing values are shown and not filled or droped
    assert ai_df.isnull().sum().sum() > 0, "The dataset should have missing values!"

    # Loop through all columns
    for column in ai_df.columns:
        if pd.api.types.is_numeric_dtype(ai_df[column]): # Only numeric data considered
            column_mean = ai_df[column].mean()  # Calculate mean ignoring NaN
            column_median = ai_df[column].median()  # Calculate median ignoring NaN
            print(f"Mean of {column}: {column_mean}")
            print(f"Median of {column}: {column_median}")

            # Ensure that the mean and median are valid numbers
            assert isinstance(column_mean, (float, int)), f"Invalid mean value for column {column}: {column_mean}"
            assert isinstance(column_median, (float, int)), f"Invalid median value for column {column}: {column_median}"
        else:
            print(f"Skipping non-numeric column: {column}")

   

