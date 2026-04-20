OK_FORMAT = True

test = {   'name': 'q2.1.1',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> outputs = []\n'
                                               '>>> q = FIFOQueue_211()\n'
                                               ">>> q.add_node('a')\n"
                                               ">>> q.add_node('b')\n"
                                               '>>> outputs.append(q.get_next())\n'
                                               ">>> q.add_node('c')\n"
                                               '>>> outputs.append(q.get_next())\n'
                                               '>>> outputs.append(q.get_next())\n'
                                               ">>> outputs == ['a', 'b', 'c'] and len(q) == 0\n"
                                               'True',
                                       'failure_message': "The expected output sequence was ['a','b','c'] and the queue should be empty at the end.",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
