## Imports ##

transit_zones_HSL = {'A','B','C','D'}

def ticket_cost(distance, cost_fn):
    """
    Calculate ticket cost based on a beeline distance and a cost function.

    Parameters
    ----------
    distance : float
        Beeline distance between two points.
    cost_fn : callable
        A function that takes `distance` as input and returns a cost.

    Returns
    -------
    float
        Calculated ticket cost.
    """
    if distance < 0:
        raise ValueError("Distance cannot be negative.")
    if not callable(cost_fn):
        raise TypeError("cost_fn must be a callable function.")

    return cost_fn(distance)


def simple_cost(distance):
    base_fee = 5
    per_km = 0.4
    ceiling_fee = 10

    trip_cost = base_fee + distance * per_km

    if trip_cost > ceiling_fee:
        trip_cost = ceiling_fee

    return trip_cost