def make_color_mutex_graph(evidences):
    '''
        Takes in a list of evidences, which are two tuples. The first element
        is a tuple of 2 gnome ids, and the 2nd element is the frequency of 
        white hats.
        
        Constructs a mutex graph of the gnome ids that are different colors
        to each other.
        
        Returns the graph as a dictionary that has a gnome id (int) keys 
        and a list of sorted gnome ids (integers) as values.
    '''
    graph = {}
    
    for evidence in evidences:
        gnome_ids = evidence[0]
        
        # If there is only one gnome that has a white hat, 
        # then we know that the gnomes are of different colors.
        # This means we can construct the graph from here.
        if evidence[1] == 1:
            for gnome_id in gnome_ids:
                # Fetch the other gnome id in the list of 2 gnome ids
                list_gnome_ids = list(gnome_ids)
                list_gnome_ids.remove(gnome_id)
                other_id = list_gnome_ids[0]
                
                # Add the other id to the list of ids that this gnome id is 
                # different to.
                if graph.get(gnome_id) is not None:
                    graph[gnome_id].append(other_id)
                else:
                    graph[gnome_id] = [other_id]       
    for gnome_id, gnome_list in graph.items():
        gnome_list.sort()
    return graph