import unittest
import pandas as pd
import os

class TestDataViz(unittest.TestCase):
    def setUp(self):
        self.file_path = "data/sales_dashboard_data.csv"
        
    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.file_path), "File dataset sales_dashboard_data.csv tidak ditemukan!")
        
    def test_data_aggregation(self):
        if os.path.exists(self.file_path):
            df = pd.read_csv(self.file_path)
            self.assertIn('total_sales', df.columns, "Kolom total_sales harus ada pada dataset!")
            self.assertGreater(df['total_sales'].sum(), 0, "Total penjualan harus bernilai positif!")

if __name__ == '__main__':
    unittest.main()
