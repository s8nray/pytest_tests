def func(x):
    return x + 1


def test_answer_one():
    assert func(3) == 4

def test_answer_two():
    assert func(-4) == -3
    
def test_answer_three():
    assert func(-1) == 0
    
def test_answer_four():
    assert func(10) == 11    
    

    