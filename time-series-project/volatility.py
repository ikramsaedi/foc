def volatility_lte(levels):
    '''
        Takes in a list of integers `levels` which is a time 
        series of flow levels.
        
        Returns the volatility (integer) the `levels` time series. 
    '''
    
    if len(levels) < 1:
        return
    
    local_min = levels[0]
    local_max = levels[0]
    biggest_diff = 0
    
    for level in levels:
        if level > local_max:
            local_max = level
        if level < local_min:
            local_min = level
            
        # Calculates the value of the difference between two successive max 
        # and minimum values
        local_diff = abs(local_max - local_min)
        
        if local_diff > biggest_diff:
            biggest_diff = local_diff
    
    return biggest_diff
        