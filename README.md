
This project reads two JSON files taken from Kaggle's NobelPrize Dataset at 
https://www.kaggle.com/datasets/imdevskp/nobel-prize?select=complete.csv .

JSONS are read and converted to Pandas dataframes ready for manipulation.

Dataframes are cleaned and manipulated and then CSV files are created 
ready to populate a locally hosted postgreSQL database for analysis


To run:
    create venv
    export python path
    install dependencies
    run psql setup_db to create raw and clean postgres databases

