###############################
# IMPORTS
###############################
import sys
import os
import ctypes
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter,
    QLabel, QPushButton, QTextEdit, QLineEdit, QListWidget, QListWidgetItem,
    QFrame, QStackedWidget, QScrollArea, QMessageBox
)
from PyQt6.QtGui import QFont, QIcon, QPixmap, QColor, QPalette, QLinearGradient, QPainter, QMovie
from PyQt6.QtCore import Qt, QSize

from src.logging import init_logging, get_logger, get_log_file_path


###############################
# GLOBAL CONFIG
###############################
DEBUG_MODE = False
LOG_FILE = 'log/redengine.log'
LOGO_PATH = 'assets/logo.gif'

init_logging()
logger = get_logger()

###############################
# ERROR DEFINITIONS
###############################
ERROR_LIST = [
    {
        "id": "#1",
        "description": "Fix #1",
        "fix_func": "fix_1"
    },
    {
        "id": "#2",
        "description": "Fix #2",
        "fix_func": "fix_2"
    },
    {
        "id": "#3",
        "description": "Fix #3",
        "fix_func": "fix_3"
    },
    {
        "id": "#4",
        "description": "Fix #4",
        "fix_func": "fix_4"
    }
]

###############################
# ERROR HANDLER CLASS
###############################
class ErrorHandler:
    def __init__(self, ui):
        self.ui = ui
        self.errors = []
        
    def load_errors(self):
        self.errors = ERROR_LIST
        for error in self.errors:
            self.ui.add_error_item(error["id"], error["description"], error["fix_func"])
        
    def fix_error(self, error_id, fix_func):
        logger.info(f"Fixing error: {error_id}")
        # Call fix function based on name
        if hasattr(self, fix_func):
            getattr(self, fix_func)()
        self.show_fix_confirmation(error_id)

################################
# ERROR FIXES
################################


    # Fix functions
    def fix_1(self):
        logger.info("Fixxed #1")
        
    def fix_2(self):
        logger.info("Fixxed #2")
        
    def fix_3(self):
        logger.info("Fixxed #3")
        
    def fix_4(self):
        logger.info("Fixxed #4")
    
    


##############################
# CONFIRMATION DIALOG
##############################

    def show_fix_confirmation(self, error_id):
        msg = QMessageBox(self.ui)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Fix Applied")
        msg.setText(f"Auto fix applied for: {error_id}")
        msg.setInformativeText("The issue should habe been resolved successfully.")
        msg.setStyleSheet("""
            QMessageBox { background-color: #151515; color: #ddd; }
            QLabel { color: #ddd; }
            QPushButton { 
                background-color: #d32f2f; color: white;
                min-width: 80px; padding: 8px; border-radius: 4px;
            }
            QPushButton:hover { background-color: #f44336; }
        """)
        msg.exec()

###############################
# MAIN APPLICATION CLASS
###############################
class RedEngineSupportTool(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("redENGINE Support Tool")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(self.create_icon())
        self.setStyleSheet(self.get_style_sheet())
        self.init_ui()
        self.error_handler = ErrorHandler(self)
        self.error_handler.load_errors()

    def get_style_sheet(self):
        return """
            QMainWindow { background-color: #0d0d0d; }
            QSplitter::handle { background-color: #333; width: 1px; }
            QFrame { background-color: #151515; border-radius: 8px; }
            QPushButton { 
                background-color: #d32f2f; color: #fff; border: none;
                border-radius: 6px; padding: 10px 18px; font-weight: bold;
                min-width: 100px; font-size: 13px;
            }
            QPushButton:hover { background-color: #f44336; }
            QPushButton:pressed { background-color: #b71c1c; }
            QListWidget { 
                background-color: #151515; color: #ddd; border: none;
                font-size: 14px; padding: 5px; outline: none;
            }
            QListWidget::item { 
                padding: 15px 20px; border-radius: 6px; margin: 5px;
            }
            QListWidget::item:selected { background-color: #d32f2f; color: white; }
            QTextEdit, QLineEdit { 
                background-color: #1a1a1a; color: #ddd; border: none;
                border-radius: 6px; padding: 12px; font-size: 14px;
                selection-background-color: #d32f2f;
            }
            QLabel { color: #ddd; font-family: 'Segoe UI', Arial, sans-serif; }
            QScrollArea { border: none; background: transparent; }
            QScrollBar:vertical { border: none; background: #151515; width: 10px; }
            QScrollBar::handle:vertical { 
                background: #d32f2f; border-radius: 4px; min-height: 20px;
            }
        """

    def create_icon(self):
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        gradient = QLinearGradient(0, 0, 64, 64)
        gradient.setColorAt(0, QColor("#ff5252"))
        gradient.setColorAt(1, QColor("#d32f2f"))
        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, 64, 64, 16, 16)
        painter.end()
        return QIcon(pixmap)

    def init_ui(self):
        
        
        
        
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(0)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        sidebar = QFrame()
        sidebar.setMinimumWidth(280)
        sidebar.setMaximumWidth(300)
        sidebar.setStyleSheet("background-color: #121212; border-radius: 10px;")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(15, 20, 15, 20)
        sidebar_layout.setSpacing(20)

        # Logo and title
        logo_title_layout = QHBoxLayout()
        logo_title_layout.setSpacing(15)
        logo_label = QLabel()
        if os.path.exists(LOGO_PATH):
            movie = QMovie(LOGO_PATH)
            logo_label.setMovie(movie)
            movie.start()
        else:
            logo_label.setText("RE")
            logo_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
            logo_label.setStyleSheet("color: #d32f2f;")
        logo_title_layout.addWidget(logo_label)

        title = QLabel("redENGINE")
        title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))
        title.setStyleSheet("""
            color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #ff5252, stop:1 #d32f2f);
        """)
        logo_title_layout.addWidget(title)
        logo_title_layout.addStretch()
        sidebar_layout.addLayout(logo_title_layout)

        # Navigation tabs
        self.tab_list = QListWidget()
        tabs = ["Support Center", "Settings", "System Logs", "Documentation"]
        for tab_name in tabs:
            item = QListWidgetItem(tab_name)
            item.setSizeHint(QSize(40, 60))
            item.setFont(QFont("Segoe UI", 12))
            self.tab_list.addItem(item)
        self.tab_list.setCurrentRow(0)
        self.tab_list.currentRowChanged.connect(self.switch_tab)
        sidebar_layout.addWidget(self.tab_list)
        sidebar_layout.addStretch()

        # Version label
        version = QLabel("v2.0.1")
        version.setStyleSheet("color: #666; font-size: 11px;")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(version)

        # Main content area
        self.main_content = QStackedWidget()
        self.create_support_tab()
        self.create_settings_tab()
        self.create_logs_tab()
        self.create_docs_tab()

        splitter.addWidget(sidebar)
        splitter.addWidget(self.main_content)
        splitter.setSizes([280, 800])
        main_layout.addWidget(splitter)
        self.setCentralWidget(main_widget)

    def create_support_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        
        # Header
        header = QFrame()
        header.setStyleSheet("background-color: #151515; border-radius: 8px;")
        hlayout = QVBoxLayout(header)
        hlayout.setContentsMargins(20, 20, 20, 20)
        hlayout.addWidget(QLabel("Support Center", font=QFont("Segoe UI", 18, QFont.Weight.Bold)))
        desc = QLabel("Find solutions to common issues and errors")
        desc.setFont(QFont("Segoe UI", 11))
        desc.setStyleSheet("color: #aaa;")
        hlayout.addWidget(desc)
        layout.addWidget(header)
        
        # Search bar
        search_frame = QFrame()
        search_layout = QHBoxLayout(search_frame)
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search errors...")
        self.search_bar.textChanged.connect(self.filter_errors)
        search_layout.addWidget(self.search_bar)
        layout.addWidget(search_frame)
        
        # Error list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        self.error_layout = QVBoxLayout(content)
        self.error_layout.addStretch()
        scroll.setWidget(content)
        layout.addWidget(scroll, 1)
        self.main_content.addWidget(tab)

    def create_settings_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        header = QFrame()
        header.setStyleSheet("background-color: #151515; border-radius: 8px;")
        hlayout = QVBoxLayout(header)
        hlayout.setContentsMargins(20, 20, 20, 20)
        hlayout.addWidget(QLabel("Settings", font=QFont("Segoe UI", 18, QFont.Weight.Bold)))
        desc = QLabel("Configure tool preferences and global settings")
        desc.setFont(QFont("Segoe UI", 11))
        desc.setStyleSheet("color: #aaa;")
        hlayout.addWidget(desc)
        layout.addWidget(header)
        
        # Update button
        btn = QPushButton("Check for Updates")
        btn.setFixedHeight(50)
        btn.clicked.connect(self.check_for_updates)
        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        self.main_content.addWidget(tab)

    def create_logs_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        header = QFrame()
        header.setStyleSheet("background-color: #151515; border-radius: 8px;")
        hlayout = QVBoxLayout(header)
        hlayout.setContentsMargins(20, 20, 20, 20)
        hlayout.addWidget(QLabel("System Logs", font=QFont("Segoe UI", 18, QFont.Weight.Bold)))
        desc = QLabel("View diagnostic information and tool activity")
        desc.setFont(QFont("Segoe UI", 11))
        desc.setStyleSheet("color: #aaa;")
        hlayout.addWidget(desc)
        layout.addWidget(header)
        
        # Button layout
        button_layout = QHBoxLayout()
        
        # Refresh button
        refresh_btn = QPushButton("Refresh Logs")
        refresh_btn.clicked.connect(self.load_log_file)
        button_layout.addWidget(refresh_btn)
        
        # Clear log button
        clear_btn = QPushButton("Clear Log")
        clear_btn.clicked.connect(self.clear_log_file)
        button_layout.addWidget(clear_btn)
        
        layout.addLayout(button_layout)
        
        # Log view
        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setStyleSheet("font-family: 'Courier New';")
        layout.addWidget(self.log_view, 1)
        
        # Load log file initially
        self.load_log_file()
        
        self.main_content.addWidget(tab)

    def create_docs_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        header = QFrame()
        header.setStyleSheet("background-color: #151515; border-radius: 8px;")
        hlayout = QVBoxLayout(header)
        hlayout.setContentsMargins(20, 20, 20, 20)
        hlayout.addWidget(QLabel("Documentation", font=QFont("Segoe UI", 18, QFont.Weight.Bold)))
        desc = QLabel("Official documentation and troubleshooting guides")
        desc.setFont(QFont("Segoe UI", 11))
        desc.setStyleSheet("color: #aaa;")
        hlayout.addWidget(desc)
        layout.addWidget(header)
        
        # Placeholder
        placeholder = QLabel("Documentation will be available in future releases")
        placeholder.setFont(QFont("Segoe UI", 12))
        placeholder.setStyleSheet("color: #aaa;")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(placeholder, 1)
        self.main_content.addWidget(tab)
        
    def load_log_file(self):
        """Load and display log file content"""
        try:
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r') as f:
                    self.log_view.setPlainText(f.read())
            else:
                self.log_view.setPlainText("Log file not found. It will be created after first log entry.")
        except Exception as e:
            self.log_view.setPlainText(f"Error reading log file: {str(e)}")
        # Scroll to bottom to show latest entries
        self.log_view.verticalScrollBar().setValue(
            self.log_view.verticalScrollBar().maximum()
        )
        
    def clear_log_file(self):
        """Clear the log file and update display"""
        try:
            # Clear the file
            open(LOG_FILE, 'w').close()
            # Update UI
            self.log_view.clear()
            # Log the action
            logger.info("Log file cleared by user")
            # Show confirmation
            self.log_view.append("Log file cleared successfully")
        except Exception as e:
            error_msg = f"Error clearing log file: {str(e)}"
            logger.error(error_msg)
            self.log_view.append(error_msg)

    def add_error_item(self, error_id, description, fix_func):
        frame = QFrame()
        frame.setObjectName(f"error_{error_id}")
        layout = QVBoxLayout(frame)
        
        # Header with ID
        header_layout = QHBoxLayout()
        id_label = QLabel(f"<b>{error_id}</b>")
        id_label.setStyleSheet("color: #ff5252;")
        header_layout.addWidget(id_label)
        header_layout.addStretch()
        layout.addLayout(header_layout)
        
        # Description
        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)
        
        # Fix button
        btn = QPushButton("AUTO FIX")
        btn.setFixedWidth(100)
        btn.clicked.connect(lambda: self.error_handler.fix_error(error_id, fix_func))
        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.error_layout.insertWidget(self.error_layout.count() - 1, frame)

    def filter_errors(self):
        search_text = self.search_bar.text().lower()
        for i in range(self.error_layout.count() - 1):  
            item = self.error_layout.itemAt(i).widget()
            if item:
                # Search in both error ID and description
                id_text = item.layout().itemAt(0).itemAt(0).widget().text().lower()
                desc_text = item.layout().itemAt(1).widget().text().lower()
                visible = search_text in id_text or search_text in desc_text
                item.setVisible(visible)

    def switch_tab(self, index):
        self.main_content.setCurrentIndex(index)
        # Refresh logs when switching to logs tab
        if index == 2:  # Logs tab index
            self.load_log_file()

    def check_for_updates(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Checking for Updates")
        msg.setText("Checking for updates...")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

###############################
# APPLICATION ENTRY POINT
###############################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Dark theme palette for Fusion style
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(13, 13, 13))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(30, 30, 30))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Highlight, QColor(211, 47, 47))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    app.setPalette(palette)
    
    # Create application instance
    window = RedEngineSupportTool()
    window.show()
    sys.exit(app.exec())