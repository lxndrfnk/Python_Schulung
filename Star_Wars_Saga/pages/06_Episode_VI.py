import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://m.media-amazon.com/images/I/A10W5g12x6L._UF1000,1000_QL80_.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)


with col2:
    st.header("""Star Wars - Die dunkle Bedrohung""")
    st.caption("1999 | 136 Minuten | FSK 6 | Lucasfilm Ltd. | 20th Century-Fox")
    st.markdown("""
    <div style="text-align: center;">
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
    
st.write("Star Wars: Episode I – Die dunkle Bedrohung (Originaltitel Star Wars: Episode I – The Phantom Menace) ist ein US-amerikanischer Science-Fiction-Film aus dem Jahr 1999 und der erste Teil der Prequel-Trilogie, welche die Vorgeschichte der Star-Wars-Filme (1977–1983) erzählt. Die weiteren Filme sind Star Wars: Episode II – Angriff der Klonkrieger (2002) und Star Wars: Episode III – Die Rache der Sith (2005). Der Film startete am 19. August 1999 in den deutschen Kinos. Im Jahr 2012 erschien er in 3D konvertiert erneut weltweit in den Kinos.")
            

with st.sidebar:
        st.header("📈 Statistik")
        st.metric(label = "iMDb-Rating", value = "6.5/10")
        st.metric(label = "Moviepilot", value = "6.7/10")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Star_Wars:_Episode_I_-_Die_dunkle_Bedrohung)  
        * [iMDb](https://www.imdb.com/de/title/tt0080684/)
        """)

tab1, tab2, tab3 = st.tabs(["Stab", "Besetzung", "Chronologie"])


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
    <li><strong>Episode I</strong>: <span style='color:orange;'>Die dunkle Bedrohung</span></li>
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
   
with st.expander("Auszeichnungen (Auszug)"):
    st.markdown("""
- 🏆 **Oscar 1981**: Bester Ton  
- ✨ **Sonderoscar 1981**: Beste visuelle Effekte  
- 🎶 **Golden Globe 1981**: Beste Filmmusik
""")