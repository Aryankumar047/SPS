import streamlit as st
import random
def app():
	st.markdown("<p style='font-size:25px'>Lets Start The Game!</p>",unsafe_allow_html=True)
	pr=st.text_input('Enter Your Choice Below👇')
	lst=['stone','paper','scissors']
	predicted=str(lst[random.randint(0,2)])
	if pr == predicted:
		st.write('Its a Tie!')
		st.write('Do you wanna rematch? Then enter your choice again.')
	elif (pr in ['Stone','stone'] and predicted == 'scissors') or (pr in ['Paper','paper'] and predicted == 'stone') or (pr in ['Scissors','scissors'] and predicted == 'paper'):
		st.write('Conratulations! You won.')
		st.write('Do you wanna rematch? Then enter your choice again.')
	elif (pr in ['Stone','stone'] and predicted == 'paper') or (pr in ['Paper','paper'] and predicted == 'scissors') or (pr in ['Scissors','scissors'] and predicted == 'stone'):
		st.write('Oops! Better luck next Time')
		st.write('Do you wanna rematch? Then enter your choice again.')
