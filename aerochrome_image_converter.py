#!/usr/bin/env python3

import os
import re
from pathlib import Path
from PIL import Image

def find_highest_number(folder_path):
    path = Path(folder_path)
    numbered_files = [file for file in path.iterdir() if file.is_file() and re.search(r'\d+', file.name)]

    if not numbered_files:
        return 0

    numbers = [int(re.search(r'\d+', file.name).group()) for file in numbered_files]
    return max(numbers)

def invert_channels(image):
    r, g, b = image.split()
    return Image.merge('RGB', (b, r, g))

def main():
    # Open image
    image_path = 'TEST1.JPG' #image you wish to convert
    image = Image.open(image_path)

    # Separate and merge channels
    result = invert_channels(image)

    # Set up folder path
    folder_path = Path('----') #Save location

    # Find the highest number in existing files
    num = find_highest_number(folder_path) + 1

    # Save the image
    result_path = folder_path / f'{num}.JPG'
    result.save(result_path)
    
main()
