import streamlit as st
import random
def app():
	st.markdown("<p style='font-size:25px'>Lets Start The Game!</p>",unsafe_allow_html=True)
	lst=['stone','paper','scissors']
	predicted=str(lst[random.randint(0,2)])
	if st.button('Stone'):
		if predicted == 'stone':
			st.markdown("<p style='font-size:22px'>Its a Tie!</p>",unsafe_allow_html=True)
		elif predicted == 'paper':
			st.markdown("<p style='font-size:22px'>Oops! You lost.",unsafe_allow_html=True)
		elif predicted == 'scissors':
			st.markdown("<p style='font-size:25px'>Congratulations! You won.",unsafe_allow_html=True)	
	if st.button('Paper'):
		if predicted == 'paper':
			st.markdown("<p style='font-size:22px'>Its a Tie!</p>",unsafe_allow_html=True)
		elif predicted == 'scissors':
			st.markdown("<p style='font-size:22px'>Oops! You lost.",unsafe_allow_html=True)
		elif predicted == 'stone':
			st.markdown("<p style='font-size:25px'>Congratulations! You won.",unsafe_allow_html=True)
	if st.button('Scissors'):
		if predicted == 'scissors':
			st.markdown("<p style='font-size:22px'>Its a Tie!</p>",unsafe_allow_html=True)
		elif predicted == 'stone':
			st.markdown("<p style='font-size:22px'>Oops! You lost.",unsafe_allow_html=True)
		elif predicted == 'paper':
			st.markdown("<p style='font-size:25px'>Congratulations! You won.",unsafe_allow_html=True)
