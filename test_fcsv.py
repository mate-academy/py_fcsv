import io
import fcsv


def test_fcsv():
    s = io.StringIO("""Apples,2.3,5
Cherrys,7.2,4
Tomatoes,3.4,10""")
    assert fcsv.calc_price(s, lambda x,m: x) == 74.3