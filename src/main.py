from PyQt5 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IntelliBeamAnaylzer")
        self.setMinimumSize(1200, 800)
        self.dark_theme = True
        self.current_model = "GPT"
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QHBoxLayout(central_widget)
        splitter = QtWidgets.QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)
        left_panel = QtWidgets.QWidget()
        left_layout = QtWidgets.QVBoxLayout(left_panel)
        chat_display = QtWidgets.QWidget()
        chat_display.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                 QtWidgets.QSizePolicy.Expanding)
        self.input_area = QtWidgets.QTextEdit() 
        font = QFont("Courier New", 12)  
        font.setStyleHint(QFont.Monospace)
        self.input_area.setFont(font)
        self.input_area.setAcceptRichText(False)
        self.input_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.send_button = QtWidgets.QPushButton("Send")
        self.send_button.setFixedWidth(100)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.send_button)
        left_layout.addWidget(chat_display)
        left_layout.addWidget(self.input_area)
        left_layout.addLayout(button_layout)
        self.pdf_viewer = QtWebEngineWidgets.QWebEngineView()
        settings = self.pdf_viewer.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        current_dir = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(current_dir, "index.html")
        url = QtCore.QUrl.fromLocalFile(filename)
        self.pdf_viewer.load(url)
        splitter.addWidget(left_panel)
        splitter.addWidget(self.pdf_viewer)
        splitter.setSizes([400, 800])
        self.create_menu_bar()
        self.send_button.clicked.connect(self.on_send)
        self.input_area.textChanged.connect(self.adjust_input_height)
        self.apply_theme(self.dark_theme)
        QtCore.QTimer.singleShot(0, self.set_initial_height)
   
    def set_initial_height(self):
        left_panel_height = self.height()
        initial_height = left_panel_height // 4
        self.input_area.setMinimumHeight(initial_height)
        self.input_area.setMaximumHeight(initial_height)
        
    def adjust_input_height(self):
        document = self.input_area.document()
        doc_height = int(document.size().height() + 10) 
        min_height = self.height() 
        max_height = self.height() 
        new_height = max(min(doc_height, max_height), min_height)
        self.input_area.setMaximumHeight(new_height)
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_input_height()
        
    def create_menu_bar(self):
        menubar = self.menuBar()
        model_menu = QtWidgets.QMenu('Model', self)
        gpt_action = QtWidgets.QAction('GPT', self)
        claude_action = QtWidgets.QAction('Claude', self)       
        gpt_action.triggered.connect(lambda: self.change_model("GPT"))
        claude_action.triggered.connect(lambda: self.change_model("Claude"))        
        model_menu.addAction(gpt_action)
        model_menu.addAction(claude_action)
        model_button = QtWidgets.QPushButton(f'Model: {self.current_model}')
        model_button.setMenu(model_menu)
        menubar.setCornerWidget(model_button, Qt.TopLeftCorner)
        theme_menu = QtWidgets.QMenu('Theme', self)
        theme_action = QtWidgets.QAction('Light' if self.dark_theme else 'Dark', self)
        theme_action.triggered.connect(self.toggle_theme)
        theme_menu.addAction(theme_action)
        theme_button = QtWidgets.QPushButton('Theme')
        theme_button.setMenu(theme_menu)
        menubar.setCornerWidget(theme_button, Qt.TopRightCorner)
    
    def toggle_theme(self):
        self.dark_theme = not self.dark_theme
        self.apply_theme(self.dark_theme)
        theme_button = self.menuBar().cornerWidget(Qt.TopRightCorner)
        theme_menu = theme_button.menu()
        theme_menu.actions()[0].setText('Light' if self.dark_theme else 'Dark')
    
    def change_model(self, model_name):
        self.current_model = model_name
        model_button = self.menuBar().cornerWidget(Qt.TopLeftCorner)
        model_button.setText(f'Model: {model_name}')
    
    def apply_theme(self, dark):
        if dark:
            self.setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #1e1e1e;
                    color: #ffffff;
                }
                QMenuBar {
                    background-color: #2d2d2d;
                    color: #ffffff;
                }
                QMenuBar::item:selected {
                    background-color: #3d3d3d;
                }
                QMenu {
                    background-color: #2d2d2d;
                    color: #ffffff;
                }
                QMenu::item:selected {
                    background-color: #3d3d3d;
                }
                QTextEdit {
                    background-color: #2d2d2d;
                    color: #ffffff;
                    border: 1px solid #3d3d3d;
                    border-radius: 4px;
                }
                QPushButton {
                    background-color: #0066cc;
                    color: white;
                    border: none;
                    padding: 5px 15px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #0077ee;
                }
                QPushButton:pressed {
                    background-color: #0055bb;
                }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #ffffff;
                    color: #000000;
                }
                QMenuBar {
                    background-color: #f0f0f0;
                    color: #000000;
                }
                QMenuBar::item:selected {
                    background-color: #e0e0e0;
                }
                QMenu {
                    background-color: #f0f0f0;
                    color: #000000;
                }
                QMenu::item:selected {
                    background-color: #e0e0e0;
                }
                QTextEdit {
                    background-color: #ffffff;
                    color: #000000;
                    border: 1px solid #c0c0c0;
                    border-radius: 4px;
                }
                QPushButton {
                    background-color: #0066cc;
                    color: white;
                    border: none;
                    padding: 5px 15px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #0077ee;
                }
                QPushButton:pressed {
                    background-color: #0055bb;
                }
            """)
    
    def on_send(self):
        text = self.input_area.toPlainText()
        if text.strip():
            print(f"Sending text: {text}")
            self.input_area.clear()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow().show()
    sys.exit(app.exec_())
    