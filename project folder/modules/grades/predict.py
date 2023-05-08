'''
Module for exam predictions
'''

def get_avg(score_history):
    '''takes a list from previous grades and returs average'''
    return sum(score_history) / len(score_history)


def predict_score(score_history, min_score=0):
    '''take a list of previous percentages grades and return the average'''
    score_avg = get_avg(score_history)
    if score_avg < min_score:
        return min_score
    return score_avg

