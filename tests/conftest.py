import pytest
from utils.extract_utils import create_df_from_json


@pytest.fixture
def prizes_path():
    return "data/raw_data/prizes.json"


@pytest.fixture
def laureates_path():
    return "data/raw_data/laureates.json"


@pytest.fixture
def bad_path():
    return "data/raw_data/missing.json"


@pytest.fixture
def prizes_data(prizes_path):
    return create_df_from_json(prizes_path)


@pytest.fixture
def laureates_data(laureates_path):
    return create_df_from_json(laureates_path)
