import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://m.media-amazon.com/images/I/A10W5g12x6L._UF1000,1000_QL80_.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Das Imperium schlägt zurück""")
    st.caption("1980 | 124 Minuten | FSK 6")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.filmstarts.de/jump/#data-affiliation-type=svod&data-provider=disney&data-entity-type=Movie&data-entity-id=25802" target="_blank">
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

st.write("Das Imperium schlägt zurück (Originaltitel The Empire Strikes Back) ist ein US-amerikanischer Space-Opera-Film aus dem Jahr 1980 und der zweite Spielfilm sowie die fünfte Episode der Star-Wars-Saga, welche die Fortsetzung von Krieg der Sterne darstellt. Heutzutage ist der Film auch unter dem Titel Star Wars: Episode V – Das Imperium schlägt zurück bekannt. Die Kinopremiere in Deutschland fand am 11. Dezember 1980 statt.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "8.7/10")
        st.metric(label = "Moviepilot", value = "8.1/10")
        st.metric(label = "Filmstarts", value = "4.7/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Das_Imperium_schlägt_zurück)  
        * [iMDb](https://www.imdb.com/de/title/tt0080684/)
        """)

tab1, tab2, tab3, tab4 = st.tabs(["Stab", "Besetzung", "Chronologie", "Einspielergebnis"])


with tab1:
    st.markdown("""
- **Regie**: Irvin Kershner  
- **Drehbuch**: Leigh Brackett, Lawrence Kasdan
- **Produktion**: Gary Kurtz
- **Musik**: John Williams
- **Kamera**: Peter Suschitzky
- **Schnitt**: Paul Hirsch
""")

with tab2:
    st.markdown("""
- **Mark Hamill**: Luke Skywalker
- **Harrison Ford**: Han Solo
- **Carrie Fisher**: Prinzessin Leia Organa
- **David Prowse**: Darth Vader
- **Anthony Daniels**: C-3PO
- **Kenny Baker**: R2-D2
- **Peter Mayhew**: Chewbacca
- **Frank Oz**: Yoda
""")

with tab3:
   st.markdown("""
<ul>
    <li><strong>Episode I</strong>: Die dunkle Bedrohung</span></li>
    <li><strong>Episode II</strong>: Angriff der Klonkrieger</span></li>
    <li><strong>Episode III</strong>: Die Rache der Sith</span></li>
    <li><strong>Episode IV</strong>: Krieg der Sterne</span></li>
    <li><span style='color:gold;'><strong>Episode V</strong>: Das Imperium schlägt zurück</span></li>
    <li><strong>Episode VI</strong>: Die Rückkehr der Jedi-Ritter</span></li>
    <li><strong>Episode VII</strong>: Das Erwachen der Macht</span></li>
    <li><strong>Episode VIII</strong>: Die letzten Jedi</span></li>
    <li><strong>Episode IX</strong>: Der Aufstieg Skywalkers</span></li>
</ul>
""", unsafe_allow_html=True)

with tab4:
    st.markdown("""
549 Mio. US-Dollar
""")
   
st.markdown("---")
   
with st.expander("Oscarverleihung 1981"):
    st.markdown("""
- Auszeichnung in der Kategorie Bester Ton 
- Sonderoscar für die besten visuellen Effekte   
- Nominierung in der Kategorie Bestes Szenenbild 
- Nominierung in der Kategorie Beste Filmmusik 
""")