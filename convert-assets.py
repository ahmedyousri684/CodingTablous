import os
from tqdm import tqdm
from PIL import Image
from pathlib import Path

data_path = Path("../woody-ordering-system/src/assets/products/jpg")
save_path = Path("../woody-ordering-system/src/assets/products")

data_list = os.listdir(data_path)


def convert_to_webp(source, destination):
    """Convert image to WebP.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = destination.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


if __name__ == "__main__":
    for img_path in tqdm(os.listdir(data_path)):
        source = data_path / img_path
        destination = save_path / img_path
        convert_to_webp(source, destination)
