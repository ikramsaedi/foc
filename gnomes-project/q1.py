from itertools import groupby

def get_colors_straightforward(evidences):
    '''
        Takes in a list of evidences, which are two tuples. The first element
        is a tuple of 2 gnome ids, and the 2nd element is the frequency of 
        white hats.
        Based on the frequency of white hats in an evidence, it determines
        the color of each gnome.
        Returns a tuple of two sorted lists, the first list being the gnome ids
        with white hats, and the 2nd list being gnome ids with black hats. Or,
        returns None if there was a contradiction.
    '''
    
    # Ensure that evidences is of a valid type
    if type(evidences) is not list or len(evidences) == 0:
        raise TypeError("Evidences must be a non-empty list!")
    
    gnome_to_color = {}
    for evidence in evidences: 
        for gnome_id in evidence[0]:
            # Check for contradictions
            color = gnome_to_color.get(gnome_id)
            if color is not None and color != convert_to_color(evidence[1]):
                return None
            if evidence[1] == 0 or evidence[1] == 2:
                gnome_to_color[gnome_id] = convert_to_color(evidence[1])
    # Group the gnomes by color
    color_to_gnomes = groupby(gnome_to_color, key=lambda x: gnome_to_color[x])
    grouped_lists = [(key, list(value)) for key, value in color_to_gnomes]
    
    # Ensure that the list of gnomes with white hats precede the list of gnomes
    # with black hats.
    sorted_gnomes = sorted(grouped_lists, key=lambda x: x[0], reverse=True)
    
    # Sort each list
    result = [sorted(gnome_list[1]) for gnome_list in sorted_gnomes]
    return tuple(result)

def convert_to_color(num):
    '''
        Takes in a color frequency (integer) from a gnome's evidence.
        Converts it to the relevant color based on the frequency of 
        white or black gnome hats.
        Returns the color (integer).
    '''
    if num == 0:
        return 0
    if num == 2:
        return 1