OK_FORMAT = True

test = {   'name': 'q3.1',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> R = np.eye(3).tolist()\n>>> p = np.array([100, 0, 0]).tolist()\n>>> panda_ik_31(R, p, model) is None\nTrue',
                                       'failure_message': 'Did not return None for unreachable pose',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> R = np.eye(3).tolist()\n>>> p = np.array([0.2, 0.3, 0]).tolist()\n>>> ik = panda_ik_31(R, p, model)\n>>> type(ik) is list and len(ik) == 7\nTrue',
                                       'failure_message': 'Did not return a 7-element list for  valid pose',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
