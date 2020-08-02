import re
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    pass
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    pass


if __name__ == '__main__' :
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))
