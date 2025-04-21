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

def get_words(link):
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    paragraph_elements = soup.select('p')
    words = paragraph_elements[11].text
    words = words.split()

    return words

def xls_word(words):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Sheet1'

    for i, word in enumerate(words_1000, start=1):
        sheet.cell(row=i, column=1).value = word

    wb.save('1000_words.xlsx')

    random_number = random.randint(1, 1000)
    random_word = sheet.cell(row=random_number, column=1).value

    return random_word

def play_game(random_word):
    # define initial values
    correct_letters = []
    incorrect_guesses = 0
    correct_word = False

    # loop until correct or too many guesses
    while (incorrect_guesses < 5) and correct_word == False:

        # print out correct letters and blanks
        for letter in random_word:
            if letter in correct_letters:
                print(letter, end='')
            else:
                print('_', end='')
        print()

        # get and evaluate guess from user
        guess = input('guess a letter: ').lower()
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

    # outside while loop
    return correct_word

def end_game_screen(if_correct, random_word):
    if if_correct:
        print('----------------------------------')
        print('You Won!')
        print('The word was:', random_word)
        print('----------------------------------')
    else:
        print('----------------------------------')
        print('You Lost!')
        print('The word was:', random_word)
        print('----------------------------------')

# link for the 1000_words website
top_1000_words = "https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/"
# get the list of 1000 words
words_1000 = get_words(top_1000_words)

### Guessing Game ###

# Put words into Excel and select random word
random_word = xls_word(words_1000)

# play the game and return if the word was guessed
if_correct = play_game(random_word)

# print the final game screen
end_game_screen(if_correct, random_word)
