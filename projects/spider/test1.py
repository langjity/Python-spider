from analysis_chart import *
from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)


# 当窗口关闭后会退出程序

ui = Ui_AanlysisChart()
dialog = QDialog()

# 调用setupUi方法动态创建控件
ui.setupUi(dialog)

# 显示窗口
dialog.show()
sys.exit(app.exec_())
import os
print(os.getcwd())