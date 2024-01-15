#!/usr/bin/env python3
import console

command_interpreter = console.HBNBCommand()
return_value = command_interpreter.cmdloop()
if return_value:
    print(f"Command interpreter exited successfully: {return_value}")
else:
    print(f"Command interpreter exited with an error: {return_value}")