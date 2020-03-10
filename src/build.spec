# -*- mode: python -*-

BLOCK_CIPHER = None
APP_NAME = 'Pythub'
APP_APP = 'Pythub.app'
APP_VERSION = '0.0.1'
SCRIPTS = ['pythub.py']
BINARIES = []
DATAS = []
HIDDEN_IMPORTS = []  # 源文件的依赖模块
HOOKSPATH = []
EXCLUDES = []  # 不需要打包的模块
RUNTIME_HOOKS = []
BUNDLE_IDENTIFIER = 'com.crogram.pythub'  # 一般情况下Bundle ID的格式为：com.公司名称.项目名称
UPX = True # 如果有UPX安装(执行Configure.py时检测),会压缩执行文件(Windows系统中的DLL也会)
PATHEX = ['aa.py', 'bb.py', 'cc.py', '/Users/douzhenjiang/Projects/pythub/src']

a = Analysis(
    SCRIPTS,
    pathex = PATHEX,
    binaries=BINARIES,
    datas=DATAS,
    hiddenimports=HIDDEN_IMPORTS,
    hookspath=HOOKSPATH,
    runtime_hooks=RUNTIME_HOOKS,
    excludes=EXCLUDES,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=BLOCK_CIPHER,
    noarchive=False
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=BLOCK_CIPHER
)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=UPX,
    console=False
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=UPX,
    name=APP_NAME
)
app = BUNDLE(
    coll,
    name=APP_APP,
    icon=None,
    bundle_identifier=BUNDLE_IDENTIFIER,
    info_plist={
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleExecutable': APP_NAME,
        'CFBundlePackageType': 'APPL',
        'CFBundleSupportedPlatforms': 'MacOSX',
        'CFBundleGetInfoString': "Dou Zhenjiang",
        'CFBundleIdentifier': BUNDLE_IDENTIFIER,
        'CFBundleVersion': APP_VERSION,
        'CFBundleInfoDictionaryVersion': APP_VERSION,
        'CFBundleShortVersionString': APP_VERSION,
        'NSHighResolutionCapable': True,
        'NSHumanReadableCopyright': 'Copyright © 2020, ' + APP_NAME + ', All Rights Reserved'
    }
)
