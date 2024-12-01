#!/bin/bash

# Check if name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

name=$1
base_dir="model/${name}_whitebg-trained"
target_dir="${base_dir}/point_cloud/iteration_7000"

# Create the target directory
mkdir -p "$target_dir"

# Move the .ply file to the target directory
mv "${name}.ply" "$target_dir/point_cloud.ply"

echo "File moved to ${target_dir}"

# cp cameras.json to the target directory
cp ./model/ficus_whitebg-trained/cameras.json $base_dir

echo "cameras.json copied to ${base_dir}"