OK_FORMAT = True

test = {   'name': 'q1.4',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> l1 = 1.0\n'
                                               '>>> l2 = 0.5\n'
                                               '>>> l3 = 0.75\n'
                                               '>>> l6 = 0.2\n'
                                               '>>> q1 = np.pi / 4\n'
                                               '>>> q2 = np.pi / 6\n'
                                               '>>> q3 = np.pi / 3\n'
                                               '>>> q4 = np.pi / 2\n'
                                               '>>> q5 = np.pi / 4\n'
                                               '>>> q6 = np.pi / 6\n'
                                               '>>> R, p = X_G_14(l1, l2, l3, l6, q1, q2, q3, q4, q5, q6)\n'
                                               '>>> isinstance(R, np.ndarray)\n'
                                               'True',
                                       'failure_message': 'The first return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n'
                                               '>>> l2 = 0.5\n'
                                               '>>> l3 = 0.75\n'
                                               '>>> l6 = 0.2\n'
                                               '>>> q1 = np.pi / 4\n'
                                               '>>> q2 = np.pi / 6\n'
                                               '>>> q3 = np.pi / 3\n'
                                               '>>> q4 = np.pi / 2\n'
                                               '>>> q5 = np.pi / 4\n'
                                               '>>> q6 = np.pi / 6\n'
                                               '>>> R, p = X_G_14(l1, l2, l3, l6, q1, q2, q3, q4, q5, q6)\n'
                                               '>>> isinstance(p, np.ndarray)\n'
                                               'True',
                                       'failure_message': 'The second return element is not a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n'
                                               '>>> l2 = 0.5\n'
                                               '>>> l3 = 0.75\n'
                                               '>>> l6 = 0.2\n'
                                               '>>> q1 = np.pi / 4\n'
                                               '>>> q2 = np.pi / 6\n'
                                               '>>> q3 = np.pi / 3\n'
                                               '>>> q4 = np.pi / 2\n'
                                               '>>> q5 = np.pi / 4\n'
                                               '>>> q6 = np.pi / 6\n'
                                               '>>> R, p = X_G_14(l1, l2, l3, l6, q1, q2, q3, q4, q5, q6)\n'
                                               '>>> R.shape == (3, 3)\n'
                                               'True',
                                       'failure_message': 'The first return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n'
                                               '>>> l2 = 0.5\n'
                                               '>>> l3 = 0.75\n'
                                               '>>> l6 = 0.2\n'
                                               '>>> q1 = np.pi / 4\n'
                                               '>>> q2 = np.pi / 6\n'
                                               '>>> q3 = np.pi / 3\n'
                                               '>>> q4 = np.pi / 2\n'
                                               '>>> q5 = np.pi / 4\n'
                                               '>>> q6 = np.pi / 6\n'
                                               '>>> R, p = X_G_14(l1, l2, l3, l6, q1, q2, q3, q4, q5, q6)\n'
                                               '>>> p.shape == (3,)\n'
                                               'True',
                                       'failure_message': 'The second return element does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n'
                                               '>>> l2 = 0.5\n'
                                               '>>> l3 = 0.75\n'
                                               '>>> l6 = 0.2\n'
                                               '>>> q1 = np.pi / 4\n'
                                               '>>> q2 = np.pi / 6\n'
                                               '>>> q3 = np.pi / 3\n'
                                               '>>> q4 = np.pi / 2\n'
                                               '>>> q5 = np.pi / 4\n'
                                               '>>> q6 = np.pi / 6\n'
                                               '>>> R, p = X_G_14(l1, l2, l3, l6, q1, q2, q3, q4, q5, q6)\n'
                                               '>>> np.allclose(R.T @ R, np.eye(3)) and np.allclose(R @ R.T, np.eye(3))\n'
                                               'True',
                                       'failure_message': 'The first return element is not a rotation matrix (R^TR = I, RR^T=I0).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 1.0\n'
                                               '>>> l2 = 0.5\n'
                                               '>>> l3 = 0.75\n'
                                               '>>> l6 = 0.2\n'
                                               '>>> q1 = np.pi / 4\n'
                                               '>>> q2 = np.pi / 6\n'
                                               '>>> q3 = np.pi / 3\n'
                                               '>>> q4 = np.pi / 2\n'
                                               '>>> q5 = np.pi / 4\n'
                                               '>>> q6 = np.pi / 6\n'
                                               '>>> R, p = X_G_14(l1, l2, l3, l6, q1, q2, q3, q4, q5, q6)\n'
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
