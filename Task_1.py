import requests, bs4, openpyxl, random

def check_if_complete(word, letters):
    temp_word = word
    # loops through all correctly guessed letters
    for letter in letters:
        # removes correct letters from temp word
        temp_word = temp_word.replace(letter, '')

    # if all letters are removed then all letters have been guessed correctly
    if len(temp_word) == 0:
        return True
    else:
        return False


res = requests.get("https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/")
soup = bs4.BeautifulSoup(res.text, 'html.parser')

paragraph_elements = soup.select('p')
# TODO not sure how else to select that specific paragraph
words_1000 = paragraph_elements[11].text
words_1000 = words_1000.split()

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Sheet1'

for i, word in enumerate(words_1000,start=1):
    sheet.cell(row=i, column=1).value = word

wb.save('1000_words.xlsx')

### Guessing Game ###

# randomly selects cell 1 - 1000 as the random word
random_number = random.randint(1,1000)
random_word = sheet.cell(row=random_number, column=1).value

correct_letters = []
incorrect_guesses = 0

correct_word = False

#loop until correct or too many guesses
while (incorrect_guesses < 5) and correct_word == False:

    # print out correct letters and blanks
    for letter in random_word:
        if letter in correct_letters:
            print(letter,end='')
        else:
            print('_',end='')
    print()

    # get and evaluate guess from user
    guess = input('guess a letter: ')
    print()
    if guess in random_word:
        # correct guess
        # add guess to correct letters
        correct_letters.append(guess)
    else:
        # wrong guess
        # increase incorrect guesses
        incorrect_guesses += 1

    # evaluate if word is completely guessed
    correct_word = check_if_complete(random_word, correct_letters)

#outside while loop
if correct_word:
    print('----------------------------------')
    print('You Won!')
    print('The word was:', random_word)
    print('----------------------------------')
else:
    print('----------------------------------')
    print('You Lost!')
    print('The word was:',random_word)
    print('----------------------------------')

# TODO maybe implement case insensitivity for the guesses
# TODO refactor code to be more modular with more functions
