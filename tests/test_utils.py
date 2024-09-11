import pytest
import pandas as pd
from utils.extract_utils import create_df_from_json
from utils.transform_utils import get_df_details
from db.seed import seed_raw_db
from pprint import pprint

pd.set_option('display.max_columns', None)


class TestExtractUtils:
    def test_func_returns_correct_dtypes(TestExtractUtils, path_1, path_2, path_3):
        data_1 = create_df_from_json(path_1)
        pprint(data_1[1])
        pprint(data_1[2])
        pprint(data_1[0].head())
        assert isinstance(data_1, tuple)
        assert isinstance(data_1[0], pd.DataFrame)
        assert isinstance(data_1[1], str)
        assert isinstance(data_1[2], list)
        
        data_2 = create_df_from_json(path_2)
        # pprint(data_2[1])
        # pprint(data_2[2])
        # pprint(data_2[0].head())
        assert isinstance(data_2, tuple)
        assert isinstance(data_2[0], pd.DataFrame)
        assert isinstance(data_2[1], str)
        assert isinstance(data_2[2], list)

        data_3 = create_df_from_json(path_3)
        # pprint(data_3[1])
        # pprint(data_3[2])
        # pprint(data_3[0].head())
        assert isinstance(data_3, tuple)
        assert isinstance(data_3[0], pd.DataFrame)
        assert isinstance(data_3[1], str)
        assert isinstance(data_3[2], list)
        
class TestTransformUtils:

    def test_func_reads_df(TestTransformUtils, data_1, data_2, data_3):
       pass
        
        
        
class TestDatabases:
    
    def test_func_creates_db_tables(TestDatabases, data_1, data_2, data_3):
        # seed_raw_db(data_1)
        # seed_raw_db(data_2)
        # seed_raw_db(data_3)
        pass