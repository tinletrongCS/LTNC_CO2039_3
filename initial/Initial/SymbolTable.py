from StaticError import *
from Symbol import *
from functools import *

# function for validate correct variable name format
def __valid_var_name(name: str) -> bool:
    return (
        name != "" and
        name[0] >= 'a' and name[0] <= 'z' and
        all(c.islower() or c.isupper() or c.isdigit() or c == '_' for c in name[1:]) 
    )

# function for validate correct data type
def __valid_data_type(type: str) -> bool:
    if type == "string" or type == "number":
        return True
    else:
        return False
    
def simulate(list_of_commands):
    return process_commands(list_of_commands, [[]], [])

def process_commands(commands, symtab, result):
    if not commands:
        if len(symtab) > 1:
            return result + [str(UnclosedBlock(len(symtab) - 1))]
        return result
    
    command,  *rest = commands

    # No idea here @@
    try:
        new_symtab, output = handle_command(command, symtab)
        return process_commands(rest, new_symtab, result + ([output] if output else []))
    except StaticError as e:
        return [str(e)]

# function for processing single command call to the correct function
def handle_command(command: str, symtab: list[list[Symbol]]):
    tokens = command.strip().split()
    COMMAND = tokens[0]
    
    if COMMAND == "INSERT":
        return handle_insert(command, symtab)
    elif COMMAND == "ASSIGN":
        return handle_assign(command, symtab)
    elif COMMAND in ["BEGIN", "END"]:
        return handle_begin_end(command, symtab)
    elif COMMAND == "LOOKUP":
        return handle_lookup(command, symtab)
    elif COMMAND == "PRINT":
        return handle_print(command, symtab)
    elif COMMAND == "RPRINT":
        return handle_rprint(command, symtab)
    else:
        raise InvalidInstruction(command)
    
# function for handling INSERT
def handle_insert(command: str, symtab: list[list[Symbol]]):
    tokens = command.strip().split()
    if len(tokens) != 3:
        raise InvalidInstruction(command) # Incorrect syntax
    
    _, name, typ = tokens

    # Checking for valid variable name and data type
    if not __valid_var_name(name) or not __valid_data_type(typ):
        raise InvalidInstruction(command) # Incorrect syntax

    # Redeclared error
    if any(sym.name == name for sym in symtab[-1]):  # Only search in current scope 
        raise Redeclared(command)
    
    new_block = symtab[-1] + [Symbol(name, typ)]
    new_symtab = symtab[:-1] + [new_block]
    
    return new_symtab, "success"

# Helper functions for ASSIGN
# Validate constant format
def __valid_const_format(value: str) -> bool:
    return (
        # Int constant
        all(c in '0123456789' for c in value) # Int constant

        # String constant
        or (
            len(value) >= 2 and
            value[0] == "'" and
            value[-1] == "'" and 
            all (c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for c in value[1:-1])
        )

        # Assigned by another variable
        or (
            __valid_var_name(value)
        )
    )

# function for handling ASSIGN
def handle_assign(command: str, symtab: list[list[Symbol]]):
    tokens = command.strip().split()
    if len(tokens) != 3:
        raise InvalidInstruction(command) # Incorrect syntax
    
    _, name, value = tokens 
    
    if not __valid_var_name(name) or not __valid_const_format(value):
        raise InvalidInstruction(command)
    
    # Undeclared error
    # Tìm biến name đã khai báo trong symbol table
    symbol = next(
        (sym for scope in reversed(symtab) for sym in scope if sym.name == name),
        None
    )
    if symbol is None:
        raise Undeclared(command)
    
    # Nếu value là một biến khác -> phải đc khai báo và đúng kiểu
    if __valid_var_name(value):
        value_sym = next(
            (sym for scope in reversed(symtab) for sym in scope if sym.name == value),
            None
        )
        # Gán từ 1 biến nhưng chưa khai báo biến đó
        if value_sym is None:
            raise Undeclared(command)
        
        # Gán từ 1 biến nhưng không khớp kiểu dữ liệu 
        if value_sym.typ != symbol.typ:
            raise TypeMismatch(command)
    
    # Gán bằng 1 hằng giá trị nhưng không khóp kiểu 
    # TypeMismatch error
    elif value.startswith("'"):
        if symbol.typ != "string":
            raise TypeMismatch(command)
        
    else:
        if symbol.typ != "number":
            raise TypeMismatch(command)

            
    new_block = symtab[-1] + [Symbol(name, value)]
    new_symtab = symtab[:-1] + [new_block]
    
    return new_symtab, "success"

def handle_begin_end(command: str, symtab: list[list[Symbol]]) -> None:
    if command =="BEGIN":
        return symtab + [[]], None
    elif command == "END":
        if len(symtab) == 1: # There only default global scope 
            raise UnknownBlock()
        return symtab[:-1], None
    else:
        raise InvalidInstruction(command)
    
def handle_lookup(command: str, symtab: list[list[Symbol]])->None:
    tokens = command.strip().split()

    if len(tokens) != 2:
        raise InvalidInstruction(command)
    
    _, name = tokens
    if not __valid_var_name(name):
        raise InvalidInstruction(command)
    
    # Tìm mức (level) đầu tiên mà danh hiệu (identifier) xuất hiện trong symbol table (từ ngoài vào trong)
    found = next(
        ((len(symtab) - 1 - i) for i, block in enumerate(reversed(symtab)) if any(sym.name == name for sym in block)),
        None
    )

    if found is None:
        raise Undeclared(command)

    return symtab, str(found)

def handle_print(command: str, symtab: list[list[Symbol]]) -> None:


    return

def handle_rprint(command: str, symtab: list[list[Symbol]]) -> None:

    return

