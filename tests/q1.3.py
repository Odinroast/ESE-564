OK_FORMAT = True

test = {   'name': 'q1.3',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> l0 = 1.0\n'
                                               '>>> l1 = 0.5\n'
                                               '>>> l2 = 0.75\n'
                                               '>>> d1 = 0.2\n'
                                               '>>> d2 = 0.3\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> R, _ = X_G_13(l0, l1, l2, d1, d2, theta1, theta2)\n'
                                               '>>> isinstance(R, np.ndarray)\n'
                                               'True',
                                       'failure_message': 'The first return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n'
                                               '>>> l1 = 0.5\n'
                                               '>>> l2 = 0.75\n'
                                               '>>> d1 = 0.2\n'
                                               '>>> d2 = 0.3\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> _, p = X_G_13(l0, l1, l2, d1, d2, theta1, theta2)\n'
                                               '>>> isinstance(p, np.ndarray)\n'
                                               'True',
                                       'failure_message': 'The second return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n'
                                               '>>> l1 = 0.5\n'
                                               '>>> l2 = 0.75\n'
                                               '>>> d1 = 0.2\n'
                                               '>>> d2 = 0.3\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> R, _ = X_G_13(l0, l1, l2, d1, d2, theta1, theta2)\n'
                                               '>>> R.shape == (2, 2)\n'
                                               'True',
                                       'failure_message': 'The first return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n'
                                               '>>> l1 = 0.5\n'
                                               '>>> l2 = 0.75\n'
                                               '>>> d1 = 0.2\n'
                                               '>>> d2 = 0.3\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> _, p = X_G_13(l0, l1, l2, d1, d2, theta1, theta2)\n'
                                               '>>> p.shape == (2,)\n'
                                               'True',
                                       'failure_message': 'The second return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n'
                                               '>>> l1 = 0.5\n'
                                               '>>> l2 = 0.75\n'
                                               '>>> d1 = 0.2\n'
                                               '>>> d2 = 0.3\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> R, _ = X_G_13(l0, l1, l2, d1, d2, theta1, theta2)\n'
                                               '>>> np.allclose(R.T @ R, np.eye(2)) and np.allclose(R @ R.T, np.eye(2))\n'
                                               'True',
                                       'failure_message': 'The first return element is not a rotation matrix (R^TR = I, RR^T=I0).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n'
                                               '>>> l1 = 0.5\n'
                                               '>>> l2 = 0.75\n'
                                               '>>> d1 = 0.2\n'
                                               '>>> d2 = 0.3\n'
                                               '>>> theta1 = np.pi / 4\n'
                                               '>>> theta2 = np.pi / 6\n'
                                               '>>> R, _ = X_G_13(l0, l1, l2, d1, d2, theta1, theta2)\n'
                                               '>>> np.isclose(np.linalg.det(R), 1.0).item()\n'
                                               'True',
                                       'failure_message': 'The first return element is not a rotation matrix (det(R) = +1).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
