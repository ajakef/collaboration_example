import numpy as np

def calculate_tip(price_list, tip_rate = 15):
    """
    Calculate the total cost of a restaurant meal.
    Parameters:
    -----------
    price_list : list of floats, prices of all foods/drinks ordered [dollars]

    Returns:
    --------
    float, total cost of meal
    """
    tax_multiplier = 1.06
    tip_multiplier = 1 + tip_rate/100
    return np.sum(price_list) * tax_multiplier * tip_multiplier


def f(x):
    return np.sum(x) * 1.06 * 1.15
