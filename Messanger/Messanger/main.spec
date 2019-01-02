# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.pyw'],
             pathex=['D:\\Yandex\\Programming\\Кооперативная разработка\\Quinkokolobicky\\ShiWarai\\quinkokolobicky\\Messanger\\Messanger'],
             binaries=[],
             datas=[('data/sound.wav', '.')],
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , version='version.rc', icon='app.ico')
