import numpy as np
import pandas as pd

train = pd.read_csv("./locust_breeding/records/train.csv")
test = pd.read_csv("./locust_breeding/records/test.csv")
val = pd.read_csv("./locust_breeding/records/val.csv")


# train_indices = np.random.choice(train.index, len(train) // 50, replace=False)
val_indices = np.random.choice(val.index, len(val) // 20, replace=False)
# test_indices = np.random.choice(test.index, len(test) // 50, replace=False)

# train_sample = train.loc[train_indices]
val_sample = val.loc[val_indices]
# test_sample = test.loc[test_indices]


# train_sample.to_csv("./locust_breeding/records/train_sample.csv")
val_sample.to_csv("./locust_breeding/records/val_sample.csv")
# test_sample.to_csv("./locust_breeding/records/test_sample.csv")
