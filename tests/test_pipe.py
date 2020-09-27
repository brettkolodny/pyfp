from pyfp.pipe import Pipe

def test_function_pipe():
    pipe_res = Pipe(3).to(max, 4).get()

    nonpipe_res = max(3, 4)
    
    assert pipe_res == nonpipe_res

def test_method_pipe():
    pipe_res = Pipe("hello, world!").to(str.upper).to(list).get()

    nonpipe_res = list("hello, world!".upper())

    assert pipe_res == nonpipe_res

def test_method_string_pipe():
    pipe_res = Pipe("hello").to("upper").to(list).get()

    nonpipe_res = list("hello".upper())

    assert pipe_res == nonpipe_res

def test_complex_pipe():
    ls = [97, 98, 99, 100]

    pipe_res = Pipe(ls) \
        .to(filter, lambda x: x % 2 == 0) \
        .to(map, lambda x: chr(x)) \
        .to(map, lambda x: x.upper()) \
        .to(list) \
        .get()

    res = list(
        map(
            lambda x: x.upper(), 
            map(
                lambda x: chr(x), 
                filter(
                    lambda x: x % 2 == 0, 
                    ls
                )
            )
        )
    )

    assert pipe_res == res

def test_invald_argument_type():
    try:
        Pipe(3).to(3)
        assert False
    except TypeError:
        assert True