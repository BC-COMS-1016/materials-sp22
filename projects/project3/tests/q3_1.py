test = {   'name': 'q3_1',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> 0 <= distance_first_to_second <= 1.0\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # The distance between the same set of features should be 0;\n>>> assert np.isclose(distance(make_array(1, 2), make_array(1,2)), 0)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> np.isclose(distance(make_array(1,2,3), make_array(4,5,6)), 5.196152422706632)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
