# Image to ASCII Art Converter

This is a simple Python script that takes any image file and converts it into some seriously cool ASCII art.

## How It Works

It's actually a pretty neat process. The script:

1.  Takes your image and shrinks it down to a more manageable size (so it fits nicely in a text file). It also cleverly adjusts the height to account for the fact that text characters are usually taller than they are wide.
2.  Converts the resized image to grayscale, so we're only dealing with brightness levels.
3.  Goes through the image pixel by pixel.
4.  For each pixel, it checks how bright it is and picks a text character to represent that brightness. Darker pixels get denser characters (like `#` or `&`), while lighter pixels get sparser ones (like `.` or `-`).
5.  Finally, it stitches all those characters together and saves them into a new text file for you.

## Requirements

  * Python 3.13 or newer

## Installation

Getting this set up is super easy.

This project uses **uv** for fast and reliable package management.

1.  First, make sure you have `uv` installed.

2.  Once you have the project code, just run this single command in your terminal:

    ```bash
    uv sync
    ```

    This command will automatically create a virtual environment (`.venv`) and install all the necessary packages specified in the `pyproject.toml` and `uv.lock` files.

3.  To run the script, you'll first need to activate the virtual environment:

    **On macOS/Linux:**

    ```bash
    source .venv/bin/activate
    ```

    **On Windows:**

    ```bash
    .venv\Scripts\activate
    ```

## How to Use It

You run this script from your terminal. The basic command is simple:

```bash
uv run main.py path/to/your/image.jpg
```

This will run the script and create a new file called `output_ascii_art.txt` in the same directory.

### Customizing Your Art

You have a couple of options to play with:

**1. Change the Width**

The default width of the art is 100 characters. If you want something bigger or smaller, use the `-w` (or `--width`) flag.

```bash
# Make the art 150 characters wide
uv run main.py my_cool_picture.png -w 150
```

**2. Change the Output Filename**

Don't like the default filename? No problem. Use the `-o` (or `--output`) flag to name it whatever you want.

```bash
# Save the result to a file named awesome_art.txt
uv run main.py my_cool_picture.png -o awesome_art.txt
```

**3. Combine Options**

You can use both flags at the same time, of course\!

```bash
# Create art that's 200 characters wide and save it as final-piece.txt
uv run main.py my_cool_picture.png -w 200 -o final-piece.txt
```
