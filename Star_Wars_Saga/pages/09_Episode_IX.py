import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("https://m.media-amazon.com/images/I/81KkxZjm-lL.jpg", width = 300)



with col2:
    st.header("""Star Wars - Die dunkle Bedrohung""")
    st.caption("1999 | 136 Minuten | FSK 6 | Lucasfilm Ltd. | 20th Century-Fox")

    col3, col4, col5 = st.columns(3)
    
    
    with col3:
        st.markdown(
        """
        <a href='https://www.disneyplus.com/de-de' target='_blank'>
            <img src='https://m.media-amazon.com/images/I/719t3jd2NeL.png' width='100' style='border-radius: 10px;'>
        </a>
        """,
        unsafe_allow_html=True
    )

    with col4:
        st.markdown(
        "<a href='https://www.amazon.de/gp/video/detail/amzn1.dv.gti.58a9f6be-72ff-c8ef-e942-d6249b50795a?autoplay=0&ref_=atv_cf_strg_wb'><img src='https://img.icons8.com/fluent/512/amazon-prime-video.png' width='100'></a>",
        unsafe_allow_html=True
    )

    with col5:
        st.markdown(
        "<a href='https://tv.apple.com/de/movie/star-wars-das-imperium-schlagt-zuruck/umc.cmc.3vabzkcmuoxxm3r3ng9q4rgh9?action=play'><img src='https://img.icons8.com/?size=512&id=10861&format=png' width='100'></a>",
        unsafe_allow_html=True
    )

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