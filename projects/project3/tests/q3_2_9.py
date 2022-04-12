test = {   'name': 'q3_2_9',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> # At least 4 of the nearest 7 movies should be thrillers;\n'
                                               ">>> assert genre_and_distances.take(np.arange(7)).group('Genre').index_by('Genre')[my_assigned_genre][0].item('count') >= 4\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> assert my_assigned_genre_was_correct == (my_assigned_genre == 'thriller')\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
