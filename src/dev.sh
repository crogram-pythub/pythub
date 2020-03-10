# _*_ coding:utf-8 _*_

pyinstaller\
    --onedir\
    --clean\
    --noconfirm\
    -p aa.py\
    -p bb.py\
    -p cc.py\
    -w\
    --osx-bundle-identifier com.pythub.app\
    --osx-name Pythub\
    pythub.py