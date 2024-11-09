from itertools import groupby

def search(negation_edges, visited, start, color):
    '''
        Takes in:
        - negation_edges: a dictionary mapping gnome ids to a list of
        gnome ids that are different in color
        - visited: a dictionary of already visited gnomes in the graph
          key: gnome id (int) to value: color (bool).
        - start: gnome id (int) 
        - color: bool 
        
        `search` traverses the negation edges, starting at the `start` using
        depth first search.
        
       Returns a tuple of two sorted lists of gnome ids, the first list being
       of gnomes with white hats, and the second is of gnomes with black hats.
    '''
    
    # Transform the colors so that they're easier to work with
    for key in visited.keys():
        original_color = visited[key]
        visited[key] = not original_color
        
    try:
        gnome_color = dfs(negation_edges, visited, start, color)
    except ValueError:
        return None
    
    # Get a dictionary of gnomes with their colors specified
    sorted_gnome_color = sorted(gnome_color, key=lambda x: gnome_color[x])
    color_to_gnomes = groupby(sorted_gnome_color, key=lambda x: gnome_color[x])
    
    # Convert color_to_gnomes to dictionary
    color_gnomes_dict = {}
    for color, gnomes in color_to_gnomes:
        color_gnomes_dict[color] = list(gnomes)

    # Ensure that there is always a tuple for gnomes that have a black hat
    # And a tuple for gnomes that have a white hat even if there are none
    # present
    if True not in color_gnomes_dict:
        color_gnomes_dict[True] = []
    if False not in color_gnomes_dict:
        color_gnomes_dict[False] = []
    
    groups = [(key, list(group)) for key, group in color_gnomes_dict.items()]
    
    # Sort it so that white hats are first, and black hats are second
    sorted_groups = sorted(groups, reverse=True)
    sorted_grouped_lists = [sorted(group[1]) for group in sorted_groups]
    return tuple(sorted_grouped_lists)
    
def dfs(negation_edges, visited, start, color):
    '''
        Takes in:
        - negation_edges: a dictionary mapping gnome ids to a list of
        gnome ids that are different in color
        - visited: a dictionary of already visited gnomes in the graph
          key: gnome id (int) to value: color (bool).
        - start: gnome id (int) 
        - color: bool 
        
        `dfs` traverses the negation edges, starting at the `start` using
        depth first search.
        
        It returns a dictionary of `visited` gnome id to colors after it has
        finished traversing the graph.
    '''
    # If the start is already in visited, then there's no need to unnecessarily
    # continue traversing through its neighbours
    if start in visited:
        return visited
    visited[start] = color
    new_color = not color
    
    find_contradictions(negation_edges[start], visited, new_color)

    # Get the unique gnomes
    visited_gnomes = set(visited.keys())

    # Exclude visited gnomes from the iteration
    for gnome_id in negation_edges[start] - visited_gnomes:
        if gnome_id not in visited:
            dfs(negation_edges, visited, gnome_id, new_color)
    return visited

def find_contradictions(neighbours, visited, new_color):
    '''
        Takes in a list of `neighbours` gnome ids, a dictionary of nodes
        in the graph that have been visited already, and a `new_color` (bool)
        
        It compares the color in the visited dictionary with the new color.
        If they are different, then there's a contradiction and it raises 
        an error.
        
        Returns nothing.
    '''
    for gnome_id in neighbours:
        if gnome_id in visited and visited[gnome_id] != new_color:
            raise ValueError("Contradiction found!")