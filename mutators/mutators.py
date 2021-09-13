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
        'enabled': ['no', 'yes'],
    },

    'set_fact': {
        'cacheable': ['no', 'yes'],
    },

    'shell': {
        'stdin_add_newline ': ['no', 'yes'],
    },

    'command': {
        'stdin_add_newline ': ['no', 'yes'],
        'strip_empty_ends': ['no', 'yes'],
        'warn': ['no', 'yes'],
    },

    'template': {
        'backup': ['no', 'yes'],
        'follow': ['no', 'yes'],
        'force': ['no', 'yes'],
        'lstrip_blocks': ['no', 'yes'],
        'newline_sequence': ['no', 'yes'],
        'trim_blocks': ['no', 'yes'],
        'unsafe_writes': ['no', 'yes'],
    },

    'file': {
        'follow': ['no', 'yes'],
        'force': ['no', 'yes'],
        'recurse': ['no', 'yes'],
        'unsafe_writes': ['no', 'yes'],
        'state': ['absent', 'directory', 'file', 'hard', 'link', 'touch'],
    },

    'copy': {
        'backup': ['no', 'yes'],
        'decrypt': ['no', 'yes'],
        'follow': ['no', 'yes'],
        'force': ['no', 'yes'],
        'local_follow': ['no', 'yes'],
        'remote_src': ['no', 'yes'],
        'unsafe_writes': ['no', 'yes'],
    },

    'gather_facts': {
        'parallel': ['no', 'yes'],
    },

    'fail': {},
    'debug': {},
}
