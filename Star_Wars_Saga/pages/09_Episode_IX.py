import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://de.web.img2.acsta.net/pictures/19/10/24/12/11/0789324.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Der Aufstieg Skywalkers""")
    st.caption("2019 | 142 Minuten | FSK 12")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.disneyplus.com/de-de/browse/entity-43f9c275-e7e8-4ab3-802d-00d06a8ad841" target="_blank">
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

st.write("Star Wars: Der Aufstieg Skywalkers (Originaltitel Star Wars: The Rise of Skywalker) ist die neunte Episode der Star-Wars-Filmreihe und der dritte und letzte Teil der Sequel-Trilogie, die mit Star Wars: Das Erwachen der Macht (2015) und Star Wars: Die letzten Jedi (2017) ihren Anfang nahm. Die Handlung spielt mehr als 30 Jahre nach der sechsten Episode Die Rückkehr der Jedi-Ritter (1983). Die Regie übernahm J. J. Abrams, der zusammen mit Chris Terrio auch das Drehbuch schrieb. Abrams nahm beide Funktionen bereits in Das Erwachen der Macht ein. Produziert wurde der Film von Kathleen Kennedy, Michelle Rejwan und J. J. Abrams.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "6.4/10")
        st.metric(label = "Moviepilot", value = "6.1/10")
        st.metric(label = "Filmstarts", value = "3.4/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Star_Wars:_Der_Aufstieg_Skywalkers)  
        * [iMDb](https://www.imdb.com/de/title/tt2527338/)
        """)

tab1, tab2, tab3, tab4 = st.tabs(["Stab", "Besetzung", "Chronologie", "Einspielergebnis"])


with tab1:
    st.markdown("""
- **Regie**: J. J. Abrams
- **Drehbuch**: J. J. Abrams, Chris Terrio
- **Produktion**: Kathleen Kennedy, J. J. Abrams, Michelle Rejwan
- **Musik**: John Williams
- **Kamera**: Dan Mindel
- **Schnitt**: Maryann Brandon, Stefan Grube
""")

with tab2:
    st.markdown("""
- **Daisy Ridley**: Rey Skywalker/Rey Palpatine
- **John Boyega**: Finn
- **Oscar Isaac**: Poe Dameron
- **Adam Driver**: Kylo Ren/Ben Solo
- **Carrie Fisher**: General Leia Organa
- **Ian McDiarmid**: Imperator Palpatine/Darth Sidious
- **Billy Dee Williams**: Lando Calrissian
- **Richard E. Grant**: Allegiant General Pryde
""")

with tab3:
   st.markdown("""
<ul>
    <li><strong>Episode I</strong>: Die dunkle Bedrohung</span></li>
    <li><strong>Episode II</strong>: Angriff der Klonkrieger</span></li>
    <li><strong>Episode III</strong>: Die Rache der Sith</span></li>
    <li><strong>Episode IV</strong>: Krieg der Sterne</span></li>
    <li><strong>Episode V</strong>: Das Imperium schlägt zurück</span></li>
    <li><strong>Episode VI</strong>: Die Rückkehr der Jedi-Ritter</span></li>
    <li><strong>Episode VII</strong>: Das Erwachen der Macht</span></li>
    <li><strong>Episode VIII</strong>: Die letzten Jedi</span></li>
    <li><span style='color:gold;'><strong>Episode IX</strong>: Der Aufstieg Skywalkers</span></li>
</ul>
""", unsafe_allow_html=True)

with tab4:
    st.markdown("""
1 Mrd. US-Dollar
""")
   
st.markdown("---")
   
with st.expander("Oscarverleihung 2020"):
    st.markdown("""
- Nominierung in der Kategorie beste visuelle Effekte
- Nominierung in der Kategorie beste Filmmusik
- Nominierung in der Kategorie bester Tonschnitt
""")