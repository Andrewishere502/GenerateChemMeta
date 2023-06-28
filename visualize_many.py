from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

from cluster import ClusterCreator


def load_master_data():
    with open("pp.txt", "r") as file:
        pp_column = [float(num) for num in file.read().split(",")]
    with open("card.txt", "r") as file:
        c_column = [float(num) for num in file.read().split(",")]
    if len(c_column) > len(pp_column):
        pp_column.extend([-1] * (len(c_column) - len(pp_column)))
    else:
        c_column.extend([-1] * (len(pp_column) - len(c_column)))
    df = pd.DataFrame()
    df["Phenylpropanoids"] = pp_column
    df["Cardenolides"] = c_column
    return df


k = 2  # effectively the minimum bucket size

for max_s in range(0, 30):
    # df = pd.read_csv("PP & C Peaks - 2022-06-3009-38-48.csv")

    # df = pd.read_csv("PP & C 250nm Peaks - 2022-07-2113-44-40.csv")

    # df = pd.read_csv("PP & C 250nm Peaks - 2022-07-2509-22-41.csv")
    
    df = pd.read_csv("PP & C 250nm Peaks - 2022-06-2910-10-34.csv")


    cluster_creator_pp = ClusterCreator(df["Phenylpropanoids"], k)
    new_pp_column = cluster_creator_pp.remove_outliers(max_s)
    df["Phenylpropanoids"] = new_pp_column + [-1] * (len(df) - len(new_pp_column))

    cluster_creator_c = ClusterCreator(df["Cardenolides"], k)
    new_c_column = cluster_creator_c.remove_outliers(max_s)
    df["Cardenolides"] = new_c_column + [-1] * (len(df) - len(new_c_column))

    sns.stripplot(df, jitter=0.2)

    plt.show()