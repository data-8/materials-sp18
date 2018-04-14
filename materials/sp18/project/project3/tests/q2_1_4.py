test = {
  'name': '2.1.4',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(close_movies.labels) >= {'Genre', 'Title', 'feel', 'money'}
          True
          >>> close_movies.num_rows == 7
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
