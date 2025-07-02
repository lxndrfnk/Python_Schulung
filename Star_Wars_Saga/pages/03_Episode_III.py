import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://m.media-amazon.com/images/I/71L94CPvDbL.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Die Rache der Sith""")
    st.caption("2005 | 140 Minuten | FSK 12")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.disneyplus.com/de-de/browse/entity-eb1e2c5f-69bf-4240-a61f-7ffc4e0311b3" target="_blank">
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

st.write("Star Wars: Episode III – Die Rache der Sith (Originaltitel Star Wars: Episode III – Revenge of the Sith) ist ein US-amerikanischer Science-Fiction-Film aus dem Jahr 2005 und der dritte Teil der Star-Wars-Saga. Regie führte George Lucas, die Hauptrollen sind mit Ewan McGregor, Natalie Portman, Hayden Christensen und Ian McDiarmid besetzt. Der Film kam am 19. Mai 2005 weltweit in die Kinos.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "7.6/10")
        st.metric(label = "Moviepilot", value = "7.3/10")
        st.metric(label = "Filmstarts", value = "4.1/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Star_Wars:_Episode_III_-_Die_Rache_der_Sith)  
        * [iMDb](https://www.imdb.com/de/title/tt0121766/)
        """)

tab1, tab2, tab3, tab4 = st.tabs(["Stab", "Besetzung", "Chronologie", "Einspielergebnis"])


with tab1:
    st.markdown("""
- **Regie**: George Lucas, Jonathan Hales  
- **Drehbuch**: George Lucas
- **Produktion**: Rick McCallum
- **Musik**: John Williams
- **Kamera**: David Tattersall
- **Schnitt**: Roger Barton, Ben Burtt
""")

with tab2:
    st.markdown("""
- **Hayden Christensen:**: Anakin Skywalker
- **Ewan McGregor**: Obi-Wan Kenobi
- **Ian McDiarmid**: Senator Sheev Palpatine/Darth Sidious
- **Samuel L. Jackson**: Mace Windu
- **Frank Oz**: Yoda
- **Natalie Portman**: Königin Padmé Amidala
- **Anthony Daniels**: C-3PO    
- **Kenny Baker**: R2-D2
""")

with tab3:
   st.markdown("""
<ul>
    <li><strong>Episode I</strong>: Die dunkle Bedrohung</span></li>
    <li><strong>Episode II</strong>: Angriff der Klonkrieger</span></li>
    <li><span style='color:gold;'><strong>Episode III</strong>: Die Rache der Sith</span></li>
    <li><strong>Episode IV</strong>: Krieg der Sterne</span></li>
    <li><strong>Episode V</strong>: Das Imperium schlägt zurück</span></li>
    <li><strong>Episode VI</strong>: Die Rückkehr der Jedi-Ritter</span></li>
    <li><strong>Episode VII</strong>: Das Erwachen der Macht</span></li>
    <li><strong>Episode VIII</strong>: Die letzten Jedi</span></li>
    <li><strong>Episode IX</strong>: Der Aufstieg Skywalkers</span></li>
</ul>
""", unsafe_allow_html=True)

with tab4:
    st.markdown("""
905 Mio. US-Dollar
""")
   
st.markdown("---")
   
with st.expander("Oscarverleihung 2006"):
    st.markdown("""
- Nominierung in der Kategorie Bestes Make-up
""")