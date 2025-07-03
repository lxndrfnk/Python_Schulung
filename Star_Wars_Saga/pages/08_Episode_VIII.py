import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="display: flex; justify-content: left;">
        <img src="https://m.media-amazon.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_FMjpg_UX1000_.jpg"
             style="border: 4px solid #FFD700; border-radius: 10px; width: 300px;">
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.header("""Star Wars - Die letzten Jedi""")
    st.caption("2017 | 152 Minuten | FSK 12")
    st.markdown("""
    <div style="text-align: left;">
        <a href="https://www.disneyplus.com/de-de/browse/entity-50c1aff5-3051-4839-9ebf-e332c635e216" target="_blank">
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

st.write("Star Wars: Die letzten Jedi (Originaltitel Star Wars: The Last Jedi) ist ein US-amerikanischer Science-Fiction-Film aus dem Jahr 2017 und die achte Episode der Star-Wars-Filmreihe. Die Regie übernahm Rian Johnson, der auch das Drehbuch schrieb. Produziert wurde der Film von Kathleen Kennedy und Ram Bergman. J. J. Abrams, der bei Vorgänger- und Nachfolgefilm Regie führte, verblieb als Executive Producer.")
            
# ---------- Sidebar ----------

with st.sidebar:
        st.markdown("""
        <h1 style='font-size: 30px;'>📈 Ratings</h1>
        """, unsafe_allow_html=True)
        st.metric(label = "iMDb", value = "6.9/10")
        st.metric(label = "Moviepilot", value = "6.3/10")
        st.metric(label = "Filmstarts", value = "3.4/5")
        st.markdown("---")
        st.header("🔗 Links")
        st.markdown("""
        * [Wikipedia](https://de.wikipedia.org/wiki/Star_Wars:_Die_letzten_Jedi)  
        * [iMDb](https://www.imdb.com/de/title/tt2527336/)
        """)

tab1, tab2, tab3, tab4 = st.tabs(["Stab", "Besetzung", "Chronologie", "Einspielergebnis"])


with tab1:
    st.markdown("""
- **Regie**: Rian Johnson
- **Drehbuch**: Rian Johnson
- **Produktion**: Kathleen Kennedy, Ram Bergman
- **Musik**: John Williams
- **Kamera**: Steve Yedlin
- **Schnitt**: Bob Ducsay
""")

with tab2:
    st.markdown("""
- **Daisy Ridley**: Rey
- **John Boyega**: Finn
- **Oscar Isaac**: Poe Dameron
- **Adam Driver**: Kylo Ren / Ben Solo
- **Mark Hamill**: Luke Skywalker
- **Carrie Fisher**: General Leia Organa
- **Andy Serkis**: Oberster Anführer Snoke
- **Laura Dern**: Vizeadmiral Holdo
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
    <li><span style='color:gold;'><strong>Episode VIII</strong>: Die letzten Jedi</span></li>
    <li><strong>Episode IX</strong>: Der Aufstieg Skywalkers</span></li>
</ul>
""", unsafe_allow_html=True)

with tab4:
    st.markdown("""
1.3 Mrd. US-Dollar
""")
   
st.markdown("---")
   
with st.expander("Oscarverleihung 2018"):
    st.markdown("""
- Nominierung in der Kategorie beste visuelle Effekte
- Nominierung in der Kategorie beste Filmmusik 
- Nominierung in der Kategorie bester Ton 
- Nominierung in der Kategorie bester Tonschnitt
""")