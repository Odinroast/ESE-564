OK_FORMAT = True

test = {   'name': 'q1.2',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> X = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])\n'
                                               '>>> normalizer = Normalizer_12(X)\n'
                                               '>>> isinstance(normalizer.mean, torch.Tensor) and normalizer.mean.shape == (2,) and isinstance(normalizer.std, torch.Tensor) and (normalizer.std.shape '
                                               '== (2,))\n'
                                               'True',
                                       'failure_message': 'The mean or std your normalizer is not a tensor of the correct shape.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])\n'
                                               '>>> normalizer = Normalizer_12(X)\n'
                                               '>>> X_normalized = normalizer.normalize(X)\n'
                                               '>>> torch.allclose(X_normalized.mean(axis=0), torch.zeros(2)) and torch.allclose(X_normalized.std(axis=0), torch.ones(2), atol=0.0001)\n'
                                               'True',
                                       'failure_message': 'The tensor normalized by your normalizer does not have the correct statistics.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])\n'
                                               '>>> normalizer = Normalizer_12(X)\n'
                                               '>>> X_normalized = normalizer.normalize(X)\n'
                                               '>>> X_denormalized = normalizer.denormalize(X_normalized)\n'
                                               '>>> torch.allclose(X_denormalized, X)\n'
                                               'True',
                                       'failure_message': 'The tensor denormalized by your normalizer is not correct.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
