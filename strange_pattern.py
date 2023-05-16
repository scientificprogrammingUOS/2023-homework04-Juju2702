import numpy as np

# implement the function strange pattern

def strange_pattern(input_tuple):
    # delete the NotImplementedError when you write your function.
    n, m = input_tuple
    pattern_array = np.full((n, m), fill_value = False)
    pattern_array[0 : n + 1 : 3, 0 : m + 1 : 3] = True
    pattern_array[1 : n + 1 : 3, 2 : m + 1 : 3] = True
    pattern_array[2 : n + 1 : 3, 1 : m + 1 : 3] = True
    return pattern_array


if __name__ == "__main__":
    # use this for your own testing!
    pass
    
