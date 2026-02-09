OK_FORMAT = True

test = {   'name': 'q1.2',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> l0 = 1.0\n>>> l1 = 0.5\n>>> l2 = 0.75\n>>> theta = np.pi / 4\n>>> R, _ = X_G_12(l0, l1, l2, theta)\n>>> isinstance(R, np.ndarray)\nTrue',
                                       'failure_message': 'The first return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n>>> l1 = 0.5\n>>> l2 = 0.75\n>>> theta = np.pi / 4\n>>> _, p = X_G_12(l0, l1, l2, theta)\n>>> isinstance(p, np.ndarray)\nTrue',
                                       'failure_message': 'The second return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n>>> l1 = 0.5\n>>> l2 = 0.75\n>>> theta = np.pi / 4\n>>> R, _ = X_G_12(l0, l1, l2, theta)\n>>> R.shape == (3, 3)\nTrue',
                                       'failure_message': 'The first return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n>>> l1 = 0.5\n>>> l2 = 0.75\n>>> theta = np.pi / 4\n>>> _, p = X_G_12(l0, l1, l2, theta)\n>>> p.shape == (3,)\nTrue',
                                       'failure_message': 'The second return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n'
                                               '>>> l1 = 0.5\n'
                                               '>>> l2 = 0.75\n'
                                               '>>> theta = np.pi / 4\n'
                                               '>>> R, _ = X_G_12(l0, l1, l2, theta)\n'
                                               '>>> np.allclose(R.T @ R, np.eye(3)) and np.allclose(R @ R.T, np.eye(3))\n'
                                               'True',
                                       'failure_message': 'The first return element is not a rotation matrix (R^TR = I, RR^T=I0).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l0 = 1.0\n'
                                               '>>> l1 = 0.5\n'
                                               '>>> l2 = 0.75\n'
                                               '>>> theta = np.pi / 4\n'
                                               '>>> R, _ = X_G_12(l0, l1, l2, theta)\n'
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
