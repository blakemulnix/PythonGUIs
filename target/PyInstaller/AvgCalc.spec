# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\m165726\\Desktop\\Repos\\PythonGUIs\\src\\main\\python\\average_calculator.py'],
             pathex=['C:\\Users\\m165726\\Desktop\\Repos\\PythonGUIs\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\m165726\\desktop\\repos\\pythonguis\\venv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\m165726\\Desktop\\Repos\\PythonGUIs\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='AvgCalc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , version='C:\\Users\\m165726\\Desktop\\Repos\\PythonGUIs\\target\\PyInstaller\\version_info.py', icon='C:\\Users\\m165726\\Desktop\\Repos\\PythonGUIs\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='AvgCalc')
