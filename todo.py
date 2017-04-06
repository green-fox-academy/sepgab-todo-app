import sys

class Controller():

    def arg_reader(self):
        self.list_argv = []
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

        if len(self.list_argv) == 0:
            display.usage_print()
        else:
            pass
#        	if( arguments[0] == '-l' ):
#        		print('Addolunk ilyet', arguments[1])


class Functions():
    pass






class Display():

    def usage_print(self):
        print('Python Todo application\n ======================= \n \n Command line arguments: \n')
        print(' -l   Lists all the tasks')
        print(' -a   Adds a new task')
        print(' -r   Removes an task')
        print(' -c   Completes an task')

controller = Controller()
display = Display()

controller.arg_reader()
