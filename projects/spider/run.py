import sys
import main
from main_event import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow

def bind_event(ui):
    ui.pushbutton_fetch_goods_list.clicked.connect(lambda : main_event.onclick_fetch_goods_list())
    ui.pushbutton_search.clicked.connect(lambda :main_event.onclick_search())
    ui.pushbutton_load_goods_list.clicked.connect(lambda : main_event.onclick_load_goods_list())
    palette = ui.lcdnumber_pages.palette()
    palette.setColor(palette.WindowText, QColor(255, 0, 0))
    ui.lcdnumber_pages.setPalette(palette)

    palette = ui.lcdnumber_every_page_goods_number.palette()
    palette.setColor(palette.WindowText, QColor(0, 0, 255))
    ui.lcdnumber_every_page_goods_number.setPalette(palette)

    palette = ui.lcdnumber_time.palette()
    palette.setColor(palette.WindowText, QColor(255, 0, 255))
    ui.lcdnumber_time.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main.Ui_MainWindow()
    main_event = MainEvent(ui)
    # 调用setupUi方法动态创建控件
    ui.setupUi(MainWindow)
    bind_event(ui)
    # 显示窗口
    MainWindow.show()
    # 当窗口关闭后会退出程序
    sys.exit(app.exec_())