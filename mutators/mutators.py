import random


def mutate(module: dict, module_used: str):
    """ Mutate a module and return it.

    Example:
    -------
    service_params = {
        'state': ['started', 'stopped', 'reloaded', 'restarted'],
        'enabled': ['no', 'yes'],
    }

    actual_service = {
        'name': 'ciao',
        'state': 'reloaded',
        'enabled': 'no'
    }

    mutated_module = mutate(actual_service, service_params)


    Return
    ------
        mutated_module: dict - the mutated module
        None: if none of the module's parameters passed in input can be mutated (i.e, is not in module_params)
    """
    # module_list = list(tasks_df['mod_keys_found_string'].unique())  # List of modules
    # module_used = list(set(module_list) & set(module))[0]  # Used module
    module_params = module_parameters[module_used]

    mutable_module_params = set(module.keys()).intersection(set(module_params.keys()))

    if not mutable_module_params:
        return module

    param_to_mutate = random.choice(list(mutable_module_params))
    mutable_param_values = module_params[param_to_mutate]
    #mutable_param_values.remove(module[param_to_mutate])
    mutated_value = random.choice(list(mutable_param_values))

    mutated_module = module
    mutated_module[param_to_mutate] = mutated_value

    return mutated_module


module_parameters = {
    'service': {
        'state': ['started', 'stopped', 'reloaded', 'restarted'],
        'enabled': [False, True],
    },

    'set_fact': {
        'cacheable': [False, True],
    },

    'shell': {
        'stdin_add_newline ': [False, True],
    },

    'command': {
        'stdin_add_newline ': [False, True],
        'strip_empty_ends': [False, True],
        'warn': [False, True],
    },

    'template': {
        'backup': [False, True],
        'follow': [False, True],
        'force': [True, False],
        'lstrip_blocks': [True, False],
        'newline_sequence': [True, False],
        'trim_blocks': [True, False],
        'unsafe_writes': [True, False],
    },

    'file': {
        'follow': [True, False],
        'force': [True, False],
        'recurse': [True, False],
        'unsafe_writes': [True, False],
        'state': ['absent', 'directory', 'file', 'hard', 'link', 'touch'],
    },

    'copy': {
        'backup': [True, False],
        'decrypt': [True, False],
        'follow': [True, False],
        'force': [True, False],
        'local_follow': [True, False],
        'remote_src': [True, False],
        'unsafe_writes': [True, False],
    },

    'gather_facts': {
        'parallel': [True, False],
    },

    'fail': {},
    'debug': {},
}
