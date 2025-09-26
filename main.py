from PIL import Image
import math
import argparse

ascii_char_scale = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"


def prepare_image(img_obj, new_width=100):
    """
    Resizes an image and converts it to grayscale.
    """
    width, height = img_obj.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)

    resized_img = img_obj.resize((new_width, new_height))
    grayscale = resized_img.convert("L")
    return grayscale


def assign_ascii_char(brightness):
    """
    Maps a brightness value to a character from the palette.
    """
    percentage = brightness / 255
    char_index = math.floor(percentage * (len(ascii_char_scale) - 1))
    return ascii_char_scale[char_index]


def pixel_to_ascii(img_obj):
    """
    Converts all pixels in the image object to a single string of ASCII characters.
    """
    ascii_str = ""
    data = list(img_obj.getdata())
    for brightness in data:
        char = assign_ascii_char(brightness)
        ascii_str += char
    return ascii_str


def create_ascii_art(img_obj, output_file):
    """
    Takes the final image object and an output filename, formats the ASCII string
    with newlines, and writes it to the specified file.
    """
    ascii_str = pixel_to_ascii(img_obj)
    grayscale_width = img_obj.width
    ascii_str_formatted = ""

    for i in range(0, len(ascii_str), grayscale_width):
        line = ascii_str[i : i + grayscale_width]
        ascii_str_formatted += line + "\n"

    with open(output_file, "w") as f:
        f.write(ascii_str_formatted)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image file to ASCII art.")

    parser.add_argument("file_path", help="Path to the input image file.")
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=100,
        help="Width of the ASCII art in characters (default: 100).",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output_ascii_art.txt",
        help="Name for the output text file (default: output_ascii_art.txt).",
    )

    args = parser.parse_args()

    try:
        img = Image.open(args.file_path)
    except FileNotFoundError:
        print(f"Error: The file '{args.file_path}' was not found.")
        exit()

    prepared_img = prepare_image(img, args.width)

    create_ascii_art(prepared_img, args.output)

    print(f"ASCII art has been successfully saved to '{args.output}'")
