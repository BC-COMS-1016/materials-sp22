test = {   'name': 'q3_3_1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> # This test to see if the classify function works correctly where k=5;\n'
                                               '>>> from collections import Counter;\n'
                                               ">>> g = train_movies.column('Genre');\n"
                                               '>>> \n'
                                               '>>> def check(r, k):\n'
                                               '...     t = test_my_features.row(r)\n'
                                               '...     return classify(t, train_my_features, g, k) == \\\n'
                                               '...         Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:k])).most_common(1)[0][0];\n'
                                               '>>> \n'
                                               '>>> check_5_nn = [check(i, 5) for i in np.arange(11)];\n'
                                               '>>> assert np.all(check_5_nn)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test to see if the classify function works correctly where k=11;\n'
                                               '>>> from collections import Counter;\n'
                                               ">>> g = train_movies.column('Genre');\n"
                                               '>>> \n'
                                               '>>> def check(r, k):\n'
                                               '...     t = test_my_features.row(r)\n'
                                               '...     return classify(t, train_my_features, g, k) == \\\n'
                                               '...         Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:k])).most_common(1)[0][0];\n'
                                               '>>> \n'
                                               '>>> check_11_nn = [check(i, 11) for i in np.arange(11)];\n'
                                               '>>> assert np.all(check_11_nn)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
