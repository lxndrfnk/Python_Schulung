import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://cdn.kinocheck.com/i/mdjlbw3ejo.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Krieg der Sterne""")
    st.caption("1977 | 121 Minuten | FSK 12")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.disneyplus.com/de-de/browse/entity-9a280e53-fcc0-4e17-a02c-b1f40913eb0b" target="_blank">
            <button style="
                background-color: gold;
                color: black;
                padding: 15px 30px;
                font-size: 18px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            ">
                🔗 Jetzt auf Disney + streamen
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("Krieg der Sterne (Originaltitel Star Wars) ist ein US-amerikanischer Space-Opera-Film des Drehbuchautors und Regisseurs George Lucas aus dem Jahr 1977. Er konnte bei der Oscar-Verleihung 1978 sechs Auszeichnungen erringen und zählt zu den finanziell erfolgreichsten Kinofilmen aller Zeiten. Krieg der Sterne begründete eines der umfangreichsten Franchises der Filmgeschichte und bildet die vierte von neun Episoden der Skywalker-Saga. Produziert wurde der Film von Gary Kurtz, in den Hauptrollen sind Mark Hamill, Carrie Fisher und Harrison Ford zu sehen.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "8.6/10")
        st.metric(label = "Moviepilot", value = "8.0/10")
        st.metric(label = "Filmstarts", value = "4.7/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Krieg_der_Sterne)  
        * [iMDb](https://www.imdb.com/de/title/tt0076759/)
        """)

tab1, tab2, tab3, tab4 = st.tabs(["Stab", "Besetzung", "Chronologie", "Einspielergebnis"])


with tab1:
    st.markdown("""
- **Regie**: George Lucas  
- **Drehbuch**: George Lucas
- **Produktion**: Gary Kurtz
- **Musik**: John Williams
- **Kamera**: Gilbert Taylor
- **Schnitt**: Paul Hirsch, Marcia Lucas, Richard Chew
""")

with tab2:
    st.markdown("""
- **Mark Hamill**: Luke Skywalker
- **Harrison Ford**: Han Solo
- **Carrie Fisher**: Prinzessin Leia Organa
- **Alec Guiness**: Obi-Wan „Ben“ Kenobi
- **David Prowse**: Darth Vader
- **Anthony Daniels**: C-3PO
- **Kenny Baker**: R2-D2
- **Peter Mayhew**: Chewbacca
""")

with tab3:
   st.markdown("""
<ul>
    <li><strong>Episode I</strong>: Die dunkle Bedrohung</span></li>
    <li><strong>Episode II</strong>: Angriff der Klonkrieger</span></li>
    <li><strong>Episode III</strong>: Die Rache der Sith</span></li>
    <li><span style='color:gold;'><strong>Episode IV</strong>: Krieg der Sterne</span></li>
    <li><strong>Episode V</strong>: Das Imperium schlägt zurück</span></li>
    <li><strong>Episode VI</strong>: Die Rückkehr der Jedi-Ritter</span></li>
    <li><strong>Episode VII</strong>: Das Erwachen der Macht</span></li>
    <li><strong>Episode VIII</strong>: Die letzten Jedi</span></li>
    <li><strong>Episode IX</strong>: Der Aufstieg Skywalkers</span></li>
</ul>
""", unsafe_allow_html=True)

with tab4:
    st.markdown("""
775 Mio. US-Dollar
""")
   
st.markdown("---")
   
with st.expander("Oscarverleihung 1978"):
    st.markdown("""
- Auszeichnung in der Kategorie bester Ton  
- Auszeichnung in der Kategorie bester Schnitt
- Auszeichnung in der Kategorie beste visuelle Effekte
- Auszeichnung in der Kategorie beste Filmmusik
- Auszeichnung in der Kategorie bestes Szenenbild
- Auszeichnung in der Kategorie bestes Kostümdesign
""")