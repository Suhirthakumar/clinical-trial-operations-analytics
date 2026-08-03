import pandas as pd
import numpy as np
from faker import Faker
import random
import os


fake = Faker()

np.random.seed(42)
random.seed(42)


DATA_PATH = "data"


os.makedirs(DATA_PATH, exist_ok=True)


# -----------------------------
# Clinical Trials
# -----------------------------

trials = []

therapeutic_areas = [
    "Oncology",
    "Cardiology",
    "Neurology",
    "Diabetes",
    "Respiratory"
]


phases = [
    "Phase I",
    "Phase II",
    "Phase III",
    "Phase IV"
]


statuses = [
    "Active",
    "Completed",
    "Recruiting"
]


for i in range(20):

    trials.append({

        "trial_id": f"TR{i+1:03}",
        "phase": random.choice(phases),
        "therapeutic_area": random.choice(therapeutic_areas),
        "status": random.choice(statuses)

    })


clinical_trials = pd.DataFrame(trials)

clinical_trials.to_csv(
    f"{DATA_PATH}/clinical_trials.csv",
    index=False
)


# -----------------------------
# Sites
# -----------------------------


countries = [
    "UK",
    "USA",
    "Germany",
    "Canada",
    "Australia"
]


sites=[]


for i in range(30):

    sites.append({

        "site_id":f"S{i+1:03}",
        "country":random.choice(countries),
        "recruitment_target":random.randint(50,300)

    })


sites_df=pd.DataFrame(sites)

sites_df.to_csv(
    f"{DATA_PATH}/sites.csv",
    index=False
)


# -----------------------------
# Patients
# -----------------------------


patients=[]


for i in range(500):

    patients.append({

        "patient_id":f"P{i+1:05}",
        "trial_id":random.choice(clinical_trials.trial_id),
        "site_id":random.choice(sites_df.site_id),
        "age":random.randint(18,80),
        "gender":random.choice(
            ["Male","Female"]
        ),
        "enrollment_date":
        fake.date_between(
            start_date="-2y",
            end_date="today"
        )

    })


patients_df=pd.DataFrame(patients)


patients_df.to_csv(
    f"{DATA_PATH}/patients.csv",
    index=False
)



# -----------------------------
# Adverse Events
# -----------------------------


events=[]


severity=[
    "Mild",
    "Moderate",
    "Severe",
    "Serious"
]


event_types=[
    "Infection",
    "Headache",
    "Nausea",
    "Fatigue",
    "Allergic Reaction"
]


for i in range(300):

    events.append({

        "event_id":f"AE{i+1:05}",
        "patient_id":
        random.choice(
            patients_df.patient_id
        ),
        "event_type":
        random.choice(event_types),

        "severity":
        random.choice(severity)

    })


events_df=pd.DataFrame(events)


events_df.to_csv(
    f"{DATA_PATH}/adverse_events.csv",
    index=False
)



print("Clinical trial data generated successfully")