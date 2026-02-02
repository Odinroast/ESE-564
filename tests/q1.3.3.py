OK_FORMAT = True

test = {   'name': 'q1.3.3',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(q_133, np.ndarray)\nTrue', 'failure_message': 'Answer is not a numpy array.', 'hidden': False, 'locked': False, 'points': 0},
                                   {'code': '>>> q_133.shape == (4,)\nTrue', 'failure_message': 'Answer does not have the correct shape.', 'hidden': False, 'locked': False, 'points': 0},
                                   {   'code': '>>> np.isclose(np.sum(q_133 ** 2), 1.0, atol=0.001).item()\nTrue',
                                       'failure_message': 'Answer is not a unit quaternion (q_0^2 q_1^2 + q_2^2 + q_3^2 = 1).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
