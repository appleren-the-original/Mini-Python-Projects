# -*- mode: python -*-

block_cipher = None


a = Analysis(['client_of_chat.py'],
             pathex=['C:\\Users\\alpge\\Documents\\Python çalışmalar\\chat app\\cli_exe'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='client_of_chat',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
