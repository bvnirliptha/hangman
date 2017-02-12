# Hangman game
#

# -----------------------------------
# ( be sure to read the docstrings!)

import random
import string 
import sys
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if (letter not in lettersGuessed):
            return False
    
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string=''
    dict={}
    def getindex(alphabet):
        return ([i for i,x in enumerate(secretWord) if x==alphabet])
    
    wordlen = len(secretWord)
    for letter in lettersGuessed:
        index = getindex(letter)
        for value in index:
            dict[value] = letter
            
    for index in range(wordlen):
        if index in dict.keys():
                string+=' ' + dict[index]
        else:
                string+=" "+ '_'
        
    return (string)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    strin = ''
    alphabets=string.ascii_lowercase
    for letter in alphabets:
       if letter not in  lettersGuessed:
           strin = strin + letter

    return (strin)	


    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    '''
    numletters = len(secretWord)
    numguesses = 8
    remaininguesses = 8
    lettersguessed = ''
    counter = 8
    print 'The secretword has %d letters \n' %numletters
    while (remaininguesses >= 0):

	if (isWordGuessed(secretWord,lettersguessed)==False):
	
		if (remaininguesses==0):
			print 'You lose the game, the secret word is %s' %secretWord
			break
		else: 
			guessletter=raw_input('Guess a letter'+ ' ')	
	
		if (guessletter in lettersguessed):
			flag=1
			print 'You have already guessed the letter'
			print getAvailableLetters(lettersguessed)
			remaininguesses = numguesses
		else:
			flag=0
			lettersguessed +=guessletter	

	

		if guessletter in secretWord:
			remaininguesses= numguesses
		else:
			if flag==0:
				remaininguesses=numguesses-1
				numguesses-=1

		guessedword=getGuessedWord(secretWord, lettersguessed)
		print guessedword
		print getAvailableLetters(lettersguessed)

	else:
		print "Congragulations , You have guessed the Secret word %s" %secretWord 
		break
	
	print 'the number of remaining guesses are %d \n' %remaininguesses
	
	

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
