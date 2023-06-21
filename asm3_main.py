"""
This is supporting modules with functions:
    - Modules to creat Menu of Assigment
    - Iterable menu for assignment
Date created: 14-Nov-2022
Originator: anhvtFX17909
<This code/ method has core AVL code referred from the lecture of Mr. Samaksh Namdev Drum
                          www.instagram.com/samaksh_namdev>

-----------------------------------------------------------------------------------------------------------------
Brief assignment:
The processing of data is following this way:
1. Data is loaded from file asm3_data.csv >>
2. Load data to BST >>
3. Solve all requirements by DFS and BFS
-----------------------------------------------------------------------------------------------------------------
"""

import time
import os.path
from asm3_file import *
from asm3_core import AVLTree

# import queue

#   Get the path to current directory
cw_dir = os.getcwd()


class AsmMenu:
    def __init__(self):
        #   Data shall be initiated the BST from file
        self.avltree_data = AVLTree()

    def read(self, file):
        print('!Note: The assigment needs to load the dataset from file asm3_data.csv\n'
              'If you do not enter the path to access the file, the data file shall be '
              'loaded in this current directory as default')
        load_option = ask('Did you keep the dataset in the same location of this assigment? (y/N)')

        if load_option:
            f = File(os.getcwd() + '/' + file)
        else:
            # start the file path validity check
            while True:
                file_path = input('Please fill the file path to access product dataset: ')
                if os.path.exists(file_path):
                    print(f'File {file_path} is found')
                    f = File(file_path)
                    break
                else:
                    print('Error! File path is invalid. Please try again')
        display_data(f.f_read())

        return f.f_read()

    def save_data(self, file, data):
        f = File()
        save_action = ask('Do you want to save the data? y/N: ')
        if save_action:
            save_option = ask('Do you want to keep the dataset in the same location? (y/N)')
            if save_option:
                f.f_write(os.getcwd() + '/' + file, data)  # save to current location
                print('Record data to file asm2_result.csv successfully!')
            else:  # save to different location
                while True:
                    location = input('Please fill the file path to save product dataset: ')
                    if os.path.dirname(location):
                        print(f'File {location} is found')
                        f.f_write(location + '/' + file, data)
                        print('Record data to file asm3_result.csv successfully!')
                        break
                    else:
                        print('Error! File path is invalid. Please try again')
        else:
            print('Not saving! Return to main menu')
            return

    def main_menu(self):
        """
        input: None
        :return: display main menu of program with m_num is the menu option item
        """
        m_list = {
            1: 'Load the data from file',
            2: 'Insert a new person',
            3: 'In-order traversal',
            4: 'Breadth-First traversal',
            5: 'Search by Person ID',
            6: 'Delete by Person ID',
            0: 'Exit Program'
        }
        #   Title Bar
        print('')
        print('-' * 40)
        print(' ' * 12, 'Assigment #3')
        print(' ' * 7, 'Originator: anhvtFX17079')
        print(' ' * 10, 'Date: 14 Nov 2022')
        print(' ' * 1, '<This assignment is tested on Python3>')
        print('*This code/ method has core AVLTree referred \n'
              'from the lecture of Mr. Samaksh Namdev Drum\n'
                          'www.instagram.com/samaksh_namdev*')
        print('-' * 40)

        #   Loop the Menu List then return the value to loop the Menu
        #   Getting the value 10 is to exit the Program
        for i in range(len(m_list)):
            # Adjust the left and right of Main Menu
            item = '{0:1} {1:>2} {2:1} {3:>0}'.format('|', list(m_list.keys())[i], '.', list(m_list.values())[i])
            n = 40 - (len(list(item)) + 2)
            print(item, ' ' * n, '|')
        print('-' * 40)

        #   Choose the section to start the work, capture error during fill the values
        while True:
            try:
                m_num = int(input('Please choose the section to perform task: '))
                if m_num in m_list.keys():
                    return m_num
                    break
                else:
                    print('Error: This section value is not available! Please choose again')
            except ValueError:
                print('Error: This section value is not available! Please choose again')
        print('-' * 50)

    # Load data from file then display
    def task1(self):
        print('.' * 50)
        print('Start reading file and loading dataset:\n')
        print('Loading to AVLTreee')
        data_in = self.read('asm3_trial.csv')

        for i in data_in:
            self.avltree_data.insert(i)
        print('load data to AVLTree successfully......')

    # Add new data to stack then display
    def task2(self):
        print('.' * 50)
        print('Start insert new member to data:')
        print('!Note: Please insert the ID in integer')
        ids = self.__id_exist_check__()
        #   After check the id is "interger and not existed", the additional work is on going
        if ids > 0:
            name = input('Please enter the new person" s name:')
            birth_place = input('Please enter the new person"s birth place: ')
            dob = input('Please enter the new person"s date of birth: ')
            new_data = [ids, name, birth_place, dob]
            self.avltree_data.insert(new_data)

    def __get_id__(self):
        while True:  # check the id must be in integer!!
            try:
                new_id = int(input('Please enter the person id: '))
                break
            except ValueError:
                print('Error! you need to enter the id in integer value!')
        return new_id

    def __id_exist_check__(self):
        new_id = self.__get_id__()
        id_check = self.avltree_data.search(new_id)
        if id_check:
            c = ask('Error: This ID is existed, do you want to try again? (y/N): ')
            if c:
                while True:
                    new_id_rev = self.__get_id__()
                    if not self.avltree_data.search(new_id_rev):  # loop until the not exist value is found
                        break
                    else:
                        print('Existed: Please try again')
                return new_id_rev
            else:
                return -1
        else:
            return new_id

    # Display data from stack
    def task3(self):
        print('.' * 50)
        print('In order traversal:\n')
        print('{:<8}{:<30}{:<20}{:<10}'.format('ID', 'Name', 'DOB', 'Birth Place'))
        self.avltree_data.inoder_traversal()

    def task4(self):
        print('.' * 50)
        print('Breadth Depth Traversal\n')
        self.avltree_data.bfs_traversal()

    def task5(self):
        print('.' * 50)
        print('Seaching task:')
        while True:  # check the quantity must be in integer!!
            try:
                id01 = int(input('Please enter the person id: '))
                break
            except ValueError:
                print('Error! you need to enter the person id in integer')

        self.avltree_data.search(id01)

    def task6(self):
        print('.' * 50)
        print('Deletion task')
        while True:  # check the quantity must be in integer!!
            try:
                id02 = int(input('Please enter the person id: '))
                break
            except ValueError:
                print('Error! you need to enter the person id in integer')

        find_id = self.avltree_data.search(id02)
        if find_id:
            self.avltree_data.remove(id02)
            print('Delete this person info successfully.......')

    def menu_loop(self):
        # User can choose the options to load the dataset:
        #   1/ If user do not enter the path, the default location of dataset is at the same directory
        #   2/ If user enter the path, the program shall check the validity of path then proceed.

        #   Start assigment environment
        m = self.main_menu()

        while True:
            if m == 1:
                self.task1()
                m = self.main_menu()
            elif m == 2:
                self.task2()
                m = self.main_menu()
            elif m == 3:
                self.task3()
                m = self.main_menu()
            elif m == 4:
                self.task4()
                m = self.main_menu()
            elif m == 5:
                self.task5()
                m = self.main_menu()
            elif m == 6:
                self.task6()
                m = self.main_menu()
            elif m == 0:
                quit_action = ask('Do you really want to quit assignment? (y/N): ')
                if quit_action:
                    print('Exiting program', end=' ')
                    for i in range(5):
                        time.sleep(0.1)
                        print('........', end='.')
                    print('\nThank you for checking my assignment!')
                    quit()
                else:
                    print('Return to main menu!')
                    m = self.main_menu()


# This code is copyright from doc.python.org for this assignment
def ask(prompt, retries=4):
    while True:
        check = input(prompt)
        if check in ('y', 'ye', 'yes', 'Y'):
            return True
        if check in ('n', 'no', 'nop', 'nope', 'N'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('Exit Program')


def display_data(data):
    print('{:<8}{:<30}{:<20}{:<10}'.format('ID', 'Name', 'DOB', 'Birth Place'))
    for i in data:
        print('{:<8}{:<30}{:<20}{:<10}'.format(i[0], i[1], i[2], i[3]))
    print('>>>>>>>>>>>>>> End Of Dataset <<<<<<<<<<<<<<<<')


if __name__ == '__main__':
    asm3_menu = AsmMenu()
    asm3_menu.menu_loop()
