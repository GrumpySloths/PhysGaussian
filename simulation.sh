#!/bin/bash

# Define arrays for model_path, output_path, and config
model_paths=(
    "./model/ficus_whitebg-trained/"
    "./model/wolf_whitebg-trained/"
    "./model/vasedeck_whitebg-trained"
    "./model/pillow2sofa_whitebg-trained"
)
output_paths=(
    "output_ficus"
    "output_wolf"
    "output_vasedeck"
    "output_pillow2sofa"
)
configs=(
    "./config/ficus_config.json"
    "./config/wolf_config.json"
    "./config/vasedeck_config.json"
    "./config/pillow2sofa_config.json"
)

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <index>"
    exit 1
fi

# Get the index from the argument
index=$1

# Check if the index is valid
if [ "$index" -lt 1 ] || [ "$index" -gt ${#model_paths[@]} ]; then
    echo "Invalid index. Please provide a value between 1 and ${#model_paths[@]}."
    exit 1
fi

# Adjust index to be zero-based
index=$((index - 1))

#print the selected configuration
echo "Selected configuration:"
echo "Model path: ${model_paths[$index]}"
echo "Output path: ${output_paths[$index]}"
echo "Config: ${configs[$index]}"
echo ""

# Run the python script with the selected configuration
python gs_simulation.py --model_path "${model_paths[$index]}" --output_path "${output_paths[$index]}" --config "${configs[$index]}" --render_img --compile_video --white_bg
