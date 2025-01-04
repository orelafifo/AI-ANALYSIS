import pytest
import pandas as pd

def test_data_loading():
    # Load data 
    file_path = 'data/aipidata.xlsx'
    ai_df = pd.read_excel(file_path, skiprows=1)

    # Check that the Dataframe is not empty
    assert not ai_df.empty, "The dataframe is empty!"

    # Check that the Dataframe contains the expected columns
    expected_columns = ['Country', 'iso3', 'type', 'AIPI', 'Digital Infrastructure',
                         'Innovation and Economic Integration', 'Human Capital and Labor Market Policies', 'Regulation and Ethics']  
    for column in expected_columns:
        assert column in ai_df.columns, f"Column {column} is missing!"



def test_handle_missing_data():
    # Load data
    ai_df = pd.read_excel('data/aipidata.xlsx', skiprows=1)

    # Ensures missing values (NaNs) are presented and not filled or droped
    assert ai_df.isnull().sum().sum() > 0, "The dataset should have missing values!"

    # Loop through all columns and calculate the mean and median, ignoring NaN values
    for column in ai_df.columns:
        column_mean = ai_df[column].mean()  # Calculate mean ignoring NaN
        column_median = ai_df[column].median()  # Calculate median ignoring NaN
        print(f"Mean of {column}: {column_mean}")
        print(f"Median of {column}: {column_median}")


        # Ensure that the mean and median are valid numbers (ignoring NaN values)
        assert isinstance(column_mean, (float, int)), f"Invalid mean value for column {column}: {column_mean}"
        assert isinstance(column_median, (float, int)), f"Invalid median value for column {column}: {column_median}"

   


