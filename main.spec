# -*- mode: python ; coding: utf-8 -*-
# run with `pyinstaller --clean main.spec` after activating the venv

from PyInstaller.utils.hooks import collect_submodules


# Collect all screen modules
hiddenimports = ['screens.GameScreen', 'screens.MainMenu']
hiddenimports += collect_submodules('screens')


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

    name='Tetris',

    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)
