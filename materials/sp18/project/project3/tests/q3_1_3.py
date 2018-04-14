test = {
  'name': 'Question 3.1.3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> genre_and_distances.labels == ('Genre', 'Distance')
          True
          >>> genre_and_distances.num_rows == train_movies.num_rows
          True
          >>> print(genre_and_distances.group('Genre'))
          Genre   | count
          action  | 114
          romance | 91
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(genre_and_distances.column('Distance'), sorted(fast_distances(test_20.row(0), train_20)))
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
