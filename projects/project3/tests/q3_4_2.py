test = {   'name': 'q3_4_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # Make sure the table has the following columns in this order;\n>>> assert test_movie_correctness.labels == ('Title', 'Genre', 'Was correct')\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> assert test_movie_correctness.num_rows == test_movies.num_rows\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure the Genres column is not modified;\n'
                                               '>>> assert test_movie_correctness.group(\'Genre\').where(\'Genre\', "comedy").column(\'count\').item(0) == 20\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
