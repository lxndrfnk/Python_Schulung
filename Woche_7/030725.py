import streamlit as st
 
if "zähler" not in st.session_state:
    st.session_state.zähler = 0
 
if st.button("Klick mich"):
    st.session_state.zähler += 1
 
st.metric("Button geklickt", value=st.session_state.zähler)
 
print(st.session_state)