test = {   'name': 'q4_1',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> assert type(above_eight) == tables.Table\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert above_eight.num_rows == 20\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # It looks like you put the columns out of order.;\n'
                                               ">>> #   Make sure to call .select('Title', 'Rating') in that order;\n"
                                               ">>> assert above_eight.labels[0] == 'Title' and above_eight.labels[1] == 'Rating'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
