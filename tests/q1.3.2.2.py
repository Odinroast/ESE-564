OK_FORMAT = True

test = {   'name': 'q1.3.2.2',
    'points': 0.5,
    'suites': [   {   'cases': [   {   'code': '>>> type(q_132) == dict and all((type(key) == tuple and len(key) == 2 and isinstance(val, (int, float)) for key, val in q_132.items()))\nTrue',
                                       'failure_message': 'Answer is not a dictionary mapping 2-tuples to scalars',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
