import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1, array2, axis = 0):
    # delete the NotImplementedError when you write your function.
    array1 = array1.squeeze()
    array2 = array2.squeeze()
    if not array1.shape[-1 - axis] == array2.shape[-1 - axis]:
        raise ValueError('All input arrays must have the same shape!')
    else:
        combined_array = np.concatenate((array1, array2), axis)
        return combined_array


if __name__ == "__main__":
    # use this for your own testing!

        a = np.array([[1, 2], [3, 4], [5, 6]])
        b = np.ones((2,2))
        ab = np.concatenate((a, b))
        print(a.shape, b.shape, ab)