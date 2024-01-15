#!/usr/bin/env python3
"""Command line Interpreter like shell in c"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    exit(1)
