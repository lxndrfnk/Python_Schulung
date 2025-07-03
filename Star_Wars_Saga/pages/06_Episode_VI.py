import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://m.media-amazon.com/images/M/MV5BNTczMmNlMWYtNzc5MC00NTRhLTgzNjEtOTVjOWE5ZDc2YjhiXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Die Rückkehr der Jedi-Ritter""")
    st.caption("1983 | 131 Minuten | FSK 12")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.disneyplus.com/de-de/browse/entity-4b6e7cda-daa5-4f2d-9b61-35bbe562c69c" target="_blank">
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

st.write("Die Rückkehr der Jedi-Ritter (Originaltitel Return of the Jedi) ist ein US-amerikanischer Space-Opera-Film aus dem Jahr 1983 und ist der dritte Spielfilm und die sechste Episode der Star-Wars-Saga von George Lucas, welche in Deutschland am 9. Dezember 1983 erschien und Das Imperium schlägt zurück fortsetzt. Alternativ ist der Film auch unter dem Titel Star Wars: Episode VI – Die Rückkehr der Jedi-Ritter bekannt.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "8.3/10")
        st.metric(label = "Moviepilot", value = "8.0/10")
        st.metric(label = "Filmstarts", value = "4.6/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Die_Rückkehr_der_Jedi-Ritter)  
        * [iMDb](https://www.imdb.com/de/title/tt0086190/)
        """)

tab1, tab2, tab3, tab4 = st.tabs(["Stab", "Besetzung", "Chronologie", "Einspielergebnis"])


with tab1:
    st.markdown("""
- **Regie**: Richard Marquand  
- **Drehbuch**: Lawrence Kasdan, George Lucas
- **Produktion**: Howard G. Kazanjian
- **Musik**: John Williams
- **Kamera**: Alan Hume
- **Schnitt**: Sean Barton, Marcia Lucas, Duwayne Dunham
""")

with tab2:
    st.markdown("""
- **Mark Hamill**: Luke Skywalker
- **Harrison Ford**: Han Solo
- **Carrie Fisher**: Prinzessin Leia Organa
- **Billy Dee Williams**: Lando Calrissian
- **Anthony Daniels**: C-3PO
- **David Prowse**: Darth Vader
- **Ian McDiarmid**: Imperator Palpatine
- **Kenny Baker**: R2-D2
- **Peter Mayhew**: Chewbacca
- **Alec Guinness**: Obi-Wan Kenobi
- **Frank Oz**: Yoda
""")

with tab3:
   st.markdown("""
<ul>
    <li><strong>Episode I</strong>: Die dunkle Bedrohung</span></li>
    <li><strong>Episode II</strong>: Angriff der Klonkrieger</span></li>
    <li><strong>Episode III</strong>: Die Rache der Sith</span></li>
    <li><strong>Episode IV</strong>: Krieg der Sterne</span></li>
    <li><strong>Episode V</strong>: Das Imperium schlägt zurück</span></li>
    <li><span style='color:gold;'><strong>Episode VI</strong>: Die Rückkehr der Jedi-Ritter</span></li>
    <li><strong>Episode VII</strong>: Das Erwachen der Macht</span></li>
    <li><strong>Episode VIII</strong>: Die letzten Jedi</span></li>
    <li><strong>Episode IX</strong>: Der Aufstieg Skywalkers</span></li>
</ul>
""", unsafe_allow_html=True)

with tab4:
    st.markdown("""
482 Mio. US-Dollar
""")
   
st.markdown("---")
   
with st.expander("Oscarverleihung 1984"):
    st.markdown("""
- Sonderoscar für die besten visuellen Effekte 
- Nominierung in der Kategorie bestes Szenenbild 
- Nominierung in der Kategorie beste Filmmusik 
- Nominierung in der Kategorie bester Ton
- Nominierung in der Kategorie bester Tonschnitt
""")