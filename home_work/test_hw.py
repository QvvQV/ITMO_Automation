def test_home():
    assert ('home', 'work') == ('home', 'work')


def test_QA():
    assert ('QC') == ('QC')


def test_not():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
