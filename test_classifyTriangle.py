from classifyTriangle import classify_triangle

def test_classify_triangle():
    
    result = classify_triangle(3,3,3)
    assert result == "Equilateral"
    
    result = classify_triangle(3,3,6)
    assert result == "Isosceles"     
    
    result = classify_triangle(4,5,6)
    assert result == "Scalene"
    