import streamlit as st
import random
def app():
	st.markdown("<p style='font-size:25px'>Lets Start The Game!</p>",unsafe_allow_html=True)
	lst=[0,1]
	predicted=str(lst[random.randint(0,2)])
	if st.button('Shoot Yourself'):
		if predicted == '0':
			st.markdown("<p style='font-size:22px'>Congratulations! You Won. The Computer Lost.",unsafe_allow_html=True)
		elif predicted == '1':
			st.markdown("<p style='font-size:25px'>Oops! You Lost. The Computer Won.",unsafe_allow_html=True)	
	if st.button('Shoot the computer'):
		if predicted == '0':
			st.markdown("<p style='font-size:22px'>Oops! You Lost.The Computer Won",unsafe_allow_html=True)
		elif predicted == '1':
			st.markdown("<p style='font-size:25px'>Congratulations! You Won.The Computer Won",unsafe_allow_html=True)
