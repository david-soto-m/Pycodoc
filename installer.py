#!/usr/bin/python3
# An installer that will create a dektop file and add it to your apps menu
from pathlib import Path
from os import geteuid


def main():
    path1 = str(Path(__file__).parent.resolve()) + '/main.py'
    path2 = str(
        Path(__file__).parent.resolve()
        / 'data'
        / 'AppIcon'
        / 'AppIcon.svg'
    )
    stri = '''\
[Desktop Entry]
Encoding=UTF-8
Type=Application
Terminal=false
Categories=Development;Documentation
Exec=%s
Name=Pycodoc
Icon=%s''' % (path1, path2)
    if geteuid() == 0:
        target = '/usr/share/applications/Pycodoc.desktop'
    else:
        target = str(
            Path.home()
            / '.local'
            / 'share'
            / 'applications'
            / 'Pycodoc.desktop'
        )
    with open(target, 'w+') as f:
        f.write(stri)


if __name__ == '__main__':
    main()
