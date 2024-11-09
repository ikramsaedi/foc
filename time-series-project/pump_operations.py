def pump_operations_lte(capacity, inflows):
    '''
       Takes in an integer `capacity` which is the capacity
       of the tank and a list of integers `inflows` which is the hourly
       inflows of water to the tank.
       
       Returns a list of integers `pumps` which is the number of times
       water was pumped out from the tank at each hour.
    '''
    
    # Type check to ensure capacity and inflows are the correct types
    if isinstance(capacity, int) and capacity < 0: 
        raise Exception("Capacity must be a positive number!")
    if isinstance(inflows, list) and len(inflows) < 1:
        raise Exception("Must have at least one inflow!")
     
    tank_volume = 0
    pumps = []

    for inflow in inflows:
        tank_volume += inflow
        pumps_num = tank_volume // capacity
        pumps.append(pumps_num)
        
        # When the tank volume has reached or overflown the tank's 
        # capacity, we want to pump water out of the tank to
        # keep the tank under capacity
        if(tank_volume >= capacity):
            tank_volume -= capacity * pumps_num
            
    return pumps