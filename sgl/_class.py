from .types import Symbol, ClassDefinition, ClassInstance
from .eval import eval

def _new(env, class_definition: ClassDefinition, instance_name: Symbol, var_values):
    assert(type(instance_name) is Symbol)
    vars = {}
    for i in range(len(class_definition.var_names)):
        var_name = class_definition.var_names[i]
        var_value = var_values[i]
        vars[var_name] = var_value
    instance = ClassInstance(class_definition, instance_name, vars)
    env.vars[instance_name] = instance

def _class(args, env):
    name: str = args[0].name
    var_names = []
    for arg in args[1:]:
        var_names.append(arg.name)
    definition = ClassDefinition(name, var_names)
    env.vars[Symbol(name)] = definition
    env.funcs[Symbol(f'new-{name.lower()}')] = lambda args2, env2, class_def=definition: _new(env2, class_def, args2[0], args2[1:])

def _get_field(args, env):
    field_name = args[0].name
    instance: ClassInstance = eval(args[1], env)
    return instance.vars[field_name]

def _set_field(args, env):
    field_name = args[0].name
    instance: ClassInstance = eval(args[1], env)
    new_value = eval(args[2], env)
    instance.vars[field_name] = new_value

CLASS_FUNCS = {
    Symbol('class'): _class,
    Symbol('get-field'): _get_field,
    Symbol('set-field'): _set_field
}