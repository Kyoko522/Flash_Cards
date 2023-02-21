import math
import time
import random
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

1.New Flash Cards
2.Load Flash Cards \n""")

    while userinput != "1" or userinput != "2":
        if userinput == "1" or userinput.lower()=="new" or userinput.lower() == "New Flash Cards":
            new_deck_name()
            new_deck()
            break
        elif userinput == "2" or userinput.lower()=="load" or userinput.lower() =="Load Flash Cards" :
            load_deck()
            break
        else:
            print("That is a invalid input")
            userinput = input("""Flash Cards, the best way to study

1.New Flash Cards
2. Load Old Flash Cards \n """)


    option = input("""What do you want to do next:
1. Add Cards
2. Start Quiz
3. Remove a Card
4. Save Deck
        """)
    while int(option) > 1 and int(option) < 3:
        if option == "1":
            add_card_to_deck()
            break
        elif option == "2":
            quiz()
        elif option == "3":
            pass
        elif option == "4":
            pass
        else:
            option = input("Invalid input please try again: ")



def load_deck():
    pass

name =""
num = 0
deck = []
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
    wrong = []
    right = []
    print ("Test how well you know your stuff\n")
    print ("""Quick notes:
-> If you would like to leave the quiz enter \"#\" after the answer is revealed
-> After the question appears press space bar once to reveal the answer
-> After each answer is revealed a prompt will ask if you got it right or wrong (answer honestly)


The test will begin shortly... """)

    # time.sleep(6)
    while True:
        # print ("-------------------------------------------------")
        # for i in range(len(deck)):
        #     print(deck[i].question + " -> " + deck[i].answer)
        #
        # for i in range(len(right)):
        #     print(right[i].question + " -> " + right[i].answer)
        #
        # for i in range(len(wrong)):
        #     print(wrong[i].question + " -> " + wrong[i].answer)
        #
        # print("-------------------------------------------------")

        print ("\n")

        rand = random.randint(1,100)
        if rand <= 40:
            if len(deck) > 1:
                rand_index = random.randint(0, len(deck)-1)
                confirm(deck[rand_index].question)
                print(deck[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break
            elif len(wrong) > 1:
                rand_index = random.randint(0, len(wrong)-1)
                confirm(wrong[rand_index].question)
                print(wrong[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break
            elif len(right) > 1:
                rand_index = random.randint(0, len(right)-1)
                confirm(right[rand_index].question)
                print(right[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break
        if 40 < rand <= 85:
            if len(wrong) >= 1:
                rand_index = random.randint(0,len(wrong)-1)
                confirm(wrong[rand_index].question)
                print(wrong[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break
            elif len(deck) >= 1:
                rand_index = random.randint(0,len(deck)-1)
                confirm(deck[rand_index].question)
                print(deck[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break
            elif len(right) >=  1:
                rand_index = random.randint(0,len(right)-1)
                confirm(right[rand_index].question)
                print(right[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break
        else:
            if len(right) >= 1:
                rand_index = random.randint(0,len(right)-1)
                confirm(right[rand_index].question)
                print(right[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break
            elif len(wrong) >= 1:
                rand_index = random.randint(0,len(wrong)-1)
                confirm(wrong[rand_index].question)
                print(wrong[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break
            elif len(deck) >= 1:
                rand_index = random.randint(0,len(deck)-1)
                confirm(deck[rand_index].question)
                print(deck[rand_index].answer)
                if sort_result().lower() == "y":
                    right.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "n":
                    wrong.append(deck[rand_index])
                    deck.remove(deck[rand_index])
                elif sort_result().lower() == "#":
                    break

        # print("-------------------------------------------------")
        #
        # print("random index is " + str(rand_index))
        # print("random number is " + str(rand))
        #
        # print("-------------------------------------------------")



def to_small():
    print("The deck is to small, add more cards to continue")
    add_card_to_deck()

def confirm(banana):
    i = input(banana)

def sort_result():
    were_u_right = input("Did you get the question right: (Y/N/#)")
    return were_u_right.lower()


if __name__ == "__main__":
    main()