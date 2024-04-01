#!/usr/bin/env python3
"""Command line Interpreter like shell in c"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

valid_classes = ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]


def count_instances(class_name, storage = FileStorage()):
    """Counts the number of instances of a given class in the storage."""
    instances = storage.all()
    count = 0
    for instance in instances.values():
        if instance.__class__.__name__ == class_name:
            count += 1
    return count


class HBNBCommand(cmd.Cmd):
    """AirBnb Command line interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ Signals end of File """
        if not line.strip():
            return True

    def do_help(self, arg):
        """ Signals sent for help """
        cmd.Cmd.do_help(self, arg)

    def do_quit(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        if args is None:
            print("** class name missing **")
        else:
            args_list = args.split()

            if not args_list:
                print("** class name missing **")

            else:
                class_name = args_list[0]

                if class_name not in valid_classes:
                    # Adjust the list if you have more classes
                    print(class_name)
                    print("** class doesn't exist **")
                else:
                    # Now you have the correct class name
                    # proceed with creating the instance
                    new_instance = globals()[class_name]()
                    new_instance.save()
                    print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        storage = FileStorage()

        if args is None:
            print("** class name missing **")
        else:
            args_list = args.split()

            if not args_list:
                print("** class name missing **")
            else:
                class_name = args_list[0]

                if class_name not in valid_classes:
                    print(class_name)
                    print("** class doesn't exist **")
                else:
                    if len(args_list) < 2:
                        print("** instance id missing **")
                    else:
                        class_id = args_list[1]

                        instance = storage.all()

                        key = f"{class_name}.{class_id}"

                        if key not in instance:
                            print(class_id)
                            print("** no instance found **")
                        else:
                            inst = instance[key]
                            # Print the string representation of the instance
                            print(inst)

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        storage = FileStorage()

        if args is None:
            print("** class name missing **")
        else:
            args_list = args.split()

            if not args_list:
                print("** class name missing **")
            else:
                class_name = args_list[0]

                if class_name not in valid_classes:
                    print("** class doesn't exist **")
                else:
                    if len(args_list) < 2:
                        print("** instance id missing **")
                    else:
                        class_id = args_list[1]
                        instance = storage.all()
                        key = f"{class_name}.{class_id}"

                        if key not in instance:
                            print("** no instance found **")
                        else:
                            # Call your Storage function if available
                            storage = FileStorage()

                            # create a key to link class_name and class_id
                            key = f"{class_name}.{class_id}"
                            # Try to find the instance in the storage
                            instance = storage.all()

                            if instance[key] is None:
                                print("** no instance found **")
                            else:
                                del storage.all()[key]
                                storage.save()
                                print("Instance deleted successfully.")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        if args is None:
            print("** class name missing **")
        else:
            args_list = args.split()

            if not args_list:
                print("** class name missing **")
            else:
                class_name = args_list[0]

                if class_name not in valid_classes:
                    print("** class doesn't exist **")
                else:
                    storage = FileStorage()
                    instances = storage.all()
                    # Assuming storage is an instance of your storage class
                    for key, instance in instances.items():
                        ins_nm = instance.__class__.__name__
                        ins_id = instance.id
                        ins_dic = str(instance.__dict__)
                        print("[[{}] ({}) {}".format(ins_nm, ins_id, ins_dic))

    @staticmethod
    def count(self):
        """
        Counts the number of instances of the User class
        """
        storage = FileStorage()
        instance_all = storage.all()

        count = 0
        for key, obj in instance_all.items():
            if isinstance(obj, User):
                count += 1
        return count

    def do_count(self, args):
        """Calls the classmethod count with the current class or handles User.count() syntax."""
        if not args:  # No arguments, treat as User.count() syntax
            try:
                # Extract class name from self.__class__.__name__ (assuming HBNBCommand inherits from it)
                class_name = self.__class__.__name__.split(".")[1]
                print(HBNBCommand.count(self.__class__, class_name))
            except (AttributeError, IndexError):
                print("** Unknown syntax or class name not found **")
        else:
            # Existing functionality for do_count with arguments
            args_list = args.split()
            if not args_list:
                print("** class name missing **")
            else:
                class_name = args_list[0]
                storage = FileStorage()
                instance_all = storage.all()
                count = 0
                for dict in instance_all.values():
                    inst_cls = dict.__class__.__name__
                    if inst_cls == class_name:
                        count += 1
                print(count)

    def do_update(self, args):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        storage = FileStorage()
        if args is None:
            print("** class name missing **")
        else:
            args_list = args.split()

            if not args_list:
                print("** class name missing **")
            else:
                class_name = args_list[0]

                if class_name not in valid_classes:
                    print("** class doesn't exist **")
                else:
                    if len(args_list) < 2:
                        print("** instance id missing **")
                    else:
                        class_id = args_list[1]

                        instance = storage.all()

                        key = f"{class_name}.{class_id}"

                        if key not in instance:
                            print("** no instance found **")
                        else:
                            if len(args_list) < 3:
                                print("** attribute name missing **")
                            else:
                                attribute_name = args_list[2]

                                if len(args_list) < 4:
                                    print("** value missing **")
                                else:
                                    attribute_value = args_list[3]

                                    instance_to_update = instance[key]

                                    setattr(instance_to_update, attribute_name, attribute_value)
                                    storage.save()
                                    print("Updated successfully")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
