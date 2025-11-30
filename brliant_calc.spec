# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['brliant_calc\\__main__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'brliant_calc.basic_ops',
        'brliant_calc.advanced_ops',
        'brliant_calc.convert_currency',
        'brliant_calc.vectors',
        'brliant_calc.physics_formulas',
        'brliant_calc.units',
        'brliant_calc.matrix_ops',
        'brliant_calc.complex_ops',
        'brliant_calc.symbolic_ops',
        'brliant_calc.plotting',
        'brliant_calc.dimensional_analysis',
        'brliant_calc.precision_ops',
        'brliant_calc.alias_manager',
        'currency_converter',
        'pint',
        'sympy',
        'numpy',
        'matplotlib'
    ],
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
    [],
    exclude_binaries=True,
    name='brliant_calc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='brliant_calc',
)
