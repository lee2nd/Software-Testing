from calculateGrade import calculate_grade
import pytest

def test_calculate_grade_empty():
    
    with pytest.raises(Exception) as error:
        calculate_grade([])
    assert str(error.value) == 'Scores must be provided as a non-empty list.'
    

def test_calculate_grade_outlier():
    
    scores = [-1,-5000,101,1000]

    with pytest.raises(Exception) as error:
        calculate_grade(scores)
    assert str(error.value) == 'Scores must be numeric values between 0 and 100.'    

def test_calculate_grade_normal():    
    
    'test A'
    scores = [97,98,96]
    assert str(calculate_grade(scores)) == 'A'
    'test B'
    scores = [81,85,84]
    assert str(calculate_grade(scores)) == 'B'
    'test C'
    scores = [71,69,78]
    assert str(calculate_grade(scores)) == 'C'
    'test D'
    scores = [54,69,66]
    assert str(calculate_grade(scores)) == 'D'
    'test F'
    scores = [1,30,50]
    assert str(calculate_grade(scores)) == 'F'                