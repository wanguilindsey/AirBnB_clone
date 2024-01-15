#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_argument(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [k.strip(",") for k in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [k.strip(",") for k in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [k.strip(",") for k in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the class.

    Attributes:
        prompt: The command prompt.
        classes: Set of available classes.
    """
    prompt = "(hbnb) "
    classes = {
            "BaseModel", "User", "State", "City", "Place", "Amenity", "Review"
            }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid."""
        command_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in command_dict:
                    call = "{} {}".format(arg_list[0], command[1])
                    return command_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        arg_list = parse_argument(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg_list[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on class name and id."""
        arg_list = parse_argument(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        arg_list = parse_argument(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representations of
        instances based or not on the class name."""
        arg_list = parse_argument(arg)
        if arg_list and arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances_list = [obj.__str__() for obj in storage.all().values()
                              if not arg_list or
                              arg_list[0] == obj.__class__.__name__]
            print(instances_list)

    def do_count(self, arg):
        """Retrieves the number of instances of a class."""
        arg_list = parse_argument(arg)
        count = sum(1 for obj in storage.all().values() if arg_list
                    and arg_list[0] == obj.__class__.__name__)
        print(count)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute."""
        arg_list = parse_argument(arg)
        obj_dict = storage.all()

        if not arg_list:
            print("** class name missing **")
            return False
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__:
                val_type = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = val_type(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            for i, j in eval(arg_list[2]).items():
                if i in obj.__class__.__dict__ and \
                        type(obj.__class__.__dict__[i]) in {str, int, float}:
                    val_type = type(obj.__class__.__dict__[i])
                    obj.__dict__[i] = val_type(j)
                else:
                    obj.__dict__[i] = j
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
