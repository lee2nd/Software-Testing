import math

def calculate_grade(scores):
    if not isinstance(scores, list) or len(scores) == 0:
        raise ValueError('Scores must be provided as a non-empty list.')

    total = 0
    for score in scores:
        if not isinstance(score, (int, float)) or math.isnan(score) or score < 0 or score > 100:
            raise ValueError('Scores must be numeric values between 0 and 100.')

        total += score

    average = total / len(scores)

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
