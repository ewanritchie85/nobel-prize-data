import pytest
import pandas as pd
from utils.extract_utils import create_df_from_json
from utils.transform_utils import create_prizes_csv, create_laureates_csv
from db.seed import seed_db
from pprint import pprint

pd.set_option('display.max_columns', None)


class TestExtractUtils:
    def test_func_returns_correct_dtypes(TestExtractUtils, path_1, path_2):
        data = create_df_from_json(path_1)
        # pprint(data[1])
        # pprint(data[0].head())
        assert isinstance(data, tuple)
        assert isinstance(data[0], pd.DataFrame)
        assert isinstance(data[1], str)
        
        data_2 = create_df_from_json(path_2)
        # pprint(data[1])
        # pprint(data[0].head())
        assert isinstance(data, tuple)
        assert isinstance(data[0], pd.DataFrame)
        assert isinstance(data[1], str)

        
class TestTransformUtils:

    def test_clean_prizes_reads_df(TestTransformUtils, data_1):
       data = create_prizes_csv(data_1)
       assert isinstance(data, tuple)
       
       
    def test_clean_laureates_reads_df(TestTransformUtils, data_2):
       data = create_laureates_csv(data_2)
       assert isinstance(data, str)
        
        
        
class TestDatabases:
    
    def test_func_creates_db_tables(TestDatabases, data_1, data_2):
        # seed_raw_db(data_1)
        # seed_raw_db(data_2)
        pass