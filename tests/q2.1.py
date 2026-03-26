OK_FORMAT = True

test = {   'name': 'q2.1',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> from IPython.utils import io\n'
                                               '>>> with io.capture_output() as captured:\n'
                                               "...     X, Y, _ = minari_data_21('mujoco/pusher/expert-v0')\n"
                                               '>>> isinstance(X, torch.Tensor) and isinstance(Y, torch.Tensor)\n'
                                               'True',
                                       'failure_message': 'The first two return values are not torch.Tensor objects.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
