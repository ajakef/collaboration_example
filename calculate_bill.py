import numpy as np

def calculate_tip(price_list, tax_rate = 6):
    """
    Calculate the total cost of a restaurant meal.
    Parameters:
    -----------
    price_list : list of floats, prices of all foods/drinks ordered [dollars]
    tax_rate

    Returns:
    --------
    float, total cost of meal
    """
    tax_multiplier = 1 + tax_rate/100
    tip_multiplier = 1.15
    return np.sum(price_list) * tax_multiplier * tip_multiplier


def f(x):
    return np.sum(x) * 1.06 * 1.15
