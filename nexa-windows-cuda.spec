# -*- mode: python ; coding: utf-8 -*-
import sys

# Determine the correct file extension based on the operating system
if sys.platform.startswith('win'):
    lib_extensions = ['.dll', '.lib']

    binaries = []

    for lib_name in ['ggml_llama', 'llama', 'llava', 'stable-diffusion']:
        for ext in lib_extensions:
            binaries.append((f'./nexa/gguf/lib/{lib_name}{ext}', './nexa/gguf/lib'))
        
    binaries.append('./nexa/gguf/lib/empty_file.txt', './nexa/gguf/lib')

    a = Analysis(['./nexa/cli/entry.py'],
                pathex=[],
                binaries=binaries,
                datas=[],
                hiddenimports=[],
                hookspath=[],
                runtime_hooks=[],
                excludes=[],
                win_no_prefer_redirects=False,
                win_private_assemblies=False,
                cipher=None,
                noarchive=False)

    pyz = PYZ(a.pure)

    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='nexa-windows-cuda',
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
        name='nexa-windows-cuda',
    )
