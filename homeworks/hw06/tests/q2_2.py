test = {   'name': 'q2_2',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> # It looks like your simulation isnt random;\n>>> assert np.std([simulate() for _ in range(1000)]) > 0\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # It looks like the sum of the items in model_proportions does not equal 1;\n'
                                               '>>> assert model_proportions.item(0) + model_proportions.item(1) == 1\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
