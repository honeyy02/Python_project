from app.app import add,sub

def test_add():
    assert add(2,5)==7
    assert add(7,7)==14

def test_sub():
    assert sub(5,2)==3
    assert sub(9,9)==0    
