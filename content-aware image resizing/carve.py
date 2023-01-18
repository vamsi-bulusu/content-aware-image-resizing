"""
The third and final step in the seam carving process: removing the lowest-energy
seam from an image. By doing so iteratively, the size of the image can be
reduced (in one dimension) by multiple pixels.

The functions you fill out in this module put together everything you've written
so far into the full seam carving algorithm. Run this module in isolation to
resize your image!

    python3 carve.py surfer.jpg 10 surfer-resized.png
"""


import sys

from energy import compute_energy
from seam_v2 import compute_vertical_seam_v2, visualize_seam_on_image
from utils import Color, read_image_into_array, write_array_into_image


def remove_seam_from_image(image, seam_xs):
    """
    Remove pixels from the given image, as indicated by each of the
    x-coordinates in the input. The x-coordinates are specified from top to
    bottom and span the entire height of the image.

    This is one of the functions you will need to implement. Expected return
    value: the 2D grid of colors. The grid will be smaller than the input by
    one element in each row, but will have the same number of rows.
    """
    resized_image = []

    for row in range(len(image)):
        temp_row = []
        for col in range(len(image[0])):
            if col != seam_xs[row]:
                temp_row.append(image[row][col])
        resized_image.append(temp_row)
    return resized_image

    # raise NotImplementedError('remove_seam_from_image is not implemented')


def remove_n_lowest_seams_from_image(image, num_seams_to_remove):
    """
    Iteratively:

    1. Find the lowest-energy seam in the image.
    2. Remove that seam from the image.

    Repeat this process `num_seams_to_remove` times, so that the resulting image
    has that many pixels removed in each row.

    While not necessary, you may want to save the intermediate images in the
    process, in case you want to see how the image gets progressively smaller.
    The `visualize_seam_on_image` is available if you want to visualize the
    lowest-energy seam at each step of the process.

    This is one of the functions you will need to implement. Expected return
    value: the 2D grid of colors. The grid will be smaller than the input by
    `num_seams_to_remove` elements in each row, but will have the same number of
    rows.
    """

    seam_count = 1
    while seam_count <= num_seams_to_remove:
        energy_data = compute_energy(image)
        seam_xs, total_seam_energy = compute_vertical_seam_v2(energy_data)
        image = remove_seam_from_image(image, seam_xs)
        visualized_pixels = visualize_seam_on_image(image, seam_xs)
        filename = 'surfer-resized-visual-' + str(seam_count) + '.png'
        write_array_into_image(visualized_pixels, filename)
        seam_count += 1
    return image

    # raise NotImplementedError('remove_n_lowest_seams_from_image is not implemented')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'USAGE: {__file__} <input> <num-seams-to-remove> <output>')
        sys.exit(1)

    input_filename = sys.argv[1]
    num_seams_to_remove = int(sys.argv[2])
    output_filename = sys.argv[3]

    print(f'Reading {input_filename}...')
    pixels = read_image_into_array(input_filename)

    print(f'Saving {output_filename}')
    resized_pixels = \
        remove_n_lowest_seams_from_image(pixels, num_seams_to_remove)
    write_array_into_image(resized_pixels, output_filename)
