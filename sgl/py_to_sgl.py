from .eval import eval as sgl_eval
from .types import Symbol, ClassDefinition, ClassInstance, String
from ._class import _class

py_exec = exec

def _import(args, env):
    library = sgl_eval(args[0], env)
    if not Symbol('pytosgl') in env.vars.keys():
        env.vars[Symbol('pytosgl:imports')] = String("")
    imports_var: String = env.vars[Symbol('pytosgl:imports')]
    imports_var.value += library + "\n"

def get_import_var(env):
    return env.vars[Symbol('pytosgl:imports')]

def _new_py_class(args, env):
    class_name = sgl_eval(args[0], env)
    module_name = sgl_eval(args[1], env)
    module = __import__(module_name)
    class_ = getattr(module, class_name)
    return class_()

def _instance_call(args, env):
    instance = env.vars[args[0]]
    func_name = sgl_eval(args[1], env)
    arguments = []
    for arg in args[2:]:
        arguments.append(sgl_eval(arg, env))
    func = getattr(instance, func_name)
    return func(arguments)

def _instance_set_prop(args, env):
    instance = env.vars[args[0]]
    property_name = sgl_eval(args[1], env)
    value = sgl_eval(args[2], env)
    setattr(instance, property_name, value)

PY_TO_SGL_FUNCS = {
    Symbol('pytosgl:import'): _import,
    Symbol('pytosgl:new-py-class'): _new_py_class,
    Symbol('pytosgl:instance-call'): _instance_call,
    Symbol('pytosgl:instance-set-prop'): _instance_set_prop
}