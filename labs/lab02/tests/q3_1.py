test = {   'name': 'q3_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # It looks like top_10_movies is not a Table. ;\n'
                                               '>>> # Remember, use Table() to make a new Table;\n'
                                               '>>> assert type(top_10_movies) == tables.Table\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> assert top_10_movies.sort(\'Name\').select(\'Name\')[0][0] == "12 Angry Men (1957)"\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
