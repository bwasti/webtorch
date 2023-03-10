class TransformType:
    Grad = None
    Jvp = None
    Vmap = None
    Functionalize = None
TransformType.Grad = TransformType()
TransformType.Jvp = TransformType()
TransformType.Vmap = TransformType()
TransformType.Functionalize = TransformType()

RandomnessType = None
CInterpreter = None
CGradInterpreterPtr = None
CFunctionalizeInterpreterPtr = None
CVmapInterpreterPtr = None
CJvpInterpreterPtr = None
pop_dynamic_layer_stack = None
push_dynamic_layer_stack = None
set_single_level_autograd_function_allowed = None
get_single_level_autograd_function_allowed = None
unwrap_if_dead = None
_wrap_for_grad = None
_unwrap_for_grad = None
current_level = None
_add_batch_dim = None
_remove_batch_dim = None
_vmap_decrement_nesting = None
_vmap_increment_nesting = None
is_batchedtensor = None
_grad_increment_nesting = None
_grad_decrement_nesting = None
_jvp_increment_nesting = None
_jvp_decrement_nesting = None
_wrap_functional_tensor = None
_unwrap_functional_tensor = None
_func_decrement_nesting = None
_func_increment_nesting = None
_assert_wrapped_functional = None
_propagate_functional_input_mutation = None
set_inplace_requires_grad_allowed = None
get_inplace_requires_grad_allowed = None
