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
