# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['blogger.py'],
             pathex=['C:\\Users\\forty\\PycharmProjects\\Blogger'],
             binaries=[],
             datas=[('C:\\Users\\forty\\PycharmProjects\\Blogger\\data_files\\sample.pdf', 'data_files')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='blogger',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\forty\\PycharmProjects\\Blogger\\data_files\\online.ico')
