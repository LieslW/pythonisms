import pytest
from pythonisms import LinkedList, shout


# @pytest.mark.skip
def test_iteration():
    escape = LinkedList(("if","you","like","pina","coladas"))
    lyrics = []
    for lyric in escape:
        lyrics.append(lyric)
    assert lyrics == ["if","you","like","pina","coladas"]


# @pytest.mark.skip
def test_comprehension():
    escape = LinkedList(("if","you","like","pina","coladas"))
    lyrics = [lyric.upper() for lyric in escape]
    assert lyrics == ["IF","YOU","LIKE","PINA","COLADAS"]


# @pytest.mark.skip
def test_cast():
    escape = ["if","you","like","pina","coladas"]
    lyrics = LinkedList(escape)
    assert list(lyrics) == escape


# @pytest.mark.skip
def test_range():
    num_range = range(1,20+1)
    nums = LinkedList(num_range)
    assert len(nums) == 20


# @pytest.mark.skip
def test_filter():
    nums = LinkedList(range(1,21))
    odds = [num for num in nums if num % 2]
    assert odds == [1,3,5,7,9,11,13,15,17,19]


# @pytest.mark.skip
def test_next():
    escape = LinkedList(["if","you","like","pina","coladas"])
    iterator = iter(escape)
    assert next(iterator) == "if"
    assert next(iterator) == "you"
    assert next(iterator) == "like"
    assert next(iterator) == "pina"
    assert next(iterator) == "coladas"


# @pytest.mark.skip
def test_stop_iteration():
    escape = LinkedList(["if","you","like","pina","coladas"])
    iterator = iter(escape)
    with pytest.raises(StopIteration):
        while True:
            lyric = next(iterator)


# @pytest.mark.skip
def test_string():
    escape = LinkedList(["if","you","like","pina","coladas"])
    assert str(escape) == "[ if ] -> [ you ] -> [ like ] -> [ pina ] -> [ coladas ] -> None"


# @pytest.mark.skip
def test_same():
    linked_list_a = LinkedList(["if","you","like","pina","coladas"])
    linked_list_b = LinkedList(["if","you","like","pina","coladas"])
    assert linked_list_a == linked_list_b


# @pytest.mark.skip
def test_get():
    escape = LinkedList(["if","you","like","pina","coladas"])
    assert escape[0] == "if"


# @pytest.mark.skip
def test_out_of_range():
    escape = LinkedList(["if","you","like","pina","coladas"])
    with pytest.raises(IndexError):
        escape[100]


# @pytest.mark.skip
def test_shout():
    @shout
    def talk():
        return 'hello'

    actual = talk()
    expected = 'HELLO!!!'
    assert actual == expected

