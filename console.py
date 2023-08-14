#!/usr/bin/python3
"""
Module: console.py
 a program called console.py that contains,
 the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

valid_classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State,
}


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = '(hbnb)  '

    def do_EOF(self, line):
        """Exits console"""
        print()
        return (True)

    def do_quit(self, line):
        """Quit command to exit the program (Ctrl-D)"""
        print()
        return (True)

    def help_quit(self):
        """when two arguments involve"""
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        """ overwriting the emptyline method """
        pass

    def do_create(self, line):
        """Creates a new instances of a class"""
        if line:
            try:
                glo_cls = globals().get(line, None)
                obj = glo_cls()
                obj.save()
                print(obj.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """print <class name> <id>"""
        arr = line.split()

        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in valid_classes:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[new_str])

    def do_destroy(self, line):
        """Destroy command deletes an instance based on the class name and id
        """
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in valid_classes:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(new_str)
                storage.save()

    def do_all(self, line):
        """ Print all instances in string representation """
        objects = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            st = line.split(" ")
            if st[0] not in valid_classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == st[0]:
                        objects.append(str(value))
                print(objects)

    def do_update(self, line):
        """Update an instance based on the class name and id."""
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
            return
        elif arr[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        elif len(arr) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
                return
            elif len(arr) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], arr[2], arr[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
