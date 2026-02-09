OK_FORMAT = True

test = {   'name': 'q1.1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> l = 1.0\n>>> d = 0.5\n>>> theta = np.pi / 4\n>>> R, _ = X_G_11(l, d, theta)\n>>> isinstance(R, np.ndarray)\nTrue',
                                       'failure_message': 'The first return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l = 1.0\n>>> d = 0.5\n>>> theta = np.pi / 4\n>>> _, p = X_G_11(l, d, theta)\n>>> isinstance(p, np.ndarray)\nTrue',
                                       'failure_message': 'The second return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l = 1.0\n>>> d = 0.5\n>>> theta = np.pi / 4\n>>> R, _ = X_G_11(l, d, theta)\n>>> R.shape == (2, 2)\nTrue',
                                       'failure_message': 'The first return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l = 1.0\n>>> d = 0.5\n>>> theta = np.pi / 4\n>>> _, p = X_G_11(l, d, theta)\n>>> p.shape == (2,)\nTrue',
                                       'failure_message': 'The second return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l = 1.0\n'
                                               '>>> d = 0.5\n'
                                               '>>> theta = np.pi / 4\n'
                                               '>>> R, _ = X_G_11(l, d, theta)\n'
                                               '>>> np.allclose(R.T @ R, np.eye(2)) and np.allclose(R @ R.T, np.eye(2))\n'
                                               'True',
                                       'failure_message': 'The first return element is not a rotation matrix (R^TR = I, RR^T=I0).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l = 1.0\n>>> d = 0.5\n>>> theta = np.pi / 4\n>>> R, _ = X_G_11(l, d, theta)\n>>> np.isclose(np.linalg.det(R), 1.0).item()\nTrue',
                                       'failure_message': 'The first return element is not a rotation matrix (det(R) = +1).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
