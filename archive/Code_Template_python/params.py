import numpy as np

def initialize() -> dict:
    """This function sets some default values for parameters 
     used in the algorithm 
     
     Returns:
     - options: Dictionary with all parameters needed for a given algorithm
     """

    ### Armijo line search parameters
    options = {}
    options['c1'] = 10^-4
    

    ### etc.... You can initialeize the deafult values here. 
    return options

