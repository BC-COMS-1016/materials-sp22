test = {   'name': 'q3_3_3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> def check(r):\n'
                                               '...     t = test_my_features.row(r)\n'
                                               "...     return classify(t, train_my_features, train_movies.column('Genre'), 13) == \\\n"
                                               '...         classify_feature_row(t);\n'
                                               '>>> \n'
                                               '>>> assert np.all([check(i) for i in np.arange(13)])\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
