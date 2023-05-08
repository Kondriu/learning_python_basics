'''
scrypt for procassing student grated
'''

from grades.predict import predict_score
from grades.results import get_grade

score_history = [80, 90, 10, 60]
predicted_score = predict_score(score_history, 50)

predicted_grade = get_grade(predicted_score)

print(f'The students predicred great {predicted_grade}')

