
# palindrome function to verify if a number is a palindrome with nb as parameter 
def palindrome(nb):
    """
        function to verify if a number is a palindrome or not
        
        Args:
            nb (int) : a number given by the user
            
        Returns:
           bool : return True if the number is a palindrome, False if it isn't
    """
    
    nb_mirr = str(nb)[::-1] # create nb_mirr variable, the mirror number of nb
    if str(nb) == nb_mirr: # verify if nb is already a palindrome
        return True # if the function return True
    return False # else return False

# nb_mirror function to return the mirror number of nb (parameter)
def nb_mirroir(nb):
    """
        function to get the mirror number of a number
        
        Args:
            nb (int) : a number given by the user
        
        Returns:
            int : return the mirror number of nb
    """
    
    return int(str(nb)[::-1]) # return the mirror number of nb

# main function, verify if nb (user number, parameter) is a lychrel number
def nb_lychrel(nb):
    """
        The main function, verify with the previous function if a number is a lychrel number
        
        Args:
            nb (int) : a number given by the user
        
        Returns:
            bool : return True if the number given by the user is a lychrel number, False if it isn't
    """
    
    if palindrome(nb): # call function palindrome() to verify if nb is already a palindrome
        return nb # if it is function return nb
    else:
        idx = 0 #initialize idx variable 
        while not palindrome(nb): # create a loop while nb is not a palindrome by calling function palindrome()
            nb_mirror = nb_mirroir(nb) # initialize nb_mirror with function nb_mirror to create the mirror of nb 
            nb += nb_mirroir(nb) # add nb_mirror to nb (lychrel number rules)
            if palindrome(nb): # if the new number is a palindrome 
                return nb # return nb if it is
            idx += 1 # add 1 to idx to create the occurence of the loop
            if idx > 300: # verify the number of occurences, if it is more than 300
                return None # return None because the number is not a lychrel number for 300 occurences
            
nb_user = input("For what number do you wanna check if it is a lychrel number ? ") # ask a number to user
print(nb_lychrel(int(nb_user))) # call the function and print the result

# exemple of none lychrel number (300 iterations) : 196
# exemple of lychrel number : 15
