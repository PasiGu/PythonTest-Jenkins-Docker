from new_program import plusmal, unterschreiben, kubieren

def test_plusmal():
    assert plusmal(2, 3) == 10

def test_unterschreiben():
    assert unterschreiben("test") == "test_unterschrieben"

def test_kubieren():
    assert kubieren(2) == 8
    assert kubieren(3) == 27
