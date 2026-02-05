# PyGame Template

A mini-framework for PyGame projects.

You only need to write the screens and change the constants in the `consts` folder.
For an example, take a look the the files in the `screens` folder.

## How to run

1. Install Python 3.x
2. run `python -m venv .venv` (change `python` to `python3` for Linux here and forward)
3. run `.\.venv\Scripts\activate` for Windows or `source .venv/bin/activate` for Linux
4. run `python -m pip install -r requirements.txt`
5. run `python -m main` to run the game
6. (Optional) run `pyinstaller --clean main.spec` to create a standalone executable