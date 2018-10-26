import platform
import os
import re
from PyQt4 import QtGui, QtCore
import sys

youku_string = '#优酷loster\n127.0.0.1 atm.youku.com\n' \
               '127.0.0.1 Fvid.atm.youku.com\n' \
               '127.0.0.1 html.atm.youku.com\n' \
               '127.0.0.1 valb.atm.youku.com\n' \
               '127.0.0.1 valf.atm.youku.com\n' \
               '127.0.0.1 valo.atm.youku.com\n' \
               '127.0.0.1 valp.atm.youku.com\n' \
               '127.0.0.1 lstat.youku.com\n' \
               '127.0.0.1 speed.lstat.youku.com\n' \
               '127.0.0.1 urchin.lstat.youku.com\n' \
               '127.0.0.1 stat.youku.com\n' \
               '127.0.0.1 static.lstat.youku.com\n' \
               '127.0.0.1 valc.atm.youku.com\n' \
               '127.0.0.1 vid.atm.youku.com\n' \
               '127.0.0.1 walp.atm.youku.com\n'


class Host_QWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.system_version = QtGui.QLabel(self)
        button = QtGui.QPushButton('remove youku add', self)
        self.tip = QtGui.QLabel(self)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.system_version, 0, 0, QtCore.Qt.AlignCenter)
        grid.addWidget(button, 1, 0)
        grid.addWidget(self.tip, 2, 0, QtCore.Qt.AlignCenter)

        self.resize(300, 300)
        self.setLayout(grid)
        self.setWindowTitle('remove ad by loster')

        self.connect(button, QtCore.SIGNAL('clicked()'), chuli)

    def setSystem_version(self, version):
        self.system_version.setText(version)

    def setTip(self, tipText):
        self.tip.setText(tipText)


def chuli():
    Host.setSystem_version(getSystem_version())
    if isExist():
        Host.setTip('Has written')
    else:
        write2Hosts()
        Host.setTip('finish')


def getSystem_version():
    System_v = platform.platform()
    return System_v


# 判断是否已经写入
def isExist():
    hosts = open(HostsPath, 'r')
    result = hosts.read()
    reg = re.compile('loster')
    tag = re.findall(reg, result)
    hosts.close()
    # reg=result.find('loster')
    return tag


# 写入网址
def write2Hosts():
    # 更改权限，可写
    os.chmod(HostsPath, 33206)
    # 打开一个文件,以追加的模式写入
    hosts = open(HostsPath, 'a')
    # 写入数据
    hosts.write(youku_string)
    # 关闭
    hosts.close()
    # 将权限改为只读
    os.chmod(HostsPath, 33060)


if __name__ == '__main__':
    HostsPath = 'C:\Windows\System32\drivers\etc\hosts'
    app = QtGui.QApplication(sys.argv)
    Host = Host_QWidget()
    Host.setSystem_version(getSystem_version())
    Host.show()
    sys.exit(app.exec_())

    # 获取系统版本
    # System_Version = platform.platform()
    # print(System_Version)
