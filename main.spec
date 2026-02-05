# -*- mode: python ; coding: utf-8 -*-
# run with `pyinstaller --clean main.spec` after activating the venv
import os
import sys
import pkgutil
import importlib

PROJECT_ROOT = os.path.abspath('.')
sys.path.insert(0, PROJECT_ROOT)

from PyInstaller.utils.hooks import collect_submodules
from consts import metadata

title = getattr(metadata, 'SCREEN_TITLE', 'pygame')
screens_folder = getattr(metadata, 'SCREENS_FOLDER', 'screens')
assets_folder = getattr(metadata, 'ASSETS_FOLDER', 'assets')

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


exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,

    [],

    name=title,

    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)
