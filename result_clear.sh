#!/bin/bash

# Define the target directory
TARGET_DIR="./output_paladin"

# Loop through each subdirectory in the target directory
for dir in "$TARGET_DIR"/*/; do
    # Check if the subdirectory contains any .mp4 files
    if ! find "$dir" -type f -name "*.mp4" | grep -q .; then
        # If no .mp4 files are found, delete the subdirectory
        rm -rf "$dir"
    fi
done