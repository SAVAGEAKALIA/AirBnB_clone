#!/usr/bin/env python3
"""Command line Interpreter like shell in c"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

                if class_name not in ["BaseModel"]:  # Adjust the list if you have more classes
                    print(class_name)
                    print("** class doesn't exist **")
                else:
                    # Now you have the correct class name, proceed with creating the instance
                    new_instance = BaseModel()
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

                if class_name not in ["BaseModel"]:
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

                if class_name not in ["BaseModel"]:
                    print("** class doesn't exist **")
                else:
                    if len(args_list) < 2:
                        print("** instance id missing **")
                    else:
                        class_id = args_list[1]

                        if class_id not in storage.all():
                            print("** no instance found **")
                        else:
                            # Call your Storage function if available
                            storage = FileStorage()

                            # create a key to link class_name and class_id
                            key = f"{class_name}.{class_id}"
                            # Try to find the instance in the storage
                            instance = storage.all().get(key, None)

                            if instance is None:
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

                if class_name not in ["BaseModel"]:
                    print("** class doesn't exist **")
                else:
                    storage = FileStorage()
                    instances = storage.all()  # Assuming storage is an instance of your storage class
                    for key, instance in instances.items():
                        print("[[{}] ({}) {}".format(instance.__class__.__name__, instance.id, str(instance.__dict__)))

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

                if class_name not in ["BaseModel"]:
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
