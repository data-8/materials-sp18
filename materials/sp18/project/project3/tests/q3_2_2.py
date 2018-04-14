test = {
  'name': 'Question 3.2.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> king_kong_genre == king_kong_expected_genre
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from collections import Counter
      g = train_movies.column('Genre')
      r = np.where(test_movies['Title'] == "king kong")[0][0]
      t = test_20.row(r)
      king_kong_expected_genre = Counter(np.take(g, np.argsort(fast_distances(t, train_20))[:9])).most_common(1)[0][0]
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
