import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
chosen_word = random.choice(word_list)

lives=6
word_length=len(chosen_word)
placeholder=""
for position in range(word_length):
    placeholder+="_"
print(placeholder)

game_over=False
correct_letter=[]
 
while not game_over:
    
    print(f"********** {lives} lives left **********")
    guess=input("guess a letter: ").lower()
    
    if guess in correct_letter:
        print(f"You have already guessed {guess}")
        continue
    display=""

    for letter in chosen_word:
        if(letter==guess):
            display +=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display +=letter
        else:
            display+="_"
    print(display)

    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess} that is not in the word. You lose a life")
        if(lives==0):
            game_over=True
            print(f"💀 Game Over! The word was '{chosen_word}'.")
    if "_" not in display:
        game_over=True
        print("🎉 Congratulations! You guessed the word.")

    print(stages[lives])


