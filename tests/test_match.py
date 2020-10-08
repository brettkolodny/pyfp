from pyfp import Match

def test_match():
    foo = 3

    a = Match(3) \
        .branch(4, lambda: "Hello") \
        .branch(5, lambda: "Goodbye") \
        .branch(lambda x: x < 4, lambda: "World!") \
        .default(lambda: str(foo)) \
        .get()
    
    assert a == "World!"