def balance_lte(flows1, flows2):
    '''
        Takes in a list of inflows `flows1` and a list of inflows `flows2` 
        of the same length.
        
        Returns the volatility (integer) of the best load balance for 
        `flows1` and `flows2`.
    '''
    
    # Type checks to enforce that flows1 and flows2 are of the same length
    if(len(flows1) != len(flows2)):
        raise Exception("Each time series must be of the same length!")

    # A list of flows that contains each possible combination of padded flows
    delayed_flow_combos = [(flows1, flows2)]
    for i in range(len(flows1) - 1):
        delayed_flow_combos.append(calculate_padding(flows1, flows2, i + 1))
        delayed_flow_combos.append(calculate_padding(flows2, flows1, i + 1))
 
    # For each possible flow combination, calculate their combined load
    combined_loads = []
    for lists in delayed_flow_combos:
        combined_load = list(map(lambda x, y: x + y, lists[0], lists[1]))
        combined_loads.append(combined_load)
    
    # For each combined load, calculate their volatility
    volatilities = []
    for combined_load in combined_loads:
        volatility = max(combined_load) - min(combined_load)
        volatilities.append(volatility)
        
    # The "best" volatility is the lowest volatility, so return that
    return min(volatilities)
   
def calculate_padding(flows1, flows2, padding):
    '''
        Takes in a list of inflows `flows1`, list of inflows `flows2` 
        of the same length, and padding
        
        Returns each flow with the appropriate amount of padding
    '''
    flows1_copy = flows1.copy()
    flows2_copy = flows2.copy()
    
    # Pad each flow by `padding` zeroes
    for _k in range(padding):
        flows1_copy.insert(0, 0)
        flows2_copy.append(0)
    return (flows1_copy, flows2_copy)