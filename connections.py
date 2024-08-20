from ui_main_window import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QTextCursor
from functions import delete_temp_files, delete_system_temp, delete_prefetch_files, app_logs, log_files, update_logs
from PyQt6.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def run(self):
        results = []
        if self.ui.tempFiles.isChecked():
            results.append(delete_temp_files(self.ui))
        if self.ui.systemTemp.isChecked():
            results.append(delete_system_temp(self.ui))
        if self.ui.prefetch.isChecked():
            results.append(delete_prefetch_files(self.ui))
        if self.ui.appLogs.isChecked():
            results.append(app_logs(self.ui))
        if self.ui.logFiles.isChecked():
            results.append(log_files(self.ui))
        if self.ui.updateLogs.isChecked():
            results.append(update_logs(self.ui))
        # Gabungkan hasil jika ada beberapa
        result_text = '\n'.join(filter(None, results))
        self.result_signal.emit(result_text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.run_action)

    def run_action(self):
        self.thread = WorkerThread(self.ui)
        self.thread.result_signal.connect(self.update_textedit)
        self.thread.start()

    def update_textedit(self, result):
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(result + '\n')
        self.ui.textEdit.setTextCursor(cursor)
        self.ui.textEdit.ensureCursorVisible()
