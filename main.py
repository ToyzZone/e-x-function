import math
def e_thresh(x: float, threshold: float) -> float:
    '''
    This function calculate e^x by using the sum of a series, with threshold is the epsilon value between the correct e^x with the sum of the series. The smaller the threshold, the more accurate the result.
    If threshold >= 1, the return value will always be 1.0
    
    Requires:
        x can be any real number
        threshold > 0
    '''
    if 1 <= threshold:
        return 1.0
    #The first term is always 1, so if the threshold is greater or equal to the first term, then the series only has 1 term: 1
    
    else:
        n = 0
        result = 0 
        term = x**n/math.factorial(n)
        while abs(term) > threshold:
            term = x**n/math.factorial(n)
            result += term
            n += 1
        return result
