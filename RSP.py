import streamlit as st
import random

def play_game(player_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    st.write(f"Your choice: {player_choice}")
    st.write(f"Computer's choice: {computer_choice}")

    if player_choice == computer_choice:
        st.write("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        st.write("You win!")
    else:
        st.write("You lose!")

st.title("Rock, Paper, Scissors")

player_choice = st.radio("Choose your move:", ('rock', 'paper', 'scissors'))
play_game(player_choice)