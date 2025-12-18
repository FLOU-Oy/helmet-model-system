## Imports ##

transit_zones_HSL = {'A','B','C','D'}

ticket_types_HSL = {
    ('A', 'A'): "AB",
    ('A', 'B'): "AB",
    ('A', 'C'): "ABC",
    ('A', 'D'): "ABCD",
    ('B', 'A'): "AB",
    ('B', 'B'): "AB",
    ('B', 'C'): "BC",
    ('B', 'D'): "BCD",
    ('C', 'A'): "ABC",
    ('C', 'B'): "BC",
    ('C', 'C'): "BC",
    ('C', 'D'): "CD",
    ('D', 'A'): "ABCD",
    ('D', 'B'): "BCD",
    ('D', 'C'): "CD",
    ('D', 'D'): "CD",
}

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