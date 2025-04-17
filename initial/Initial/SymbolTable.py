from StaticError import *
from Symbol import *
from functools import *

def simulate(list_of_commands):
    return process_commands(list_of_commands, [[]], [])

def process_commands(commands, symtab, result):
    if not commands:
        return result
    
    command,  *rest = commands

    try:
        new_symtab, output = handle_command(command, symtab)
        return process_commands(rest, new_symtab, result + [output])
    except StaticError as e:
        return [str(e)]

# function for processing single command
# call to the correct function
def handle_command(command: str, symtab: list[list[Symbol]]):
    tokens = command.strip().split()
    action = tokens[0]
    
    if action == "INSERT":
        return handle_insert(command, symtab)
    else:
        raise InvalidInstruction(command)
    
# function for handling insertion
def handle_insert(command: str, symtab: list[list[Symbol]]):
    tokens = command.strip().split()
    if len(tokens) != 3:
        raise InvalidInstruction(command) # Không đúng cú pháp
    
    _, name, typ = tokens

    if any(sym.name == name for block in symtab for sym in block):
        raise Redeclared(command)
    
    new_block = symtab[-1] + [Symbol(name, typ)]
    # Tại -1 là block toàn cục 
    new_symtab = symtab[:-1] + [new_block]
    
    return new_symtab, "success"



# function for handling assignment
def handle_assign(command: str, symtab: list[list[Symbol]]):
    tokens = command.strip().split()
    if len(tokens != 3):
        raise InvalidInstruction(command) # Không đúng cú pháp 
    
    _, name, typ = tokens
    return "success"
