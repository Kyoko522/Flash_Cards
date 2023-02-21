import time
import random
import os.path
from os import path
class Flashcard:
    def __init__(self,question, answer):
        self.question = question
        self.answer = answer


    def get_question(self):
        return self.question

    def get_answer(self):
        print (self.answer)

def main():
    userinput = input("""Flash Cards, the best way to study

1. New Flash Cards
2. Load Flash Cards
3. Remove Flash Cards\n""")

    while userinput != "1" or userinput != "2":
        if userinput == "1" or userinput.lower()=="new" or userinput.lower() == "New Flash Cards":
            new_deck_name()
            new_deck()
            break
        elif userinput == "2" or userinput.lower()=="load" or userinput.lower() =="Load Flash Cards" :
            load_deck()
            break
        elif userinput == "3" or userinput.lower()=="remove" or userinput.lower()=="Remove Flash Cards":
            remove_deck()
        else:
            print("That is a invalid input")
            userinput = input("""Flash Cards, the best way to study

1.New Flash Cards
2. Load Old Flash Cards \n """)
    meanu()


def meanu():
    option = input("""What do you want to do next:
1. Add Cards
2. Start Quiz
3. Remove a Card
4. Save Deck
5. Back
""")
    if option == "1":
        add_card_to_deck()
    elif option == "2":
        quiz()
    elif option == "3":
        remove_card()
    elif option == "4":
        save_deck()
    elif option == "5":
        main()
    else:
        print("Invalid input please try again: ")
        meanu()


def load_deck():
    name = input("What is the name of the deck")
    if path.exist(name + ".txt"):
        with open(name + ".txt", 'r') as file:
            for line in file:
                if line == "Start Questions in deck:_>!%^@":
                    deck.append(line)




def remove_deck():
    name = input("What is the name of the Deck you want to remove: ")

name =""
num = 0
deck = []
wrong = []
right = []
def new_deck_name():
    global name
    name = input("Name of deck: \t\t\t\t")
    return name

def new_deck():
    num = int(input("How many cards do you want:\t"))
    for i in range (num):
        question = input("Question -> \t\t\t\t")
        answer = input("Answer -> \t\t\t\t\t")
        card = Flashcard(question,answer)
        global deck
        deck.append(card)
    print("\nSuccessfully added all cards to the the deck\n")
    return deck

def add_card_to_deck():
    print("Type # in the question input to stop adding cards\n")
    while True :
        question = input("Question -> \t\t\t\t")
        answer = input("Answer -> \t\t\t\t\t")
        card = Flashcard(question,answer)
        global deck
        deck.append(card)
        print("Successfully added to deck")


def quiz():
    global wrong
    global right
    print ("Test how well you know your stuff\n")
    print ("""Quick notes:
-> If you would like to leave the quiz enter \"#\" after the answer is revealed
-> After the question appears press space bar once to reveal the answer
-> After each answer is revealed a prompt will ask if you got it right or wrong (answer honestly)


The test will begin shortly... """)

    time.sleep(6)
    while True:
        print ("\n")

        rand = random.randint(1,100)
        if rand <= 40:
            if len(deck) > 1:
                rand_index = random.randint(0, len(deck)-1)
                confirm(deck[rand_index].question)
                print("Answer -> \t" +deck[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    meanu()
                    break
            elif len(wrong) > 1:
                rand_index = random.randint(0, len(wrong)-1)
                confirm(wrong[rand_index].question)
                print("Answer -> \t" + wrong[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(wrong[rand_index])
                    deck.remove(wrong[rand_index])
                elif sort_result().lower() == "n":
                    pass
                elif sort_result().lower() == "#":
                    meanu()
                    break
            elif len(right) > 1:
                rand_index = random.randint(0, len(right)-1)
                confirm(right[rand_index].question)
                print("Answer -> \t" +right[rand_index].answer)
                if sort_result().lower() == "y":
                    pass
                elif sort_result().lower() == "n":
                    wrong.append(right[rand_index])
                    deck.remove(right[rand_index])
                elif sort_result().lower() == "#":
                    meanu()
                    break
        if 40 < rand <= 85:
            if len(wrong) >= 1:
                rand_index = random.randint(0,len(wrong)-1)
                confirm(wrong[rand_index].question)
                print("Answer -> \t" +wrong[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(wrong[rand_index])
                    deck.remove(wrong[rand_index])
                elif sort_result().lower() == "n":
                    pass
                elif sort_result().lower() == "#":
                    meanu()
                    break
            elif len(deck) >= 1:
                rand_index = random.randint(0,len(deck)-1)
                confirm(deck[rand_index].question)
                print("Answer -> \t" +deck[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    meanu()
                    break
            elif len(right) >=  1:
                rand_index = random.randint(0,len(right)-1)
                confirm(right[rand_index].question)
                print("Answer -> \t" +right[rand_index].answer)
                if sort_result().lower() == "y":
                    pass
                elif sort_result().lower() == "n":
                    wrong.append(right[rand_index])
                    deck.remove(right[rand_index])
                elif sort_result().lower() == "#":
                    meanu()
                    break
        else:
            if len(right) >= 1:
                rand_index = random.randint(0,len(right)-1)
                confirm(right[rand_index].question)
                print("Answer -> \t" +right[rand_index].answer)
                if sort_result().lower() == "y":
                    pass
                elif sort_result().lower() == "n":
                    wrong.append(right[rand_index])
                    deck.remove(right[rand_index])
                elif sort_result().lower() == "#":
                    meanu()
                    break
            elif len(wrong) >= 1:
                confirm(wrong[rand_index].question)
                print("Answer -> \t" +wrong[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(wrong[rand_index])
                    deck.remove(wrong[rand_index])
                elif sort_result().lower() == "n":
                    pass
                elif sort_result().lower() == "#":
                    meanu()
                    break
            elif len(deck) >= 1:
                rand_index = random.randint(0,len(deck)-1)
                confirm(deck[rand_index].question)
                print("Answer -> \t" +deck[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    meanu()
                    break

def remove_card():
    count = 0
    remove_question = input("Type in the question that you want to remove: ")
    remove_answer = input("Type in the answer that you want to remove: ")
    for d in range(len(deck)):
        if deck[d].question == remove_question and deck[d].answer == remove_answer:
            deck.remove[d]
            count = 1
    for r in range(len(right)):
        if right[r].question == remove_question and right[r].answer == remove_answer:
            right.remove(r)
            count = 1

    for w in range(len(wrong)):
        if wrong[w].question == remove_question and right[w].answer == remove_answer:
            right.remove(r)
            count = 1

    if count == 0:
        print("The Card with that question and answer doesn't not exist")
        try_again = input("\nWould you like to try again? (y/n)")
        if try_again.lower() == "y":
            remove_card()
        else:
            meanu()

def save_deck():
    print ("it does run this method")
    with open(name+".txt",'w') as file:
        file.write("Start Questions in deck:_>!%^@\n")
        for i in deck:
            file.write(str(i) +'\n')
        file.write("End Questions in deck:_>!%^@")

        file.write("Start Questions in right:_>!%^@\n")
        for j in right:
            file.write(str(j) + '\n')
        file.write("End Questions in right:_>!%^@")

        file.write("Start Questions in wrong:_>!%^@\n")
        for n in wrong:
            file.write(str(n) + '\n')
        file.write("End Questions in wrong:_>!%^@")

    print("The deck has be successfully saved")
    time.sleep(3)
    meanu()


def to_small():
    print("The deck is to small, add more cards to continue")
    add_card_to_deck()

def confirm(banana):
    i = input("Question -> \t" + banana)

def sort_result():
    were_u_right = input("Did you get the question right: (Y/N/#)")
    return were_u_right.lower()


if __name__ == "__main__":
    main()