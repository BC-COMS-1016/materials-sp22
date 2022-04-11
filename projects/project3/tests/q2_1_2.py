test = {   'name': 'q2_1_2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you can use any two movies;\n'
                                               '>>> correct_distance = 0.0005412;\n'
                                               '>>> assert np.round(distance_two_features("clerks.", "the avengers", "water", "feel"), 7) == correct_distance\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure you can use any two features;\n>>> np.round(distance_two_features("clerks.", "the avengers", "your", "that"), 7) == 0.0064867\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
