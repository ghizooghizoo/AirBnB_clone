#!/usr/bin/python3
""" The console that represents the frontend of the App """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Define the command interpreter"""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

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

    def do_create(self, arg):
        """Create instance of a specific class"""
        if arg:
            argv = arg.split()
            if len(argv) == 1:
                if arg in self.classes.keys():
                    instance = self.classes[arg]()
                    instance.save()
                    print(instance.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
