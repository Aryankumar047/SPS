import streamlit as st
import SPS_home
import SPS_game
dict={"Home":SPS_home,"The Game":SPS_game}
st.sidebar.title('Navigation')
ch=st.sidebar.radio('Go to',dict.keys())
if ch == 'Home':
	SPS_home.app()
elif ch == 'The Game':
	SPS_game.app()