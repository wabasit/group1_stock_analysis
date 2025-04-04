import unittest
import pandas as pd
import stock_data_analysis import data_cleaning, pipeline

class TestDataProcessingFunctions(unittest.TestCase):
    def test_clean_data(self):
        data = pd.DataFrame({
            'Stock': ['AAPL', 'AAT', 'AAPL', 'ABB'],
            'Closing_Price': [200, 500, None, 300]
        })
        cleaned_data = data_cleaning(data)
        self.assertFalse(cleaned_data.isnull().values.any(), 'NaN values exist')
        self.assertEqual(len(cleaned_data), 2, 'Duplicates exist')

if __name__=='__main__':
    unittest.main()