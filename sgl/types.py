class Atom:
    pass

class Number(Atom):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self) -> str:
        return f"Number {self.value}"
    
    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value

    def __hash__(self) -> int:
        return hash(self.value)

class Symbol(Atom):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f"Symbol {self.name}"
    
    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name

    def __hash__(self) -> int:
        return hash(self.name)

class String(Atom):
    def __init__(self, value) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f"String {self.value}"
    
    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value
    
    def __hash__(self) -> int:
        return hash(self.value)

class List(Atom):
    def __init__(self, elements: list) -> None:
        self.elements = elements
    
    def __repr__(self) -> str:
        return str(self.elements)
    
    def __eq__(self, __o: object) -> bool:
        return self.elements == __o.elements

    def __hash__(self) -> int:
        return hash(self.elements)

class ClassDefinition:
    def __init__(self, name, var_names):
        self.name = name
        self.var_names = var_names

class ClassInstance:
    def __init__(self, definition: ClassDefinition, name: str, vars: dict):
        self.definition = definition
        self.name = name
        self.vars = vars
    
    def __repr__(self) -> str:
        return f"{self.name.name}: {str(self.vars)}"

Exp = (Atom, list)

class Env:
    def __init__(self, vars: dict, funcs: dict) -> None:
        self.vars = vars
        self.funcs = funcs