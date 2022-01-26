test = {   'name': 'q4_2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> # It looks like you forgot to call .num_rows when you queried the table;\n'
                                               '>>> assert num_in_20th_century != tables.Table;\n'
                                               '>>> assert num_in_21st_century != tables.Table\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # It looks like you forgot to exclude movies in the 21st century when selecting movies in the 20th century;\n'
                                               '>>> #  HINT: Try using `are.below(2000)` for num_in_20th_century instead;\n'
                                               '>>> assert proportion_in_20th_century != 1.0\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> assert proportion_in_20th_century == 0.684\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert proportion_in_21st_century == 0.316\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
