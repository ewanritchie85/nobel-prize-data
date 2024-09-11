import pandas as pd
import json
from pprint import pprint


def create_df_from_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        df_title = list(data.keys())[0]
        # normalize will flatten nested jsons
        df = pd.json_normalize(data[df_title])
        df_columns = df.columns.tolist()
        
                
        
        return df, df_title, df_columns
    except FileNotFoundError:
        print(f"Error: File not found at path {path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {path}")
    except Exception as e:
        print(f"An error occurred: {e}")


