#!/bin/bash
# Remove the checkpoint file if it exists
if [ -f "outputs/first_run/last.ckpt" ]; then
    rm "outputs/first_run/last.ckpt"
fi
# Train the InstaGeo model using the custom Locust configuration
python -m instageo.model.run --config-name=custom-locust \
    hydra.run.dir="outputs/first_run" \
    root_dir="locust_breeding" \
    train.batch_size=8 \
    train.num_epochs=5 \
    mode=train \
    train_filepath="train.csv" \
    valid_filepath="val.csv"

# Evaluate the trained model
python -m instageo.model.run --config-name=custom-locust \
    root_dir="locust_breeding" \
    test_filepath="val.csv" \
    train.batch_size=16 \
    checkpoint_path='outputs/first_run/last.ckpt' \
    mode=eval