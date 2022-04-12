test = {   'name': 'q3_2_6',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> assert len(my_features) >= 10\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure every word in my_features is a column in the test movies table;\n>>> assert np.all([f in test_movies.labels for f in my_features])\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # It looks like there are many movies in the training set;\n'
                                               ">>> # that don't have any of the chosen words. The classifier will perform ;\n"
                                               '>>> # poorly in this case. ;\n'
                                               '>>> train_f = train_movies.select(my_features);\n'
                                               '>>> assert np.count_nonzero(train_f.apply(lambda r: np.sum(np.abs(np.array(r)) == 0))) < len(my_features)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # It looks like there are many movies in the test set;\n'
                                               ">>> # that don't have any of the chosen words. The classifier will perform ;\n"
                                               '>>> # poorly in this case. ;\n'
                                               '>>> test_f = test_movies.select(my_features);\n'
                                               '>>> assert np.count_nonzero(test_f.apply(lambda r: np.sum(np.abs(np.array(r)) == 0))) < len(my_features)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
