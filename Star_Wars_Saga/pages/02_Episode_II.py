import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://cdn.moviepilot.de/files/bf02faec74bce8d92c6f37efb28185ce5058ac17e10245ae8abd679cc75e/copyright/19685181.jpg-r_1280_720-f_jpg-q_x-xxyxx.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Der Angriff der Klonkrieger""")
    st.caption("2002 | 142 Minuten | FSK 12")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.disneyplus.com/de-de/browse/entity-39cbdf17-1bbe-4de2-b4a4-8e342875c2c6" target="_blank">
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

st.write("Star Wars: Episode II – Angriff der Klonkrieger (Originaltitel Star Wars: Episode II – Attack of the Clones) ist ein US-amerikanischer Science-Fiction-Film aus dem Jahr 2002 und der zweite Teil der Star-Wars-Saga. Regie führte George Lucas und die Hauptrollen sind mit Hayden Christensen, Ewan McGregor, Christopher Lee und Natalie Portman besetzt. 2005 folgte die Fortsetzung Star Wars: Episode III – Die Rache der Sith. Der Film startete am 16. Mai 2002 in den deutschen Kinos.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "6.6/10")
        st.metric(label = "Moviepilot", value = "6.7/10")
        st.metric(label = "Filmstarts", value = "3.7/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Star_Wars:_Episode_II_-_Angriff_der_Klonkrieger)  
        * [iMDb](https://www.imdb.com/de/title/tt0121765/)
        """)

tab1, tab2, tab3 = st.tabs(["Stab", "Besetzung", "Chronologie"])


with tab1:
    st.markdown("""
- **Regie**: George Lucas, Jonathan Hales  
- **Drehbuch**: George Lucas
- **Produktion**: Rick McCallum
- **Musik**: John Williams
- **Kamera**: David Tattersall
- **Schnitt**: Ben Burtt, Paul Martin Smith
""")

with tab2:
    st.markdown("""
- **Hayden Christensen:**: Anakin Skywalker
- **Ewan McGregor**: Obi-Wan Kenobi
- **Natalie Portman**: Königin Padmé Amidala
- **Christopher Lee**: Count Dooku/Darth Tyranus
- **Samuel L. Jackson**: Mace Windu
- **Frank Oz**: Yoda
- **Ian McDiarmid**: Senator Sheev Palpatine/Darth Sidious
- **Pernilla August**: Shmi Skywalker-Lars
""")

with tab3:
   st.markdown("""
<ul>
    <li><strong>Episode I</strong>: Die dunkle Bedrohung</span></li>
    <li><span style='color:gold;'><strong>Episode II</strong>: Angriff der Klonkrieger</span></li>
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
   
with st.expander("Oscarverleihung 2003"):
    st.markdown("""
- Nominierung in der Kategorie Beste visuelle Effekte
""")