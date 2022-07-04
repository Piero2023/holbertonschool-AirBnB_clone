#!/usr/bin/python3
'''
HBNBCommand - console for the airbnb clone
'''

import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_quit(self, argum):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, argum):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Method called when an empty line is entered in response to the request
        """
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()

