#!/usr/bin/python3
"""Our Console that contains the entry point of the command interpreter"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "
    file = None

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[1]:
                all_objs = storage.all()
                for key in all_objs.keys():
                    objs = all_objs[key]
                    if objs.id == args[1]:
                        print(objs)
                        break
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                for key in all_objs.keys():
                    objs = all_objs[key]
                    if objs.id == args[1]:
                        del all_objs[key]
                        storage.save()
                        break
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        if arg == 'BaseModel' or not arg:
            all_objs = storage.all()
            lis = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                lis.append(str(obj))
            print(lis)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
        adding or updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                all_objs = storage.all()
                for key in all_objs.keys():
                    objs = all_objs[key]
                    if objs.id == args[1]:
                        setattr(objs, args[2], args[3][1:-1])
                        break
                    else:
                        print("** no instance found **")

    def do_EOF(self, line):
        """When pushing a EOF"""
        return True

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


def separarArgs(arg):
    """separamos la linea leida en string separados"""
    argumentos = arg.split()
    return argumentos


if __name__ == '__main__':
    HBNBCommand().cmdloop()
