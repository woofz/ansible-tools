module_parameters = {
    'service': {
        'state': ['started', 'stopped', 'reloaded', 'restarted'],
        'enabled': [False, True],
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

    'fail': {
        'msg': ['yes', 'no']
        },
    'debug': {
        'verbosity': [0, 1, 2, 3]},
}