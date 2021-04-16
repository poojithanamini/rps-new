import streamlit as st
import random

st.write("Choose your weapon Rock, Paper, or Scissors: ")

userChoice = st.radio('', ['Rock', 'Paper', 'Scissors'])

choices = ['Rock', 'Paper', 'Scissors']
opponenetChoice = random.choice(choices)

st.write("You chose: "+userChoice)
st.write("I chose: " + opponenetChoice)

if opponenetChoice == userChoice:   
    st.write("Tie! 😁")
elif opponenetChoice == 'Rock' and userChoice == 'Scissors':      
    st.write("Scissors beats rock, I win! 🎉")
    pass
elif opponenetChoice == 'Scissors' and userChoice == 'Paper':          
    st.write("Scissors beats paper, I win! 🎉")
    pass
elif opponenetChoice == 'Paper' and userChoice == 'Rock':      
    st.write("Paper beats rock, I win! 🎉")
    pass
else:       
    st.write("You win! 😒")