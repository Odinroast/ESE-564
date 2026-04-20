OK_FORMAT = True

test = {   'name': 'q1.1.8.3',
    'points': 0.5,
    'suites': [   {   'cases': [   {   'code': '>>> type(p_118) == dict and all((type(child) == tuple and len(child) == 2 and (type(parent) == tuple and len(parent) == 2 or parent is None) for '
                                               'child, parent in p_118.items()))\n'
                                               'True',
                                       'failure_message': 'Answer is not a dictionary mapping 2-tuples to 2-tuples or None',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
