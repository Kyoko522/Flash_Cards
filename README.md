Flashcard Program README:

This is a Python program that lets you create, load and quiz on flashcards. You can add flashcards to the deck, remove cards from it, save and load decks, and quiz yourself on the flashcards.

Requirements:

This program requires the following:

Python 3.x
os.path module
time module

How to Use:

Run the program from the command line using python flashcard_program.py.

The program will prompt you to either create a new deck or load an existing one.

If you choose to create a new deck, you will be prompted to enter a name for your new deck and the number of flashcards you want to add. You can then add the flashcards by entering a question and answer for each one.

If you choose to load an existing deck, you will be prompted to enter the name of the deck you want to load. If the deck exists, the program will load it and you can start using it.

Once you have created or loaded a deck, you can add more flashcards, remove cards, save the deck, or start a quiz.

If you choose to start a quiz, the program will randomly select flashcards from the deck and ask you to answer them. After each flashcard, you will be asked if you got the answer right or wrong. The program will keep track of your right and wrong answers.

Once you finish the quiz, the program will display your score.

Note
The program saves the decks in a .txt file in the same directory as the program. If you delete the .txt file, you will lose the saved deck.
