# -*- mode: python ; coding: utf-8 -*-
# run with `pyinstaller --clean main.spec` after activating the venv
import os
import sys

PROJECT_ROOT = os.path.abspath('.')
sys.path.insert(0, PROJECT_ROOT)

import platform
import pkgutil
import importlib

from PIL import Image
from PyInstaller.utils.hooks import collect_submodules

from consts import metadata

title = getattr(metadata, 'SCREEN_TITLE', 'pygame')
screens_folder = getattr(metadata, 'SCREENS_FOLDER', 'screens')
assets_folder = getattr(metadata, 'ASSETS_FOLDER', 'assets')
icon_path = getattr(metadata, 'GAME_ICON_PATH', 'assets/icon.png')
icon_path = os.path.abspath(icon_path)

def collect_project_submodules():
    modules = []

    pkg = importlib.import_module(screens_folder)

    for _, name, is_pkg in pkgutil.iter_modules(pkg.__path__):
        if not is_pkg:
            modules.append(f"{screens_folder}.{name}")

    return modules

# Collect all screen modules
hiddenimports = collect_project_submodules()
hiddenimports += collect_submodules('screens')

a = Analysis(
    ['./main.py'],

    pathex=[
        './',
    ],

    binaries=[],

    datas=[
        (assets_folder, assets_folder)
    ],

    hiddenimports=hiddenimports,

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)
base, _ = os.path.splitext(icon_path)

def windows_icon(img):
    ico_path = base + ".ico"
    if not os.path.exists(icon_path):
        return None

    sizes = [(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]

    img.save(ico_path, format="ICO", sizes=sizes)
    
    return ico_path

def mac_icon(img):
    icns_path = base + ".icns"
    if not os.path.exists(icon_path):
        return None
        
    sizes = [
        (16,16), (32,32), (64,64),
        (128,128), (256,256),
        (512,512), (1024,1024)
    ]

    icons = []

    for size in sizes:
        icons.append(img.resize(size, Image.LANCZOS))

    icons[0].save(
        icns_path,
        format="ICNS",
        save_all=True,
        append_images=icons[1:]
    )

    return icns_path

def linux_icon(img):
    png_path = base + ".png"
    if not os.path.exists(icon_path):
        return None

    img.save(png_path, format="PNG")

    return png_path

system = platform.system()
img = Image.open(icon_path).convert("RGBA")
if system == "Darwin":
    icon_path = mac_icon(img)
elif system == "Windows":
    icon_path = windows_icon(img)
else:
    icon_path = linux_icon(img)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,

    [],

    name=title,
    icon=icon_path,

    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)
