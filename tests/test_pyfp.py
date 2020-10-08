from pyfp import __version__
from pyfp import Pipe
from pyfp import Option

def test_version():
    assert __version__ == '0.1.5'

def test_option_pipe():

    def get_ascii_letter(key_code: int) -> Option:
        if 97 <= key_code <= 122 or 65 <= key_code <= 90:
            return Option.some(chr(key_code))
        
        return Option.empty()
    
    res = Pipe([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100]) \
        .to(map, lambda x: get_ascii_letter(x)) \
        .to(map, lambda x: x.unwrap_or("-")) \
        .to("".join) \
        .get()

    assert res == "Hello--World"
