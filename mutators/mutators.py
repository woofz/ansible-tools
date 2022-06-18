import random
import typing
from typing import Dict, Any

from utils.data import module_parameters


def mutate_params(*, normal_module: dict, module_used: str, task_name: str) -> Dict[str, Any]:
    """
    This method mutates a given module description to another, by changing or adding a random parameter and documenting
    it in the Task Name. Specific changes were made for some modules, such as 'command' and
    Args:
        normal_module: Unmutated module description
        module_used: Used module (i.e.: service, gather_facts)
        task_name: Task name (i.e.: restart datadog-agent)

    Returns:
        dict: returns a dictionary with two keys:
                - task_body: contains the mutated task body;
                - task_name: contains the mutated task title.
    """
    module = normal_module
    module_params = typing.cast(Dict[str, Any], (module_parameters[module_used]))

    if type(module) in (str, bool):
        mutable_module_params = None
    else:
        mutable_module_params = set(module.keys()).intersection(set(module_params.keys()))

    if not mutable_module_params or module_used == 'command':
        # Adding a random parameter to the data
        if module_used not in module_parameters.keys():
            return {'task_body': module, 'task_name': task_name}
        param_to_add = random.choice(list(module_parameters.get(module_used)))
        param_value = random.choice(list(module_parameters.get(module_used).get(param_to_add)))
        # getting the mutated description for the parameter
        desc_param_value = [x for x in list(module_parameters.get(module_used).get(param_to_add)) if x != param_value]
        m_desc = param_to_add + ' ' + str(desc_param_value[0])

        task_name += ' ' + m_desc
        if type(module) in (str, bool):
            mutated_dict = dict()
            mutated_dict.update({param_to_add: param_value})
            return {'task_body': mutated_dict, 'task_name': task_name}
        if module is None:
            print("module is none.")
        module.update({param_to_add: param_value})
        return {'task_body': module, 'task_name': task_name}

    param_to_mutate = random.choice(list(mutable_module_params))
    mutable_param_values = module_params[param_to_mutate]
    gen = [i for i in mutable_param_values if i != module[param_to_mutate]]
    mutated_value = random.choice(gen)

    mutated_module = module
    old_param = mutated_module[param_to_mutate]
    mutated_module[param_to_mutate] = mutated_value

    task_name += ' ' + param_to_mutate + ' ' + str(old_param)
    return {'task_body': mutated_module, 'task_name': task_name}
