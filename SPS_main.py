import streamlit as st
import SPS_home
import SPS_game
st.set_page_config(page_title = 'Stone Paper Scissors',
                    page_icon = ':Controller:',
                    layout = 'centered',
                    initial_sidebar_state = 'auto'
                    )
dict={"Home":SPS_home,"The Game":SPS_game}
st.sidebar.title('Navigation')
ch=st.sidebar.radio('Go to',dict.keys())
if ch == 'Home':
	SPS_home.app()
elif ch == 'The Game':
	SPS_game.app()
