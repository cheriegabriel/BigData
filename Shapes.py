import random
#import math
from math import *

def main():
    select = {}
    menu(select)

class user:
    def __init__(self, username, select, initial_score = 0):
        self.__username = username
        self.select = select
        self.__initial_score = initial_score
        self.register()

    #to filter the username in the select object
    def register(self):
        if self.__username not in self.select.keys():
            self.select[self.__username] = self.__initial_score


class Shape:
    def __init__(self,r, shapename, select, username, peri, area):
        self.username = username
        self.shapename = shapename
        self.peri = peri
        self.area = area
        self.select = select


    def AnswerDetails(self):
        print('Correct Answers below.')


class Square(Shape):

    def __init__(self, r, shapename, select, username, peri, area, length):
        super().__init__(r, shapename, select, username, peri, area)
        self.length = length

    def output(self):
        Speri = float(4 * self.length)
        Sarea = float(self.length * self.length)
        print('Correct Perimeter: {}'.format(Speri))
        print('Correct Area : {}'.format(Sarea))
        if (round(Speri,2) == round(self.peri,2)):
            print('Your answer in perimeter is correct. \n')
            self.select[self.username] = self.select[self.username]+1
        else:
            print('Your answer in perimeter is incorrect. \n')


        if (round(Sarea,2) == round(self.area,2)):
            print('Your answer in area is correct.\n')
            self.select[self.username] = self.select[self.username]+1
        else:
            print('Your answer in perimeter is incorrect.\n')


    def AnswerDetails(self):
        print('You have completed the Square game.')


    def process_data(self):
        super().AnswerDetails()
        self.output()
        self.AnswerDetails()


class Rectangle(Shape):

    def __init__(self, r, shapename, select, username, peri, area, Rlength, Rheight):
        super().__init__(r, shapename, select, username, peri, area)
        self.Rlength = Rlength
        self.Rheight = Rheight


    def output(self):
        Rperi = float(2*(self.Rlength + self.Rheight))
        Rarea = float(self.Rlength * self.Rlength)
        print('Correct Perimeter: {}'.format(Rperi))
        print('Correct Area : {}'.format(Rarea))
        if (round(Rperi,2) == round(self.peri,2)):
            print('Your answer in perimeter is correct. \n')
            self.select[self.username] = self.select[self.username]+1
        else:
            print('Your answer in perimeter is incorrect. \n')


        if (round(Rarea,2) == round(self.area,2)):
            print('Your answer in area is correct.\n')
            self.select[self.username] = self.select[self.username]+1
        else:
            print('Your answer in perimeter is incorrect.\n')


    def AnswerDetails(self):
        print('You have completed the Rectangle game.')


    def process_data(self):
        super().AnswerDetails()
        self.output()
        self.AnswerDetails()


class Triangle(Shape):

    def __init__(self, r, shapename, select, username, peri, area, Tlength):
        super().__init__(r, shapename, select, username, peri, area)
        self.Tlength = Tlength

    def output(self):
        Tperi = float(3 * self.Tlength)
        Tarea = float(sqrt(3) / 4 * self.Tlength * self.Tlength)
        print('Correct Perimeter: {}'.format(Tperi))
        print('Correct Area : {}'.format(Tarea))
        if (round(Tperi,2) == round(self.peri,2)):
            print('Your answer in perimeter is correct. \n')
            self.select[self.username] = self.select[self.username]+1
        else:
            print('Your answer in perimeter is incorrect. \n')


        if (round(Tarea,2) == round(self.area,2)):
            print('Your answer in area is correct.\n')
            self.select[self.username] = self.select[self.username]+1
        else:
            print('Your answer in perimeter is incorrect.\n')


    def AnswerDetails(self):
        print('You have completed the Triangle game.')


    def process_data(self):
        super().AnswerDetails()
        self.output()
        self.AnswerDetails()


class Circle(Shape):

    def __init__(self, r, shapename, select, username, peri, area, radius):
        super().__init__(r, shapename, select, username, peri, area)
        self.radius = radius


    def output(self):
        Cperi = float(2 * 3.14 * self.radius)
        Carea = float(3.14 * self.radius * self.radius)
        print('Correct Perimeter: {}'.format(round(Cperi,2)))
        print('Correct Area : {}'.format(Carea))
        if (round(Cperi,2) == round(self.peri,2)):
            print('Your answer in perimeter is correct. \n')
            self.select[self.username] = self.select[self.username]+1
        else:
            print('Your answer in perimeter is incorrect. \n')


        if (round(Carea,2) == round(self.area,2)):
            print('Your answer in area is correct.\n')
            self.select[self.username] = self.select[self.username]+1
        else:
            print('Your answer in perimeter is incorrect.\n')


    def AnswerDetails(self):
        print('You have completed the Circle game.')


    def process_data(self):
        super().AnswerDetails()
        self.output()
        self.AnswerDetails()

#get scores
def ShowScore(select):
    if select:
        print("=======================")
        print('|   User   |   Score  |')
        print("=======================")
        for user, score in select.items():
            print(' {}    |    {}   '.format(user, score))
            print("=======================")
    else:
        print("You are not a registered user. Please register first.\n")
        main()

#input answers
def input_answers():
    ans_error_peri = True
    while ans_error_peri:
        try:
            peri = float(input('Enter the Perimeter (Default unit = cm) : '))
        except ValueError:
            print("Invalid value.. Please try again!")
            continue
        else:
            ans_error_peri = False


    ans_error_area = True


    while ans_error_area:
        try:
            area = float(input('Enter the Area (Default unit = cm) : '))
        except ValueError:
            print("Invalid value.. Please try again!")
            continue
        else:
            ans_error_area = False
    answer = [peri, area]
    return answer

#the function below will let the user play.
def game(select, username):
    error_game_entry = True
    while error_game_entry:
        try:
            game_entry = int(input("Enter the number of tries you want to play [Available shapes to play: Square, Rectangle, Triangle and Circle]: "))
            #A user can play up to 20x
            if game_entry > 20:
                print("Maximum game to play is 20")
                continue
        except ValueError:
            print("You have to enter a valid number from 1 to 20. Please try again.")
            continue
        else:
            error_game_entry = False
        for n in range(game_entry):
            r = random.randint(1, 4)

            if (r == 1):
                shapename = 'SQUARE'
                length = random.randint(1, 10)
                print("\nYou will play: " + shapename +'\n')
                print('\nLength of SQUARE: {} cm '.format(length))
                answer_list = input_answers()
                peri = answer_list[0]
                area = answer_list[1]
                square = Square(r, shapename, select, username, peri, area, length)
                square.process_data()

            elif (r == 2):
                shapename = 'RECTANGLE'
                Rlength = random.randint(1, 10)
                Rheight = random.randint(1, 10)
                print("\nYou will play: " + shapename + '\n')
                print('\nLength of RECTANGLE: {} cm \n Height of RECTANGLE: {} cm '.format(Rlength, Rheight))
                answer_list = input_answers()
                peri = answer_list[0]
                area = answer_list[1]
                rectangle = Rectangle(r, shapename, select, username, peri, area, Rlength, Rheight)
                rectangle.process_data()

            elif (r == 3):
                shapename = 'TRIANGLE'
                Tlength = random.randint(1, 10)
                print("\nYou will play an Equilateral " + shapename + '.\n')
                print("\nLength is: {} cm ".format(Tlength))
                answer_list = input_answers()
                peri = answer_list[0]
                area = answer_list[1]
                triangle = Triangle(r, shapename, select, username, peri, area, Tlength)
                triangle.process_data()

            elif (r == 4):
                shapename = 'CIRCLE'
                radius = random.randint(1, 10)
                print("\nYou will play: " + shapename + '\n')
                print("\nRadius of CIRCLE: {} cm ".format(radius))
                print("Value of Pi = 3.14")
                answer_list = input_answers()
                peri = answer_list[0]
                area = answer_list[1]
                circle = Circle(r, shapename, select, username, peri, area, radius)
                circle.process_data()
        print('Total score of {} : {}'.format(username, select[username]))

        error_game_end = True
        while error_game_end:
            try:
                print("=========================================================")
                print("|[1] Continue playing      [2] Go to the main menu      |")
                print("=========================================================")
                play_more = int(input("Enter your choice: "))
            except ValueError:
                print("You have to enter a valid integer value for this option.. Please try again")
                continue
            else:
                error_game_end = False
        if (play_more==1):
            game(select, username)
        elif(play_more==2):
            menu(select)
        else:
            print('Invalid option.. Quitting application\n')
            quit()


def menu(select):
    error_select = True
    while error_select:
        try:
            print("=========================================================")
            print("|                   Shapes Game                         |")
            print("=========================================================")
            print("|Please select option.                                  |")
            print("---------------------------------------------------------")
            print("|[1] User Registration    [2] Show Score     [3] Quit   |")
            print("=========================================================")
            choice = int(input("Enter your option: "))
        except ValueError:
            print("Invalid entry. Select option [1-3].. Please try again.")
            continue
        else:
            error_select = False
    if(choice == 1):
        username = input("Enter your Name: ")
        user1 = user(username, select)
        error_choice1 = True
        while error_choice1:
            try:
                print("==============================")
                print("|What would you like to do?  |")
                print("==============================")
                print("| [1] Start to Play          |")
                print("| [2] Quit                   |")
                print("==============================")
                selection = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid entry. Select option [1-2].. Please try again.")
                continue
            else:
                error_choice1 = False
        if(selection==1):
            game(select, username)
        elif(selection==2):
            quit()
        else:
            print("Invalid entry...TRY AGAIN\n")
            menu(select)
    elif(choice==2):
        ShowScore(select)
        quit()
    elif(choice==3):
        quit()
    else:
        print("Invalid choice. Please try again.\n")
        menu(select)



if __name__ == "__main__":
    main()
