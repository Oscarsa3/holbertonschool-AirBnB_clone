#!/usr/bin/python3
"""Our Console that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "
    file = None

    def do_EOF(self, line):
        """When pushing a EOF"""
        return True

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
