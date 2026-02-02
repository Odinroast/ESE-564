OK_FORMAT = True

test = {   'name': 'q1.3.7',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> r = 2 * np.pi / 3\n>>> y = np.pi / 4\n>>> isinstance(R_r_halfpi_y_137(r, y), np.ndarray)\nTrue',
                                       'failure_message': 'Did not return a numpy array.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> r = 2 * np.pi / 3\n>>> y = np.pi / 4\n>>> R_137 = R_r_halfpi_y_137(r, y)\n>>> R_137.shape == (3, 3)\nTrue',
                                       'failure_message': 'The returned array does not have the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> r = 2 * np.pi / 3\n'
                                               '>>> y = np.pi / 4\n'
                                               '>>> R_137 = R_r_halfpi_y_137(r, y)\n'
                                               '>>> np.allclose(R_137.T @ R_137, np.eye(3), atol=0.001) and np.allclose(R_137 @ R_137.T, np.eye(3), atol=0.001)\n'
                                               'True',
                                       'failure_message': 'The returned array is not a rotation matrix (R^TR = I, RR^T = I).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> r = 2 * np.pi / 3\n>>> y = np.pi / 4\n>>> R_137 = R_r_halfpi_y_137(r, y)\n>>> np.isclose(np.linalg.det(R_137), 1.0, atol=0.001).item()\nTrue',
                                       'failure_message': 'The returned array is not a rotation matrix (det(R) =+1).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
