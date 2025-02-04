import os

import pandas as pd

for split in ["train", "val", "test"]:
    root_dir = "locust_breeding"
    chips = [
        chip.replace("chip", f"{split}/chips/chip")
        for chip in os.listdir(os.path.join(root_dir, f"{split}/chips"))
    ]
    seg_maps = [
        chip.replace("seg_map", f"{split}/seg_maps/seg_map")
        for chip in os.listdir(os.path.join(root_dir, f"{split}/seg_maps"))
    ]

    df = pd.DataFrame({"Input": chips, "Label": seg_maps})
    df.to_csv(os.path.join(root_dir, f"{split}.csv"))
