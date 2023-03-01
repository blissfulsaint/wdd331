secret = 'isaiah'
secret_length = len(secret)

print('Welcome to the word guessing game!')
print('Your hint is: ', end='')
for i in range(secret_length):
    print('_', end=' ')
print('')
guess_word = ''
guess_count = 0

while guess_word != secret:
    guess_word = input('What is your guess? ')
    if guess_word == secret:
        break
    guess_length = len(guess_word)
    if guess_length != secret_length:
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        print('Your hint is: ', end='')
        for i in range(guess_length):
            letter = guess_word[i]
            match = ''
            if letter == secret[i]:
                match = letter.capitalize()
            else:
                for secret_letter in secret:
                    if letter == secret_letter:
                        match = letter.lower()
                        break
                    else:
                        match = '_'
            print(match, end=' ')
    print('\n')
    guess_count += 1

print('Congrats! You guessed it!')
print(f'It took you {guess_count} guesses.')