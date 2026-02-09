OK_FORMAT = True

test = {   'name': 'q3.4',
    'points': 7,
    'suites': [   {   'cases': [   {   'code': '>>> type(joints_34) is list and len(joints_34) == 7\nTrue',
                                       'failure_message': 'IK did not return any joint angles',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': ">>> joint_ids = [mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, f'panda_joint{i + 1}') for i in range(7)]\n"
                                               '>>> all((joints_34[i] >= model.jnt_range[joint_ids[i], 0] and joints_34[i] <= model.jnt_range[joint_ids[i], 1] for i in range(7)))\n'
                                               'True',
                                       'failure_message': 'The joint values do not respect joint limits',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
