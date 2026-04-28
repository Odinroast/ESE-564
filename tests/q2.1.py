OK_FORMAT = True

test = {   'name': 'q2.1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> outputs = []\n'
                                               '>>> q = PriorityQueue_21()\n'
                                               ">>> q.add('a', 5)\n"
                                               ">>> q.add('b', 10)\n"
                                               ">>> q.add('c', 1)\n"
                                               '>>> outputs.append(q.extract_min())\n'
                                               ">>> q.decrease_priority('a', 0)\n"
                                               '>>> outputs.append(q.extract_min())\n'
                                               '>>> outputs.append(q.extract_min())\n'
                                               ">>> outputs == ['c', 'a', 'b'] and len(q) == 0\n"
                                               'True',
                                       'failure_message': "The expected output sequence was ['c','a','b'] and the queue should be empty at the end.",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
