import streamlit as st
import pandas as pd
import plotly.express as px


# Page configuration
st.set_page_config(
    page_title="Clinical Trial Operations Analytics",
    layout="wide"
)


# Title
st.title(
    "Clinical Trial Operations Analytics Dashboard"
)


# Load data

trials = pd.read_csv(
    "data/clinical_trials.csv"
)


# Sidebar filters

st.sidebar.header(
    "Filters"
)


# Trial phase filter

selected_phase = st.sidebar.multiselect(
    "Select Trial Phase",
    options=sorted(
        trials["phase"].unique()
    ),
    default=sorted(
        trials["phase"].unique()
    )
)


# Filter dataset

filtered_trials = trials[
    trials["phase"].isin(selected_phase)
]


# Display metrics

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Trials",
        len(filtered_trials)
    )


with col2:

    st.metric(
        "Therapeutic Areas",
        filtered_trials["therapeutic_area"].nunique()
    )


with col3:

    delayed = (
        filtered_trials["status"]
        == "Delayed"
    ).sum()

    st.metric(
        "Delayed Trials",
        delayed
    )



# Trial status chart

st.subheader(
    "Trial Status Distribution"
)


status_count = (
    filtered_trials["status"]
    .value_counts()
    .reset_index()
)


status_count.columns = [
    "Status",
    "Count"
]


fig = px.bar(
    status_count,
    x="Status",
    y="Count",
    title="Clinical Trial Status"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# Phase distribution chart

st.subheader(
    "Trial Phase Distribution"
)


phase_count = (
    filtered_trials["phase"]
    .value_counts()
    .reset_index()
)


phase_count.columns = [
    "Phase",
    "Count"
]


fig2 = px.pie(
    phase_count,
    names="Phase",
    values="Count",
    title="Trials by Phase"
)


st.plotly_chart(
    fig2,
    use_container_width=True
)



# Data table

st.subheader(
    "Filtered Clinical Trials"
)


st.dataframe(
    filtered_trials,
    use_container_width=True
)