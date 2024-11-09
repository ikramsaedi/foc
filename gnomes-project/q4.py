# DO NOT DELETE/EDIT THIS LINE OF CODE, AS IT IS USED TO PROVIDE ACCESS TO
# WORKING IMPLEMENTATIONS OF THE FUNCTIONS FROM Q1, Q2 and Q3. 
from hidden import get_colors_straightforward, make_color_mutex_graph, search

def resolve_colors(evidences):
    '''
        Takes in a list of evidences.
        
        It resolves as many of the gnome ids' colors as it can.
        
        Returns a tuple of sorted gnome ids in white hats, then in black hats.
        If a contradiction is found, it returns None.
    '''
    colors_straight = get_colors_straightforward(evidences)
    negation_edges = make_color_mutex_graph(evidences)
    if colors_straight is None:
        return None
    
    try:
        find_contradictions(colors_straight, negation_edges)
    except:
        return None
    
    # Find the overlap between colors_straight and negation_edges
    # This will give us a starting gnome id and color to traverse the negation
    # edges with, and resolve all other gnome ids that colors_straight has 
    # not resolved already.
    start = None
    for i in range(len(colors_straight)):
        for gnome_id in colors_straight[i]:
            if gnome_id in negation_edges:
                start = (gnome_id, bool(i))
                break
    
    # If there's no overlap, that means we don't have enough information to 
    # resolve all the colors for the gnomes in negation edges.
    if start is None:
        return colors_straight
    
    gnome_tuple = search(negation_edges, {}, start[0], start[1])
    gnome_tuple_reversed = list(reversed(gnome_tuple))
    
    result = []
    for i in range(len(colors_straight)):
        gnome_list = colors_straight[i].copy()
        gnome_list += gnome_tuple_reversed[i]
        unique_gnomes = set(gnome_list)
        sorted_gnome_list = sorted(unique_gnomes)
        result.append(sorted_gnome_list)
    return tuple(result)
    
def find_contradictions(colors_straight, negation_edges):
    '''
        Takes in params:
        - `colors_straight`: a tuple of two sorted lists of gnome_ids for each
        color
        - `negation_edges`: a dictionary mapping gnome ids to a list of
        gnome ids that are different in color
        
        Finds contradictions
    '''
    for gnome_id, gnome_list in negation_edges.items():
        for neg_gnome_id in gnome_list:
            gnome_id_index = None
            neg_gnome_index = None
            # Iterate over both colors straight and negation edges
            for i in range(len(colors_straight)):
                for gnome_id_in_straight in colors_straight[i]:
                    # Compare gnome id in negation edges with gnome id
                    # in straightforward tuple
                    if gnome_id_in_straight == gnome_id:
                        gnome_id_index = i
                    if gnome_id_in_straight == neg_gnome_id:
                        neg_gnome_index = i
            type_check = neg_gnome_index != None and gnome_id_index != None
            
            # If two gnome ids that are supposed to be opposite colors to each 
            # other end up with the same index in the colors_straightforward 
            # tuple, then that means they are the same color
            if type_check and gnome_id_index == neg_gnome_index:
                raise Exception("Contradiction found!")