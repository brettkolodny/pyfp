from pyfp.option import Option

def test_is_empty():
    empty = Option.empty()

    assert empty.is_empty() == True
    assert empty.is_some() != True

def test_is_some():
    some = Option.some(3)

    assert some.is_some() == True
    assert some.is_empty != True

def test_default():
    opt = Option()

    assert opt.is_empty() == True

def test_unwrap_some():
    opt = Option.some(3)

    assert opt.unwrap() == 3

def test_unwrap_empty():
    opt = Option.empty()

    try:
        opt.unwrap()
        assert False
    except AssertionError:
        assert True

def test_unwrap_or():
    opt = Option.some(6)

    res = opt.unwrap_or(12)

    assert res == 6

    opt = Option.empty()

    res = opt.unwrap_or(12)

    assert res == 12

def test_unwrap_or_else():
    opt = Option.empty()
    foo = 100
    func = lambda: foo * 3

    res = opt.unwrap_or_else(func)

    assert res == 300

    opt = Option.some(6)

    res = opt.unwrap_or_else(func)

    assert res == 6

def test_map():
    opt = Option.some(98)

    res = opt.map(lambda x: chr(x))

    assert res.unwrap() == "b"

def test_map_or():
    opt = Option.empty()

    res = opt.map_or("b", lambda x: chr(x))

    assert res.unwrap() == "b"

    opt = Option.some(99)

    res = opt.map_or(98, lambda x: chr(x))

    assert res.unwrap() == "c"

def test_map_or_else():
    opt = Option.empty()

    res = opt.map_or_else(lambda: ord("b"), lambda x: ord(x))

    assert res.unwrap() == ord("b")

    opt = Option.some("c")

    res = opt.map_or_else(lambda: ord("b"), lambda x: ord(x))

    assert res.unwrap() == ord("c")