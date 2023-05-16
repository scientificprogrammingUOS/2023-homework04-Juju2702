import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    # delete the NotImplementedError when you write your function.
    if not all((isinstance(i, int) or isinstance(i, float)) for i in [loc, scale, lower_bound, upper_bound]):
        raise TypeError("Make sure that all parameters are either of type int or float!")
    elif lower_bound >= upper_bound:
        raise ArithmeticError("The parameter lower_bound has to be smaller than upper_bound!")
    else:
        sample_values = np.random.normal(loc, scale, size = 10)
        mask = (sample_values > lower_bound) & (sample_values < upper_bound)
        filtered_values = sample_values[mask]
        mean = np.sum(filtered_values) / filtered_values.size
        std = np.sqrt((np.sum((filtered_values - loc) ** 2) / filtered_values.size))
        return ((mean, std))


if __name__ == "__main__":
    # use this for your own testing!
    pass