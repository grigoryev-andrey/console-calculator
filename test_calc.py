from src import calc


def test_addition():
    assert calc.add(547, 679) == 1226
    assert calc.add(1390, 378912) == 380302


def test_subtraction():
    assert calc.sub(547, 679) == -132
    assert calc.sub(378912, 1390) == 377522


def test_multiplication():
    assert calc.mul(547, 679) == 371413
    assert calc.mul(1390, 378912) == 526687680


def test_division():
    assert calc.div(75, 25) == 3
    assert calc.div(84, 18) == 4


def test_addition_2():
    assert calc.add(3, 2) == 5
    assert calc.add(5, 7) == 12
