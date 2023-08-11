#!/usr/bin/python3
""" The console that represents the frontend of the App """
import cmd
from models.base_model import BaseModel
from models import storage


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
        """Prints the string representation
        of an instance based on the class name and id
        """
        if arg:
            arg1 = arg.split()[0]
            if arg1 not in self.classes.keys():
                print("** class doesn't exist **")
                return
            if len(arg.split()) > 1:
                key = arg1 + '.' + arg.split()[1]
                objects = storage.all()
                if key in objects.keys():
                    print(objects[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")
            return
    def do_destroy(self, arg):
        """
            Deletes an instance based on 
            the class name and id
        """
        if arg:
            arg1 = arg.split()[0]
            if arg1 not in self.classes.keys():
                print("** class doesn't exist **")
                return
            if len(arg.split()) > 1:
                key = arg1 + '.' + arg.split()[1]
                objects = storage.all()
                if key in objects.keys():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")
            return

    def do_all(self, arg):
        """Prints all string representation of all instances 
            based or not on the class name
        """
        if arg:
            if arg not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                emptyList = []
                for key, value in storage.all().items():
                    if arg in key:
                        emptyList.append(str(value))
                print(emptyList)
        else:
            emptyList = []
            for value in storage.all().values():
                emptyList.append(str(value))
                print(emptyList)

    def do_update(self, arg):
        """
        Updates an instance based on the class name 
        and id by adding or updating attribute
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
