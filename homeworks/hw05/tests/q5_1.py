test = {   'name': 'q5_1',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> # The array deck_model_probabilities should have a length of 2;\n>>> assert len(deck_model_probabilities) == 2\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # The sum of the array should equal 1 (remember that these are probabilities);\n>>> assert sum(deck_model_probabilities) == 1\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The values in the array should be between 0 and 1 (remember that these are probabilities);\n'
                                               '>>> assert 0 < deck_model_probabilities.item(0) < 1 and  0 < deck_model_probabilities.item(1) < 1\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
