import doctest


#def longest_word(words):
#    """
#        words is a list of words#

#        return the word from the list with the most characters
#        if multiple words are the longest, return the first 
#        such word        #

#    longest_word(['cat', 'dog', 'bird'])  
#    'bird' #

#    longest_word(['happy', 'birthday', 'my', 'cat'])   
#    'birthday' #

#    longest_word(['happy'])   
#    'happy' #

#    longest_word(['cat', 'dog', 'me']) 
#    'cat' #

#    longest_word(['', ''])  
#    '' 
#    """
#    longest = ''
#    for i in range(0, len(words)):
#        if len(words[i]) > len(longest):
#            longest = words[i]
#    return longest


# test the function with doctest
# doctest.testmod(verbose=True)


def most_students(classroom):

    """
    classroom is a list of lists
    Each ' ' is an empty seat
    Each 'S' is a student  
    How many new students can sit in a row?
    """
    most = 0
    for i in range(0, len(classroom)):
        count = 0
        for j in range(0, len(classroom[i])):
            if classroom[i][j] == 'S':
                count += 1
        if count > most:
            most = count
    return most

doctest.testmod(verbose=True)
