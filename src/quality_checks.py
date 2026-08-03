import pandas as pd


files=[
"data/clinical_trials.csv",
"data/patients.csv",
"data/adverse_events.csv",
"data/sites.csv"
]


for file in files:

    df=pd.read_csv(file)

    print("\nDataset:",file)

    print(
        "Rows:",
        len(df)
    )

    print(
        "Missing values:"
    )

    print(
        df.isnull().sum()
    )