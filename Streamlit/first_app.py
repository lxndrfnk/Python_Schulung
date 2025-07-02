import streamlit as st
 
# st.title("Meine erste App")


# st.write("Hallo Welt!")
# st.text("""Ich 
# bin ein 
# mehrzeiliger Text!""")

# st.write("""Hallo
         
# Welt!""")

# st.subheader("Ich bin eine Unterüberschrift!")

# st.caption("Ich bin ein kleiner Untertext!")

# st.write("""
# Ich bin ein langer Absatz mit vielen Informationen. 

# Ich bin ein langer Absatz mit vielen Informationen.)

# ---

# """)

# st.metric(label = "Anzahl Teilnehmer", value = 7)

# st.metric(label = "Preis", value = 20, delta = -10)

# st.metric(label = "höchste Punktzahl", value = 95, delta = "Maximilian")

# st.video("https://www.youtube.com/watch?v=zxq60I5RSW8&pp=ygULa3VyeiBnZXNhZ3Q%3D")

# video_from_user = st.file_uploader("Lade ein Video hoch", type = ["mp4", "mov"])

# if video_from_user:
#     st.video(video_from_user)

# col1, col2, col3 = st.columns(3, border = True)

# with col1:
#     st.metric("Anzahl Schüler", value = 7)

# with col2:
#     st.write("""* Alexander
# * Ornela
# * Rafael""")

# with col3:
#     st.write("Hallo Alexander!")

# tab1, tab2 = st.tabs(["Eins", "ZWEI"])

# with tab1:
#     st.write("Ich bin heute ganz schön müde")

# with tab2:
#     st.write("TestTestTestTestTestTestTestTestTestTest")

# with st.sidebar:
#     st.header("HalliHallo")
#     st.text("hiewhgirhgirhgpirhgiprhgipwrhgpirhhioehzioehziezieziotehithi" \
# "hirhiohierhziehiehziperhzierhzizhibghihipäetzipezhei")

# -------------------- Aufgabe 2.2 --------------------

st.header("Dashboard: Kennzahlen 2024")

st.subheader("Finanzen")
st.metric("Umsatz", value = "2,5 Mio. €", delta = "4 %" )

st.subheader("Kunden")
st.metric("Kundenanzahl", value = "8.420", delta = "120" )

st.subheader("Mitarbeitende")
st.metric("Zufriedenheit", value = "87 %", delta = "-2 %" )

st.write("**Stand:** April 2024")