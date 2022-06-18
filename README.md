# Ansible Mutator Tool
This tool was used to detect Ansible's linguistic inconsistencies between tasks title and their body. 
This package mutates the most used Ansible modules (*service, set_fact, shell, command, template, file, copy, gather_facts, fail, debug*) parameters.

### Usage
Given a dict of task module description: 
```python
services = {
    1: {
        'name': 'task1',
        'enable': 'no',
        'state': 'stopped',
	'task_name': 'Modify task1'
    },

    2: {
        'name': 'task2',
        'enable': 'yes',
        'state': 'started',
	'task_name': 'Update task2 and enable'
    }
```
The method *mutate_params* will modify a random module parameter: in this case one between *enable* and *state*, because *service* module has those parameters.

```python
for key, value in services.items():
    mutated_tasks.update({key: mutate_params(normal_module=value,
                                                 module_used='service',
                                                 task_name=value['task_name'])})

```

```python
print(f"Task Body: {mutated_tasks[1]['task_body']}")
print(f"Task Name: {mutated_tasks[1]['task_name']}")
```

```
{'name': 'task1', 'enable': 'no', 'state': 'restarted', 'task_name': 'Modify task1'}
Modify task1 state stopped
```
*mutate_params* is going to return a dictionary with 2 keys:
1. *task_body*, which contains the mutated task body (name, enable, state, task_name);
2. *task_name*, which contains the mutated task name. Note that if the task name is inside the task dict, it will not change there, but it will come back mutated in the *task_name* dict key object. This is an intended behaviour.

