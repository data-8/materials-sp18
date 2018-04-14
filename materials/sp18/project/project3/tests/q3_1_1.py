test = {
  'name': 'Question 3.1.1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(my_20_features)
          20
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all([f in test_movies.labels for f in my_20_features])
          True
          >>> # It looks like there are many movies in the training set that
          >>> # don't have any of your chosen words.  That will make your
          >>> # classifier perform very poorly in some cases.  Try choosing
          >>> # at least 1 common word.
          >>> train_f = train_movies.select(my_20_features)
          >>> np.count_nonzero(train_f.apply(lambda r: np.sum(np.abs(np.array(r))) == 0)) < 20
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like there are many movies in the test set that
          >>> # don't have any of your chosen words.  That will make your
          >>> # classifier perform very poorly in some cases.  Try choosing
          >>> # at least 1 common word.
          >>> test_f = test_movies.select(my_20_features)
          >>> np.count_nonzero(test_f.apply(lambda r: np.sum(np.abs(np.array(r))) == 0)) < 5
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
