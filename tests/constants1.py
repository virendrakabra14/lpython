def test_boz():
    b: str
    b = bin(5)
    b = bin(64)
    b = oct(8)
    b = oct(56)
    b = hex(42)
    b = hex(12648430)


def test_ord_chr():
    s: str
    a: i32
    a = ord('5')
    s = chr(43)


def test_abs():
    a: i32
    a = abs(-1)
    a = abs(False)
    a = abs(True)
    b: f32
    b = abs(3.45)
    b = abs(-3.45)
    b = abs(complex(3.45, 5.6))