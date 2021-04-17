import streamlit as st
import random

option = st.sidebar.selectbox('Select', ['Rock, Paper, Scissor', 'With Lizard and Spock'])
if option == 'Rock, Paper, Scissor':
    st.title('ROCK, PAPER, SCISSORS')

    st.write("Choose your weapon - Rock, Paper, or Scissors: ")

    userChoice = st.radio('', ['Rock', 'Paper', 'Scissors'])

    choices = ['Rock', 'Paper', 'Scissors']
    opponentChoice = random.choice(choices)

    st.write("You chose: "+userChoice)
    st.write("I chose: " + opponentChoice)

    if opponentChoice == userChoice:   
        st.write("Tie! 😁")
    elif opponentChoice == 'Rock' and userChoice == 'Scissors':      
        st.write("Rock crushes Scissors, I win! 🎉")
        pass
    elif opponentChoice == 'Scissors' and userChoice == 'Paper':          
        st.write("Scissors cuts Paper, I win! 🎉")
        pass
    elif opponentChoice == 'Paper' and userChoice == 'Rock':      
        st.write("Paper covers Rock, I win! 🎉")
        pass
    else:       
        st.write("You win! 😒")
if option == 'With Lizard and Spock':
    st.title('ROCK, PAPER, SCISSORS, LIZARD, SPOCK')
    st.write('')
    st.write('')
    st.write("Choose your weapon - Rock, Paper, Scissors, Lizard, Spock: ")

    userChoice = st.radio('', ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])

    choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    opponentChoice = random.choice(choices)

    st.write("You chose: "+userChoice)
    st.write("I chose: " + opponentChoice)

    if opponentChoice == userChoice:   
        st.write("Tie! 😁")
    elif opponentChoice == 'Scissors' and userChoice == 'Paper':      
        st.write("Scissors cuts Paper, I win! 🎉")
        pass
    elif opponentChoice == 'Paper' and userChoice == 'Rock':          
        st.write("Paper covers Rock, I win! 🎉")
        pass
    elif opponentChoice == 'Rock' and userChoice == 'Lizard':      
        st.write("Rock crushes Lizard, I win! 🎉")
        pass
    elif opponentChoice == 'Spock' and userChoice == 'Scissors':      
        st.write("Spock smashes Scissors, I win! 🎉")
        pass
    elif opponentChoice == 'Lizard' and userChoice == 'Spock':      
        st.write("Lizard poisons Spock, I win! 🎉")
        pass
    elif opponentChoice == 'Scissors' and userChoice == 'Lizard':      
        st.write("Scissors decapitates Lizard, I win! 🎉")
        pass
    elif opponentChoice == 'Lizard' and userChoice == 'Paper':      
        st.write("Lizard eats Paper, I win! 🎉")
        pass
    elif opponentChoice == 'Paper' and userChoice == 'Spock':      
        st.write("Paper disproves Spock, I win! 🎉")
        pass
    elif opponentChoice == 'Spock' and userChoice == 'Rock':      
        st.write("Spock vaporizes Rock, I win! 🎉")
        pass
    elif opponentChoice == 'Rock' and userChoice == 'Scissors':      
        st.write("Rock crushes Scissors, I win! 🎉")
        pass
    else:       
        st.write("You win! 😒")