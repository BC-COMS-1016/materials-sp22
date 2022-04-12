test = {   'name': 'q3_3_2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> from collections import Counter;\n'
                                               ">>> g = train_movies.column('Genre');\n"
                                               ">>> r = np.where(test_movies['Title'] == 'juno')[0][0];\n"
                                               '>>> t = test_my_features.row(r);\n'
                                               '>>> juno_expected_genre = Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:13])).most_common(1)[0][0];\n'
                                               '>>> assert juno_expected_genre == juno_genre\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
