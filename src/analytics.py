import sqlite3
import pandas as pd


DATABASE="database/clinical_trial.db"



def get_connection():

    return sqlite3.connect(
        DATABASE
    )



def recruitment_summary():

    conn=get_connection()


    query="""

    SELECT
    site_id,
    COUNT(patient_id) AS enrolled_patients

    FROM patients

    GROUP BY site_id

    """


    df=pd.read_sql(
        query,
        conn
    )

    conn.close()

    return df




def adverse_event_summary():

    conn=get_connection()


    query="""

    SELECT
    severity,
    COUNT(event_id) AS total_events

    FROM adverse_events

    GROUP BY severity

    """


    df=pd.read_sql(
        query,
        conn
    )


    conn.close()


    return df




def trial_summary():

    conn=get_connection()


    df=pd.read_sql(

    """
    SELECT *
    FROM clinical_trials

    """,

    conn)


    conn.close()

    return df