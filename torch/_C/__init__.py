__all__ = []

from torch_shim import js_global_shim 

def export(obj):
    __all__.append(obj.__name__)
    return obj

@export
def _initExtension(*args):
    pass
@export
def _get_cpp_backtrace(*args):
    pass
@export
def _rename_privateuse1_backend(*args):
    pass
@export
def _has_torch_function(*args):
    pass
@export
def _has_torch_function_unary(*args):
    pass
@export
def _has_torch_function_variadic(*args):
    pass
@export
def _has_compatible_shallow_copy_type(*args):
    pass
@export
def _add_docstr(*args):
    class DS:
        def __init__(self):
            self.__module__ = None
    return DS()
@export
def _push_on_torch_function_stack(*args):
    pass
@export
def _pop_torch_function_stack(*args):
    pass
@export
def _get_function_stack_at(*args):
    pass
@export
def _len_torch_function_stack(*args):
    pass
@export
def _is_torch_function_mode_enabled(*args):
    pass
@export
def _from_dlpack(*args):
    pass
@export
def _to_dlpack(*args):
    pass

@export
def _disabled_torch_dispatch_impl(*args):
    pass
@export
def _infer_size(*args):
    pass
@export
def _autograd_init():
    return True

@export
def __getattr__(name):
    if name in js_global_shim:
        return js_global_shim[name]
    def f(*args):
        pass
    return f

class _TensorBaseMeta(type):
    def __getattr__(self, name):
        def f(*args):
            pass
        return f

class _TensorBase(metaclass=_TensorBaseMeta):
    def __init__(self):
        pass
    def __getattr__(self, name):
        def f(*args):
            pass
        return f

class _NN(object):
    def __getattr__(self, name):
        def f(*args):
            pass
        return f
_nn = _NN()
__all__.append("_nn")
class _VFClass(object):
    def __getattr__(self, name):
        def f(*args):
            pass
        return f
_VF = _VFClass()
__all__.append("_VF")

@export
class dtype:
    def __init__(self, name):
        self.name = name

float32 = dtype('float32')
__all__.append('float32')

@export
class device:
    pass
@export
class qscheme:
    pass
@export
class Size:
    pass
@export
class layout:
    pass
@export
class DispatchKey:
    Python = None
DispatchKey.Python = DispatchKey()

@export
class StorageBase:
    pass

@export
class Generator:
    def set_state(*args):
        pass
    def get_state(*args):
        pass
    def manual_seed(*args):
        pass
    def initial_seed(*args):
        pass
    def seed(*args):
        pass
    def device(*args):
        pass

default_generator = Generator()
__all__.append('default_generator')

@export
class ErrorReport:
    def call_stack():
        return ""
    pass

_VariableFunctions = None
__all__.append('_VariableFunctions')

@export
def _disabled_torch_function_impl(*args):
    pass

@export
class _TensorMeta(_TensorBaseMeta):
    pass

@export
class _Await(object):
    pass

@export
class _Future(type):
    pass

@export
class Future(object):
    pass

@export
class ScriptFunction:
    pass

@export
class _LegacyVariableBase:
    pass

@export
class _FunctionBase:
    pass

@export
def _jit_init():
    return True

contiguous_format = True
__all__.append("contiguous_format")

@export
def _jit_get_operation(qualified_op_name):
    class Op:
        def __init__(self):
            self.__module__ = None
    return Op(), []

@export
def _get_operation_overload(qualified_op_name, use_key):
    class Op:
        def __init__(self):
            self.__module__ = None
    return Op(), [], None

@export
def _get_schema(qualified_op_name, use_key):
    class Schema:
        def __init__(self):
            self.overload_name = None
            self.name = 'todo::todo'
            self.arguments = []
    return Schema()
