import sqlite3
import pandas as pd
import os


DATABASE="database/clinical_trial.db"


conn=sqlite3.connect(DATABASE)


tables=[
    "clinical_trials",
    "patients",
    "sites",
    "adverse_events"
]


for table in tables:

    df=pd.read_csv(
        f"data/{table}.csv"
    )


    df.to_sql(
        table,
        conn,
        if_exists="replace",
        index=False
    )


conn.close()


print(
"SQLite database created successfully"
)