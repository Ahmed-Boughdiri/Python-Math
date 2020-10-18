from lessons import Lessons
from suite_réelles import SuiteRéelles

def starter():
    lessons_list = Lessons()
    for title in lessons_list.titles:
        print(f"1-{title}")
    choice = None
    while((choice is None) or (choice <= 0) or (choice > len(lessons_list.titles))):
        choice = input("Choisir Le Leçon: ")
        if(choice in "0123456789"):
            choice = int(choice)
        else:
            choice = None
    return choice

def start_suite_réelles():
    print("Entrer Votre Equation: ")
    x = input("> ")
    taritement = SuiteRéelles(x)
    taritement.calc()

def direct(choice):
    directions = {
        1: start_suite_réelles
    }
    directions[choice]()

direct(starter())
