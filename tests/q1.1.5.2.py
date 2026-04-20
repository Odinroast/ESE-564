OK_FORMAT = True

test = {   'name': 'q1.1.5.2',
    'points': 0.5,
    'suites': [   {   'cases': [   {   'code': '>>> type(q_115) == list and all((type(node) == tuple and len(node) == 2 for node in q_115))\nTrue',
                                       'failure_message': 'Answer is not a list of 2-tuples',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
