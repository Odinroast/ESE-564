OK_FORMAT = True

test = {   'name': 'q2.2',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': ">>> goal = 'a'\n"
                                               ">>> parents = {'a': 'b', 'b': 'c', 'c': 'd', 'd': None}\n"
                                               '>>> plan = retrace_plan_22(goal, parents)\n'
                                               ">>> plan == ['d', 'c', 'b', 'a']\n"
                                               'True',
                                       'failure_message': "The expected plan was ['d', 'c', 'b', 'a']",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
