#!/usr/bin/python3
""" The console that represents the frontend of the App """
import cmd


class HBNBCommand(cmd.Cmd):
    """Define the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        exit()

    def emptyline(self):
        """pass when emptyline entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
