# -*- mode: python ; coding: utf-8 -*-
# run with `pyinstaller --clean main.spec` after activating the venv
import os
import sys

PROJECT_ROOT = os.path.abspath('.')
sys.path.insert(0, PROJECT_ROOT)

from PyInstaller.utils.hooks import collect_submodules
from consts import metadata

# Collect all screen modules
hiddenimports = ['screens.GameScreen', 'screens.MainMenu']
hiddenimports += collect_submodules('screens')

title = getattr(metadata, 'SCREEN_TITLE', 'pygame')

a = Analysis(
    ['./main.py'],

    pathex=[
        './',
    ],

    binaries=[],

    datas=[
        ('./assets', 'assets')
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
