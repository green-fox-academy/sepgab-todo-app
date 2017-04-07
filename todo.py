import sys
import os
from termcolor import colored, cprint

class Controller():

    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.manager()

    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

    def manager(self):
        if len(self.list_argv) == 0:
            display.usage_print()
        else:
            if self.list_argv[0] == '-h':
                display.usage_print()
            else:
                model.db_opener()
                if model.auth == True:
                    if self.list_argv[0] == '-l':
                        display.list_printer()
                    elif self.list_argv[0] == '-c':
                        if len(self.list_argv) == 1:
                            display.error_missing_arg()
                        else:
                            model.db_checker(self.list_argv[1])
                            model.db_updater()
                            display.list_printer()
                    elif self.list_argv[0] == '-a':
                        if len(self.list_argv) == 1:
                            display.error_missing_arg()
                        else:
                            model.db_adder(' '.join(self.list_argv[1:]))
                            display.list_printer()
                    elif self.list_argv[0] == '-e':
                        model.db_eraser()
                        display.list_eraser()
                    elif self.list_argv[0] == '-r':
                        if len(self.list_argv) == 1:
                            display.error_missing_arg()
                        else:
                            model.db_remover(self.list_argv[1])
                            model.db_updater()
                            display.list_printer()
                    else:
                        display.error_argument()
                        display.usage_print()

class Model():

    def __init__(self):
        self.task_list_raw = []
        self.task_list = []
        self.auth = False

    def db_opener(self):
        self.user_name = input('Please enter your user name: ')
        self.password = input('Password: ')
        try:
            self.file = open(str(self.user_name)+'.txt', 'r+')
        except FileNotFoundError:
            self.file = open(str(self.user_name)+'.txt', 'w')
            self.file.write(str(self.password) + '\n')
            display.print_db_inited()
        self.file.close()
        self.file = open(str(self.user_name)+'.txt', 'r+')
        if self.file.readline().rstrip() == self.password:
            self.task_list.append(self.password)
            self.task_list_raw = self.file.readlines()
            for task in self.task_list_raw:
                self.task_list.append(task.split('|||'))
            self.auth = True
        else:
            display.error_user()

    def db_adder(self, task_to_add):
        self.task_list.append(['0', str(task_to_add) + '\n'])
        self.file.write('0'+'|||'+str(task_to_add) + '\n')
        self.file.close()

    def db_eraser(self):
        self.eraser = input('Are you sure? (Y/N) ')
        if self.eraser == 'Y':
            self.file.close()
            self.file = open(str(self.user_name)+'.txt', 'w')
            self.file.write(self.password + '\n')
            self.file.close()

    def db_checker(self, num):
        try:
            self.task_list[int(num)][0] = '1'
        except IndexError:
            display.error_index()
        except ValueError:
            display.error_value()

    def db_updater(self):
        self.file.close()
        self.file = open(str(self.user_name)+'.txt', 'w')
        self.file.write(self.password + '\n')
        for i in range(1, len(self.task_list)):
            self.file.write(self.task_list[i][0] + '|||' + self.task_list[i][1])
        self.file.close()
        return self.task_list

    def db_remover(self, num):
        try:
            self.task_list.remove(self.task_list[int(num)])
        except IndexError:
            display.error_index()
        except ValueError:
            display.error_value()

class Display():

    def __init__(self):
        self.not_checked = '[ ] '
        self.checked = '[X] '

    def usage_print(self):
        cprint(' Python Todo application\n ======================= \n \n Command line arguments: \n', 'yellow')
        cprint(' -h   Help on command line arguments.', 'yellow')
        cprint(' -l   Lists all the tasks', 'yellow')
        cprint(' -a   Adds a new task', 'yellow')
        cprint(' -r   Removes a task. Enter task number.', 'yellow')
        cprint(' -c   Completes a task. Enter task number.', 'yellow')
        cprint(' -e   Empty task list', 'yellow')

    def list_printer(self):
        if len(model.task_list) == 1:
            cprint('No todos for ' + str(model.user_name) + '!', 'white', 'on_blue')
        else:
            cprint('\nThings to do for ' + str(model.user_name) + ':', 'white', 'on_blue')
            for i in range(len(model.task_list)):
                if model.task_list[i][0] == '0':
                    print(str(i) + ' - ' + self.not_checked + model.task_list[i][1][:-1])
                elif model.task_list[i][0] == '1':
                    print(str(i) + ' - ' + self.checked + model.task_list[i][1][:-1])
                else:
                    pass

    def list_eraser(self):
        if model.eraser == 'Y':
            print('List successfully erased.')
        else:
            print('Exit without erasing.')

    def error_argument(self):
        cprint('\nUnsupported argument. \n', 'red')

    def error_missing_arg(self):
        cprint('\nUnable to perform: no task provided. \n', 'red')

    def error_index(self):
        cprint('\nUnable to perform: index is out of bound. \n', 'red')

    def error_value(self):
        cprint('\nUnable to perform: index is not a number. \n', 'red')

    def error_user(self):
        cprint('\nWrong password.\n', 'red')

    def print_db_inited(self):
        cprint('\nTask list successfully created.\n', 'green')

display = Display()
model = Model()
controller = Controller()
