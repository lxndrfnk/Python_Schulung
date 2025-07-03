import streamlit as st
import pandas as pd
import plotly.express as px

# Daten laden
df = pd.read_csv("Woche_7/teams.csv")

st.title("NHL Teams")

# Auswahl: Teams (mehrere auswählbar, nichts vorausgewählt)
alle_teams = df["Team"].sort_values().unique()
ausgewaehlte_teams = st.multiselect(
    "Welche Teams möchtest du sehen?",
    options=alle_teams
    # keine default-Auswahl
)

# Auswahl: Jahrbereich
min_jahr = int(df["Jahr"].min())
max_jahr = int(df["Jahr"].max())
jahr_start, jahr_ende = st.slider(
    "Welche Jahre möchtest du betrachten?",
    min_value=min_jahr,
    max_value=max_jahr,
    value=(min_jahr, max_jahr),
    step=1
)

# Filter anwenden
df_gefiltert = df.copy()

# Jahresfilter immer anwenden
df_gefiltert = df_gefiltert[
    (df_gefiltert["Jahr"] >= jahr_start) &
    (df_gefiltert["Jahr"] <= jahr_ende)
]

# Team-Filter: nur wenn etwas gewählt wurde
if ausgewaehlte_teams:
    df_gefiltert = df_gefiltert[df_gefiltert["Team"].isin(ausgewaehlte_teams)]

# Daten anzeigen
st.write(f"Angezeigte Daten ({len(df_gefiltert)} Einträge):")
st.dataframe(df_gefiltert)

# Zwischenüberschrift „Trendanalyse als Liniendiagramm“
st.header("Trendanalyse als Liniendiagramm")

# Metrik-Auswahl
metriken_mapping = {
    "Erzielte Tore (GF)": "GF",
    "Kassierte Tore (AF)": "AF",   # ggf. "AF" → "GA" prüfen
    "Siege": "Siege",
    "Niederlagen": "Niederlagen"
}

auswahl_text = st.selectbox("Welche Metrik möchtest du analysieren?", list(metriken_mapping.keys()))
ausgewaehlte_metrik = metriken_mapping[auswahl_text]

# Diagramm nur anzeigen, wenn mindestens ein Team gewählt wurde
if ausgewaehlte_teams:
    if not df_gefiltert.empty:
        fig = px.line(
            df_gefiltert,
            x="Jahr",
            y=ausgewaehlte_metrik,
            color="Team",
            markers=True,
            title=f"Entwicklung: {auswahl_text} pro Saison"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Keine Daten für die gewählte Kombination aus Team(s) und Zeitraum.")
else:
    st.info("Bitte wähle mindestens ein Team aus, um die Trendanalyse zu starten.")

import streamlit as st
import os

st.write("📂 Aktuelles Verzeichnis:", os.getcwd())
st.write("📄 Dateien im Verzeichnis:", os.listdir())

