def predict_lte(current, past):
    ''' 
        Takes in a list of integers `current` a time series of inflows to 
        the tank, and a list of lists (time series) of integers `past`.
        
        Returns the next predicted flow value (integer) for the current
        time series based on the past time series.
    '''
    
    # Compare each past time series with a copy of the current time series list
    # and calculate their similarities
    similarities = list(map(calculate_similarity, [current] * len(past), past))
    
    # Get the index of the first time series in the past
    # that is the most similar to the current one
    index = similarities.index(min(similarities))
    most_similar_time_series = past[index]

    return most_similar_time_series[-1]

def calculate_similarity(current, past):
    ''' Takes in the `current` time series as a list, and the `past` time 
        series as a list.
        Returns their similarity as an integer. The lower the integer, the
        more similar they are and vice versa.
    '''
    similarity = 0
    for i in range(len(current)):
        diff = current[i] - past[i]
        similarity += abs(diff)
    return similarity