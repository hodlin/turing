states_table = {
        'q0': {0: {'write': 0, 'move': +1, 'next': 'q0'},
               1: {'write': 1, 'move': +1, 'next': 'q0'},
               'blank':
                  {'write': 'blank', 'move': +1, 'next': 'q1'}},

        'q1': {0: {'write': 0, 'move': +1, 'next': 'q1'},
               1: {'write': 1, 'move': +1, 'next': 'q1'},
               'blank':
                  {'write': 'blank', 'move': -1, 'next': 'q2'}},

        'q2': {0: {'write': 0, 'move': -1, 'next': 'q2'},
               1: {'write': 0, 'move': -1, 'next': 'q3'},
               'blank':
                  {'write': 'blank', 'move': +1, 'next': 'q4'}},

        'q3': {0: {'write': 0, 'move': -1, 'next': 'q3'},
               1: {'write': 1, 'move': -1, 'next': 'q3'},
               'blank':
                  {'write': 'blank', 'move': -1, 'next': 'q7'}},

        'q4': {0: {'write': 0, 'move': +1, 'next': 'q4'},
               1: {'write': 1, 'move': +1, 'next': 'q4'},
               'blank':
                  {'write': 'blank', 'move': -1, 'next': 'q5'}},

        'q5': {0: {'write': 'blank', 'move': -1, 'next': 'q5'},
               1: {'write': 1, 'move': -1, 'next': 'q5'},
               'blank':
                  {'write': 'blank', 'move': -1, 'next': 'q6'}},

        'q6': {0: {'write': 'blank', 'move': -1, 'next': 'q6'},
               1: {'write': 1, 'move': -1, 'next': 'q6'},
               'blank':
                  {'write': 'blank', 'move': +1, 'next': 'stop'}},

        'q7': {0: {'write': 0, 'move': -1, 'next': 'q7'},
               1: {'write': 0, 'move': +1, 'next': 'q0'},
               'blank':
                  {'write': 'blank', 'move': +1, 'next': 'stop'}}
    }
