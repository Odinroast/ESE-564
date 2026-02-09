OK_FORMAT = True

test = {   'name': 'q2.1.1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> l1 = 1.0\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> d = 0.5\n'
                                               '>>> th = theta_G_211(l1, theta1, theta2, d)\n'
                                               '>>> (0 <= np.array(th) <= 2 * np.pi).item()\n'
                                               'True',
                                       'failure_message': 'The return element is not a scalar in 0 <= theta <= 2pi.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
