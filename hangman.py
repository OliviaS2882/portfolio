import random
from hangman_art import logo, stages
from hangman_words import word_list 

end_of_game = False
#word_list = ["ardvark", "baboon", "camel", "kangaroo", "elephant"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left. 
# Set 'lives' to equal 6.

lives = 6

# Create blank list of guessed letters.
display = []

print(logo)

# Replace each letter in chosen word with '_'.
for _ in range(word_length):
    display += "_"

# Loop through each position in the chosen_word, if the letter at that position matches 'guess' then reveal that letter in the display at that position.
end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      print("You found a letter, well done!")
  
  # If letter is not found, reduce lives. If lives reduce to 0, end game.
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the chosen word. You lose a life.")
    lives -= 1

    if lives == 0:
      end_of_game = True
      print(f"\nYou lose. The mystery word was {chosen_word}.")
            
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win!")
  
  # Print relevant image from stages list to show lives remaining.
  print(stages[lives])   

