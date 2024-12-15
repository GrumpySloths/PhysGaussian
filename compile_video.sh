#!/bin/bash

# Define the arguments
fps="25"
width="3994"
height="2994"
output_path="output_vasedeck/88686"

ffmpeg -framerate "$fps" -i "$output_path/%04d.png" -c:v libx264 -s "${width}x${height}" \
    -y -pix_fmt yuv420p "$output_path/output.mp4"