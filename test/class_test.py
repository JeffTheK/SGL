from sgl.eval import eval_string
from sgl.stdlib import STD_ENV
from sgl.types import Symbol, ClassDefinition, ClassInstance

def setup_env():
    env = STD_ENV
    eval_string('(class Person name age)', env)
    return env

def test_class():
    env = STD_ENV
    eval_string('(class Person name age)', env)
    definition: ClassDefinition = env.vars[Symbol('Person')]
    assert(definition.name == 'Person')
    assert(definition.var_names == ['name', 'age'])
    assert(Symbol('new-person') in env.funcs.keys())

def test_new():
    env = setup_env()
    eval_string('(new-person john "John" 21)', env)
    instance: ClassInstance = env.vars[Symbol('john')]
    assert(instance.name == Symbol('john'))
    assert(instance.vars['name'].value == 'John')
    assert(instance.vars['age'].value == 21)

def test_get_field():
    env = setup_env()
    eval_string('(new-person john "John" 21)', env)
    assert(eval_string('(get-field name john)', env).value == "John")

def test_set_field():
    env = setup_env()
    eval_string('(new-person john "John" 21)', env)
    eval_string('(set-field age john 30)', env)
    assert(eval_string('(get-field age john)', env) == 30)