import pandas as pd
from pprint import pprint


def create_prizes_csv(data: tuple) -> tuple:
    # function reads prizes.json
    # unpack 'data' tuple
    df, df_title = data[0], data[1]
    columns_to_drop = ["overallMotivation", "laureates"]
    df.drop(columns=columns_to_drop, inplace=True, errors="ignore")
    # creates prize_index column starting from 1 for the first date
    df["prize_id"] = pd.RangeIndex(start=len(df), stop=0, step=-1)
    # rename columns
    df.rename(
        columns={"year": "prize_year", "category": "prize_category"}, inplace=True
    )
    # reorder columns
    columns = ["prize_id", "prize_year", "prize_category"]
    df = df[columns]
    # write to local csv file
    prizes_path = f"data/clean_data/prizes.csv"
    df.to_csv(prizes_path, index=False)

    return prizes_path


def create_categories_csv(data: tuple):
    # function reads prizes.json
    # creating csv of unique prize categories
    df = data[0]
    df.rename(columns={"category": "prize_category"}, inplace=True)
    unique_categories = df["prize_category"].unique()
    cat_df = pd.DataFrame(unique_categories, columns=["prize_category"])
    cat_df["category_id"] = pd.RangeIndex(start=1, stop=len(cat_df) + 1)
    cat_columns = ["category_id", "prize_category"]
    cat_df = cat_df[cat_columns]
    categories_path = "data/clean_data/categories.csv"
    cat_df.to_csv(categories_path, index=False)
    return categories_path


def create_laureates_csv(data: tuple):
    # unpack 'data' tuple
    df, df_title = data[0], data[1]

    # merging nested 'prizes' data
    df = df.explode("prizes").reset_index(drop=True)
    prizes_expanded = pd.json_normalize(df["prizes"])
    df = df.drop(columns=["prizes"]).join(prizes_expanded)

    # merging nested 'affiliates' data
    df = df.explode("affiliations").reset_index(drop=True)
    df["affiliations"] = df["affiliations"].apply(
        lambda x: x if isinstance(x, dict) else {}
    )
    affiliations_expanded = pd.json_normalize(df["affiliations"])
    df = df.drop(columns=["affiliations"]).join(affiliations_expanded)

    # dropping unwanted columns
    columns_to_drop = ["motivation", "overallMotivation"]
    df.drop(columns=columns_to_drop, inplace=True, errors="ignore")

    # renaming columns
    df.rename(
        columns={
            "id": "laureate_id",
            "firstname": "first_name",
            "born": "date_of_birth",
            "died": "date_of_death",
            "bornCountry": "country_of_birth",
            "bornCountryCode": "country_of_birth_code",
            "bornCity": "city_of_birth",
            "diedCountry": "country_of_death",
            "diedCountryCode": "country_of_death_code",
            "diedCity": "city_of_death",
            "year": "year_of_prize_win",
            "category": "prize_category",
            "share": "share_of_prize",
            "name": "affiliated_university",
            "city": "city_of_university",
            "country": "country_of_university",
        },
        inplace=True,
    )

    # writing cleaned data to local csv file
    laureates_path = "data/clean_data/laureates.csv"
    df.to_csv(laureates_path, index=False)

    # # *** Make separate util for this ***
    # # creating csv of unique countries and codes
    # unique_countries = df['country_of_birth'].unique()
    # country = pd.DataFrame(unique_countries, columns=['country'])
    # country['country_id'] = pd.RangeIndex(start=1, stop=len(country)+1)
    # country_columns = ['country_id','country', 'country_code']
    # country = country[country_columns]
    # countries_path = 'data/clean_data/countries.csv'
    # country.to_csv(countries_path, index=False)
    return laureates_path
