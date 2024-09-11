import pytest
from utils.extract_utils import create_df_from_json

@pytest.fixture
def path_1():
    return "data/raw_data/prizes.json"

@pytest.fixture
def path_2():
    return "data/raw_data/laureates.json"

@pytest.fixture
def path_3():
    return "data/raw_data/countries.json"

@pytest.fixture
def data_1(path_1):
    return create_df_from_json(path_1)

@pytest.fixture
def data_2(path_2):
    return create_df_from_json(path_2)

@pytest.fixture
def data_3(path_3):
    return create_df_from_json(path_3)