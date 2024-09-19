# -*- mode: python ; coding: utf-8 -*-
import sys

if sys.platform.startswith('darwin'):
    lib_extensions = ['.dylib']
    binaries = []
    for lib_name in ['libggml_llama', 'libllama', 'libllava', 'libstable-diffusion']:
        binaries.append((f'./nexa/gguf/lib/{lib_name}{lib_extensions[0]}', './nexa/gguf/lib'))

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

    pyz = PYZ(a.pure, a.zipped_data,
              cipher=None)

    exe = EXE(pyz,
              a.scripts,
              a.binaries,
              a.zipfiles,
              a.datas,
              [],
              name='nexa',
              debug=False,
              bootloader_ignore_signals=False,
              strip=False,
              upx=True,
              upx_exclude=[],
              runtime_tmpdir=None,
              console=True,
              disable_windowed_traceback=False,
              argv_emulation=False,
              target_arch=None,
              codesign_identity=None,
              entitlements_file=None)