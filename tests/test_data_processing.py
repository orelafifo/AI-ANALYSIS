import pytest 
import pandas as pd

def test_group_data():
    file_path = 'data/aipidata.xlsx'
    ai_df = pd.read_excel(file_path, skiprows=1)
    ai_df.rename(columns={'Digitial Infrastructure': 'Digital Infrastructure'}, inplace=True)
    
    # Group data by type (name of column)
    economic_status = ['AE', 'EM', 'LIC']
    grouped_data = ai_df.groupby('type')[['Digital Infrastructure', 'Innovation and Economic Integration', 
                                          'Human Capital and Labor Market Policies', 'Regulation and Ethics']].mean()
    
    # Test if the data is grouped by type
    assert 'type' in ai_df.columns, "Column 'type' should be present"
    
    # Filter for specified economic status
    grouped_data = grouped_data.loc[economic_status]
    
    # Test if the filtered grouped data contains only the specified economic statuses
    assert set(grouped_data.index) == set(economic_status), "The grouped data does not contain the expected economic statuses"
