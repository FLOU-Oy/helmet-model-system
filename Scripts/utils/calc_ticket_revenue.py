import pandas as pd
import os
import openmatrix as omx
import numpy as np

def get_HSL_internal_od_pairs(results_path: str, file_name: str):
    """
    get list of HSL internal od-pairs as network centroids

    Parameters
    ----------
    results_path : str
        path where the file containing the od-pairs is saved
    file_name : str
        name of the file containing the od-pairs is saved

    Returns
    -------
    list
        list of od-pairs as network centroid numbers
    """

    path = os.path.join(results_path, file_name)
    od_pairs_df = pd.read_csv(path, sep="\t")
    od_pairs = list(od_pairs_df.itertuples(index=False, name=None))

    return od_pairs

def get_ticket_revenue(results_path: str, od_pairs_file_name: str):

    # --- Load the demand matrix ---
    demand_file = omx.open_file("demand_aht.omx", mode="r") # TODO: Pitää puukottaa suoraan model-system koodiin, että tulostaa resultsiin demand_vrk.omx, sen saa suoraan EMME-matriiseista exportattuu.
    demand = demand_file["transit_work"][:]

    zone_map = demand_file.mapping("zone_number")
    mapping = {v: k for k, v in zone_map.items()}

    # --- Load the cost matrix ---
    cost_file = omx.open_file("cost_aht.omx", mode="r")
    cost = cost_file["transit_work"][:]

    # --- Close files ---
    demand_file.close()
    cost_file.close()

    # --- Compute total revenue ---
    revenue_matrix = demand * cost

    # Use only HSL internal od pairs to calculate ticket revenue
    od_list = get_HSL_internal_od_pairs(results_path=results_path, file_name=od_pairs_file_name)

    origins_HSL = np.array([mapping[o] for o, d in od_list])
    dests_HSL   = np.array([mapping[d] for o, d in od_list])

    revenue_matrix_HSL = revenue_matrix[origins_HSL, dests_HSL]

    # Print total HSL revenue
    total_revenue_HSL = np.sum(revenue_matrix_HSL)
    print(f"Total revenue for HSL: {total_revenue_HSL :,}")

    # Export revenue matrix
    with omx.open_file("demand_aht.omx", "w") as f:
        f["revenue"] = revenue_matrix
