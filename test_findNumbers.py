from findNumbers import find_numbers

def test_find_numbers():
    
    nums = [120, 80, 70, 30, 50, 0, -100]
    
    result = find_numbers(nums)
    
    for n, r in zip(nums,result):
        if n > 0:
            assert r == "positive"
        elif n < 0:
            assert r == "negative"
        else:
            assert r == "zero"       
