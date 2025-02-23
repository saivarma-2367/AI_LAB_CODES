import random

def display_hangman(parts_left):
    hangman_states = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =====
        """
    ]
    print(hangman_states[parts_left])

def ai_guess(guessed_letters):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    possible_choices = [c for c in alphabet if c not in guessed_letters]
    return random.choice(possible_choices) if possible_choices else None

def play_hangman():
    word = input("Player 1, enter a word: ").lower()
    guessed_word = ['_'] * len(word)
    guessed_letters = set()
    body_parts = 6  # AI starts with full body
    
    print("\nGame Starts! AI is guessing...")
    
    while body_parts >= 0 and '_' in guessed_word:
        display_hangman(body_parts)
        print("Current Word: ", " ".join(guessed_word))
        guess = ai_guess(guessed_letters)
        if not guess:
            print("AI has no more letters to guess!")
            break
        print(f"AI guesses: {guess}")
        guessed_letters.add(guess)
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            body_parts = min(6, body_parts + 1) 
        else:
            body_parts -= 1 
        
    display_hangman(body_parts)
    if '_' not in guessed_word:
        print("AI Wins! The word was:", word)
    else:
        print("Player 1 Wins! The word was:", word)

play_hangman()