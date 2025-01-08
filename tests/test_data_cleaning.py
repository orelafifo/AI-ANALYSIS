import pytest
import pandas as pd

def test_data_loading():
    # Load data 
    file_path = 'data/aipidata.xlsx'
    ai_df = pd.read_excel(file_path, skiprows=1)

    # Check that the Dataframe is not empty
    assert not ai_df.empty, "The dataframe is empty!"

    # Re-name mispelt column
    ai_df.rename(columns={'Digitial Infrastructure': 'Digital Infrastructure'}, inplace=True)

    # Check that the Dataframe contains the expected columns
    expected_columns = ['Country', 'iso3', 'type', 'AIPI', 'Digital Infrastructure',
                         'Innovation and Economic Integration', 'Human Capital and Labor Market Policies', 'Regulation and Ethics']  
    for column in expected_columns:
        assert column in ai_df.columns, f"Column {column} is missing!"



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

   


