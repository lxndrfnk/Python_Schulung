import streamlit as st
import pandas as pd

# Daten laden
df = pd.read_csv("dashboards/teams.csv")

st.title("NHL Teams")

# Sidebar: Team-Auswahl (mehrere auswählbar, aber zuerst leer)
alle_teams = df["Team"].sort_values().unique()
ausgewaehlte_teams = st.sidebar.multiselect(
    "Welche Teams möchtest du sehen?",
    options=alle_teams
    # keine default-Auswahl, damit alle angezeigt werden
)

# Sidebar: Jahrbereich
min_jahr = int(df["Jahr"].min())
max_jahr = int(df["Jahr"].max())

jahr_start, jahr_ende = st.sidebar.slider(
    "Welche Jahre möchtest du betrachten?",
    min_value=min_jahr,
    max_value=max_jahr,
    value=(min_jahr, max_jahr),
    step=1
)

# Filter anwenden – aber nur, wenn nötig
df_gefiltert = df.copy()

# Filter auf Jahre immer anwenden
df_gefiltert = df_gefiltert[
    (df_gefiltert["Jahr"] >= jahr_start) &
    (df_gefiltert["Jahr"] <= jahr_ende)
]

# Filter auf Teams nur anwenden, wenn welche ausgewählt sind
if ausgewaehlte_teams:
    df_gefiltert = df_gefiltert[df_gefiltert["Team"].isin(ausgewaehlte_teams)]

# Daten anzeigen
st.write(f"Angezeigte Daten ({len(df_gefiltert)} Einträge):")
st.dataframe(df_gefiltert)