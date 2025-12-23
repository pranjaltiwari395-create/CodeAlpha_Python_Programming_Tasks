import random

# Predefined list of 5 words
word_list = ["pranjal", "raghav", "manpreet", "python", "coding"]

lives = 6
chosen_word = random.choice(word_list)

# Create placeholder (e.g. "______")
word_length = len(chosen_word)
placeholder = "_" * word_length
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    # Check each letter in the chosen word
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # Wrong guess
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            print("You Lose! The word was:", chosen_word)
            game_over = True

    # All letters guessed
    if "_" not in display:
        print("You Win! 🎉")
        game_over = True
