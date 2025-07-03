import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://de.web.img2.acsta.net/pictures/15/10/30/11/35/228722.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Das Erwachen der Macht""")
    st.caption("2015 | 136 Minuten | FSK 12")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.disneyplus.com/de-de/browse/entity-2854a94d-3702-40bd-97a4-12d55a809188" target="_blank">
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

st.write("Star Wars: Das Erwachen der Macht (Originaltitel Star Wars: The Force Awakens) ist ein US-amerikanischer Science-Fiction-Film und die siebte Episode der Star-Wars-Filmreihe. Die Regie übernahm J. J. Abrams, der gemeinsam mit Lawrance Kasdan und Michael Arndt auch das Drehbuch schrieb. Produziert wurde der Film von Kathleen Kennedy, J. J. Abrams und Bryan Burk. Der Film ist der Nachfolger von Die Rückkehr der Jedi-Ritter aus dem Jahr 1983, die Handlung ist knapp 30 Jahre nach den Ereignissen der sechsten Episode angesiedelt.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "7.8/10")
        st.metric(label = "Moviepilot", value = "7.2/10")
        st.metric(label = "Filmstarts", value = "4.1/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Star_Wars:_Das_Erwachen_der_Macht)  
        * [iMDb](https://www.imdb.com/de/title/tt2488496/)
        """)

tab1, tab2, tab3, tab4 = st.tabs(["Stab", "Besetzung", "Chronologie", "Einspielergebnis"])


with tab1:
    st.markdown("""
- **Regie**: J. J. Abrams
- **Drehbuch**: Lawrence Kasdan, J. J. Abrams, Michael Arndt
- **Produktion**: Kathleen Kennedy, J. J. Abrams, Bryan Burk
- **Musik**: John Williams
- **Kamera**: Dan Mindel
- **Schnitt**: 	Mary Jo Markey, Maryann Brandon
""")

with tab2:
    st.markdown("""
- **Daisy Ridley**: Rey
- **John Boyega**: Finn
- **Oscar Isaac**: Poe Dameron
- **Adam Driver**: Kylo Ren
- **Harrison Ford**: Han Solo
- **Carrie Fisher**: General Leia Organa
- **Mark Hamill**: Luke Skywalker
- **Domhnall Gleeson**: General Hux
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
    <li><span style='color:gold;'><strong>Episode VII</strong>: Das Erwachen der Macht</span></li>
    <li><strong>Episode VIII</strong>: Die letzten Jedi</span></li>
    <li><strong>Episode IX</strong>: Der Aufstieg Skywalkers</span></li>
</ul>
""", unsafe_allow_html=True)
   
with tab4:
    st.markdown("""
2.07 Mrd. US-Dollar
""")
   
st.markdown("---")
   
with st.expander("Oscarverleihung 2016"):
    st.markdown("""
- Nominierung in der Kategorie beste visuelle Effekte
- Nominierung in der Kategorie beste Filmmusik 
- Nominierung in der Kategorie bester Schnitt 
- Nominierung in der Kategorie bester Tonschnitt
- Nominierung in der Kategorie bester Ton 
""")