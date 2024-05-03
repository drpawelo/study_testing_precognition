# Before running the script, make it executable by running chmod +x script_name.sh in the terminal, where 
# script_name.sh is the name of your script file. After that, you can run the script by navigating to the 
# directory where it's saved and executing ./script_name.sh.



#!/bin/bash

# Directory containing the original mp4 files
SOURCE_DIR="../__pool__"

# Directory to save the shortened mp4 files
DEST_DIR="../__pool_short__"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# # Find all video files in the source directory and its subdirectories
find "$SOURCE_DIR" -type f -name "*.avi" | while read -r FILE; do
    # Compute the path of the new file by replacing the source directory with the destination directory
    NEW_FILE="${FILE/$SOURCE_DIR/$DEST_DIR}"
    # Create the directory structure for the new file
    mkdir -p "$(dirname "$NEW_FILE")"
    # Use ffmpeg to create a 1-second clip from the original video
    ffmpeg -y -i "$FILE" -ss 0 -t 1 -c:v copy -c:a copy "$NEW_FILE"

done

# Find all image files in the source directory and its subdirectories
find "$SOURCE_DIR" -type f -name "*.jpg" | while read -r FILE; do
    NEW_FILE="${FILE/$SOURCE_DIR/$DEST_DIR}"
    mkdir -p "$(dirname "$NEW_FILE")"
    cp "$FILE" "$NEW_FILE"
done

# Find all audio files in the source directory and its subdirectories
find "$SOURCE_DIR" -type f -name "*.wav" | while read -r FILE; do
    NEW_FILE="${FILE/$SOURCE_DIR/$DEST_DIR}"
    mkdir -p "$(dirname "$NEW_FILE")"
    ffmpeg -y -i "$FILE" -ss 0 -t 1 -c:a copy "$NEW_FILE"
done