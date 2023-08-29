import doctest

def most_students(classroom):

    """
    classroom is a list of lists
    Each ' ' is an empty seat
    Each 'S' is a student
    
    Return the maximum total number of ' ' characters in a
    given row.
    
    >>> most_students([['S', 'S', 'S', 'S', 'S', 'S'], \
                       ['S', 'S', 'S', 'S', 'S', 'S'], \
                       ['S', 'S', 'S', 'S', 'S', 'S']])  
    0

    >>> most_students([['S', ' ', ' ', ' ', 'S', 'S'], \
                       ['S', 'S', 'S', 'S', 'S', 'S'], \
                       ['S', 'S', 'S', 'S', 'S', 'S']])  
    3
    
    >>> most_students([['S', ' ', ' '], \
                       [' ', 'S', ' '], \
                       [' ', ' ', 'S']])  
    2
    """
    max_seats = 0
    for row in classroom:
        seats = row.count(' ')
        if seats > max_seats:
            max_seats = seats
    return max_seats

doctest.testmod(verbose=True)
