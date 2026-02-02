OK_FORMAT = True

test = {   'name': 'q3.2.1',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(p_B_321, np.ndarray)\nTrue', 'failure_message': 'p_B_321 is not a numpy array.', 'hidden': False, 'locked': False, 'points': 0},
                                   {'code': '>>> p_B_321.shape == (3,)\nTrue', 'failure_message': 'p_B_321 does not have the correct shape.', 'hidden': False, 'locked': False, 'points': 0},
                                   {'code': '>>> isinstance(quat_B_321, np.ndarray)\nTrue', 'failure_message': 'quat_B_321 is not a numpy array).', 'hidden': False, 'locked': False, 'points': 0},
                                   {'code': '>>> quat_B_321.shape == (4,)\nTrue', 'failure_message': 'quat_B_321 does not have the correct shape.', 'hidden': False, 'locked': False, 'points': 0},
                                   {   'code': '>>> np.isclose(np.sum(quat_B_321 ** 2), 1.0, atol=0.001).item()\nTrue',
                                       'failure_message': 'quat_B_321 is not a unit quaternion (q_0^2 q_1^2 + q_2^2 + q_3^2 = 1).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
