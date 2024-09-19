import pandas as pd
import json
from pprint import pprint


def create_df_from_json(path: str) -> tuple:
    try:
        with open(path, "r") as f:
            data = json.load(f)
        df_title = list(data.keys())[0]
        # normalize will flatten nested jsons
        df = pd.json_normalize(data[df_title])
        return df, df_title

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at path {path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Error: Invalid JSON format in file {path}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
