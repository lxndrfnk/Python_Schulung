import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://i.ebayimg.com/images/g/TCAAAOSwo1Bk4LDf/s-l400.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Die dunkle Bedrohung""")
    st.caption("1999 | 136 Minuten | FSK 6")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.disneyplus.com/de-de/browse/entity-e0a9fee4-2959-4077-ad8c-8fab4fd6e4d1" target="_blank">
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

st.write("Star Wars: Episode I – Die dunkle Bedrohung (Originaltitel Star Wars: Episode I – The Phantom Menace) ist ein US-amerikanischer Science-Fiction-Film aus dem Jahr 1999 und der erste Teil der Prequel-Trilogie, welche die Vorgeschichte der Star-Wars-Filme (1977–1983) erzählt. Die weiteren Filme sind Star Wars: Episode II – Angriff der Klonkrieger (2002) und Star Wars: Episode III – Die Rache der Sith (2005). Der Film startete am 19. August 1999 in den deutschen Kinos. Im Jahr 2012 erschien er in 3D konvertiert erneut weltweit in den Kinos.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "6.5/10")
        st.metric(label = "Moviepilot", value = "6.7/10")
        st.metric(label = "Filmstarts", value = "3.4/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Star_Wars:_Episode_I_-_Die_dunkle_Bedrohung)  
        * [iMDb](https://www.imdb.com/de/title/tt0120915/)
        """)

tab1, tab2, tab3 = st.tabs(["Stab", "Besetzung", "Chronologie"])


with tab1:
    st.markdown("""
- **Regie**: George Lucas  
- **Drehbuch**: George Lucas
- **Produktion**: Rick McCallum
- **Musik**: John Williams
- **Kamera**: David Tattersall
- **Schnitt**: Ben Burtt, Paul Martin Smith
""")

with tab2:
    st.markdown("""
- **Liam Neeson:**: Qui-Gon Jinn
- **Ewan McGregor**: Obi-Wan Kenobi
- **Natalie Portman**: Königin Padmé Amidala
- **Jake Lloyd**: Anakin Skywalker
- **Pernilla August**: Shmi Skywalker
- **Frank Oz**: Yoda
- **Ian McDiarmid**: Senator Sheev Palpatine/Darth Sidious
- **Ray Park**: Darth Maul
""")

with tab3:
   st.markdown("""
<ul>
    <li><span style='color:gold;'><strong>Episode I</strong>: Die dunkle Bedrohung</span></li>
    <li><strong>Episode II</strong>: Angriff der Klonkrieger</span></li>
    <li><strong>Episode III</strong>: Die Rache der Sith</span></li>
    <li><strong>Episode IV</strong>: Krieg der Sterne</span></li>
    <li><strong>Episode V</strong>: Das Imperium schlägt zurück</span></li>
    <li><strong>Episode VI</strong>: Die Rückkehr der Jedi-Ritter</span></li>
    <li><strong>Episode VII</strong>: Das Erwachen der Macht</span></li>
    <li><strong>Episode VIII</strong>: Die letzten Jedi</span></li>
    <li><strong>Episode IX</strong>: Der Aufstieg Skywalkers</span></li>
</ul>
""", unsafe_allow_html=True)
   
st.markdown("---")
   
with st.expander("Oscarverleihung 2000"):
    st.markdown("""
- Nominierung in der Kategorie bester Ton  
- Nominierung in der Kategorie bester Tonschnitt 
- Nominierung in der Kategorie beste Spezialeffekte
""")