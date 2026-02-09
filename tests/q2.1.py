OK_FORMAT = True

test = {   'name': 'q2.1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> l1 = 1.0\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> d = 0.5\n'
                                               '>>> R, _ = X_G_21(l1, theta1, theta2, d)\n'
                                               '>>> isinstance(R, np.ndarray)\n'
                                               'True',
                                       'failure_message': 'The first return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n>>> theta1 = np.pi / 4\n>>> theta2 = np.pi / 6\n>>> d = 0.5\n>>> R, _ = X_G_21(l1, theta1, theta2, d)\n>>> R.shape == (2, 2)\nTrue',
                                       'failure_message': 'The first return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> d = 0.5\n'
                                               '>>> R, _ = X_G_21(l1, theta1, theta2, d)\n'
                                               '>>> np.allclose(R.T @ R, np.eye(2)) and np.allclose(R @ R.T, np.eye(2))\n'
                                               'True',
                                       'failure_message': 'The first return element is not a rotation matrix (R^TR=I, RR^T=I).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> d = 0.5\n'
                                               '>>> R, _ = X_G_21(l1, theta1, theta2, d)\n'
                                               '>>> np.isclose(np.linalg.det(R), 1.0).item()\n'
                                               'True',
                                       'failure_message': 'The first return element is not a rotation matrix (det(R) = +1).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> d = 0.5\n'
                                               '>>> _, p = X_G_21(l1, theta1, theta2, d)\n'
                                               '>>> isinstance(p, np.ndarray)\n'
                                               'True',
                                       'failure_message': 'The second return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n>>> theta1 = np.pi / 4\n>>> theta2 = np.pi / 6\n>>> d = 0.5\n>>> _, p = X_G_21(l1, theta1, theta2, d)\n>>> p.shape == (2,)\nTrue',
                                       'failure_message': 'The second return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
