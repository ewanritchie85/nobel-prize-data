import pytest
import pandas as pd
from utils.extract_utils import create_df_from_json
from utils.transform_utils import (
    create_prizes_csv,
    create_laureates_csv,
    create_categories_csv,
)
from db.seed import seed_db
from pprint import pprint

pd.set_option("display.max_columns", None)


class TestExtractUtils:
    def test_func_returns_correct_dtypes(TestExtractUtils, prizes_path, laureates_path):

        data = create_df_from_json(prizes_path)
        assert isinstance(data, tuple)
        assert isinstance(data[0], pd.DataFrame)
        assert isinstance(data[1], str)

        data_2 = create_df_from_json(laureates_path)
        assert isinstance(data, tuple)
        assert isinstance(data[0], pd.DataFrame)
        assert isinstance(data[1], str)

    def test_returns_error_for_bad_path(TestExtractUtils, bad_path):
        with pytest.raises(
            FileNotFoundError, match=f"Error: File not found at path {bad_path}"
        ):
            create_df_from_json(bad_path)


class TestTransformUtils:

    def test_create_prizes_reads_df(TestTransformUtils, prizes_data):
        data = create_prizes_csv(prizes_data)
        assert isinstance(data, str)

    def test_creat_categories_reads_df(TestTransformUtils, prizes_data):
        data = create_categories_csv(prizes_data)
        assert isinstance(data, str)

    def test_clean_laureates_reads_df(TestTransformUtils, laureates_data):
        data = create_laureates_csv(laureates_data)
        assert isinstance(data, str)


class TestDatabases:

    def test_func_creates_db_tables(TestDatabases, prizes_data, laureates_data):
        # seed_raw_db(prizes_data)
        # seed_raw_db(laureates_data)
        pass
