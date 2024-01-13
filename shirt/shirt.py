import sys as s
import os as o
from PIL import Image, ImageOps


def main():
    if len(s.argv) < 3:
        s.exit("Too few command-line arguments")
    elif len(s.argv) > 3:
        s.exit("Too many command-line arguments")
    else:
        input_image = o.path.splitext(s.argv[1])
        output_image = o.path.splitext(s.argv[2])
        if input_image[1] not in [".jpg", ".jpeg", ".png"] or output_image[1] not in [".jpg",".jpeg",".png",]:
            s.exit("Invalid output")
        elif input_image[1] != output_image[1]:
            s.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        with Image.open(s.argv[1]) as file:
            input_cropped = ImageOps.fit(file, shirt.size)
            input_cropped.paste(shirt, mask=shirt)
            input_cropped.save(s.argv[2])
    except FileNotFoundError:
        s.exit(f"Input does not exist")


if __name__ == "__main__":
    main()