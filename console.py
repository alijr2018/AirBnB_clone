#!/usr/bin/python3
"""
Module: console.py
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program gracefully at EOF"""
        print("")  # Print a new line before exiting
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objs = storage.all()
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        objs = storage.all()
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances or instances of a specific class"""
        args = arg.split()
        objs = storage.all()
        if not args:
            print([str(obj) for obj in objs.values()])
            return
        if args[0] in storage.classes.keys():
            filtered_objs = [str(obj) for key,
                             obj in objs.items() if key.startswith(args[0])]
            print(filtered_objs)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        objs = storage.all()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
