import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QLabel # Added QLabel
from PyQt5.QtGui import QPainter, QColor, QRect
from PyQt5.QtCore import Qt # Added Qt for alignment
from main import GameBoard, ChessPiece # Added ChessPiece

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Game - Main Menu")
        self.start_game_button = QPushButton("Start New Game")
        self.start_game_button.clicked.connect(self.start_game_clicked)
        layout = QVBoxLayout()
        layout.addWidget(self.start_game_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_game_clicked(self):
        # print("Start New Game button clicked") # Optional: keep for debugging
        self.game_window = GameWindow()  # Create and store instance
        self.game_window.show_game()     # Show the game window
        self.close()                     # Close the MainMenu window


    def show_menu(self):
        self.show()

class ChessBoardWidget(QWidget):
    def __init__(self, game_board, parent=None):
        super().__init__(parent)
        self.game_board = game_board 
        
        self.board_display_size = 400 
        self.square_size = self.board_display_size // self.game_board.width 
        self.actual_board_display_size = self.square_size * self.game_board.width
        self.setFixedSize(self.actual_board_display_size, self.actual_board_display_size)
        # Removed setWindowTitle from here as the main window (GameWindow) will have the title.

    def paintEvent(self, event):
        painter = QPainter(self)
        light_color = QColor(240, 217, 181) 
        dark_color = QColor(181, 136, 99)   

        for r in range(self.game_board.height): 
            for c in range(self.game_board.width): 
                x_coord = c * self.square_size
                y_coord = r * self.square_size
                if (r + c) % 2 == 0:
                    painter.setBrush(light_color)
                else:
                    painter.setBrush(dark_color)
                painter.drawRect(QRect(x_coord, y_coord, self.square_size, self.square_size))

class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Chess Game")

        self.game_board = GameBoard()
        # Add test pieces
        # Note: In GameBoard, place_piece(self, piece, x, y) stores at self.matrix[y][x]
        # So, (x=0, y=1) means column 0, row 1.
        self.game_board.place_piece(ChessPiece("White", "Pawn"), 0, 1) # White Pawn at (0,1) -> matrix[1][0]
        self.game_board.place_piece(ChessPiece("Black", "Rook"), 7, 0) # Black Rook at (7,0) -> matrix[0][7]
        self.chess_board_widget = ChessBoardWidget(self.game_board)
        
        self.current_turn = "White"
        self.turn_label = QLabel(f"Turn: {self.current_turn}")
        self.turn_label.setAlignment(Qt.AlignCenter) 
        
        self.next_turn_button = QPushButton("Next Turn")
        self.next_turn_button.clicked.connect(self.switch_turn)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chess_board_widget)
        main_layout.addWidget(self.turn_label)
        main_layout.addWidget(self.next_turn_button) # Add button to layout

        central_content_widget = QWidget()
        central_content_widget.setLayout(main_layout)
        self.setCentralWidget(central_content_widget)

    def switch_turn(self):
        if self.current_turn == "White":
            self.current_turn = "Black"
        else:
            self.current_turn = "White"
        self.turn_label.setText(f"Turn: {self.current_turn}")

    def show_game(self):
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Start with MainMenu to test the flow
    main_menu = MainMenu()
    main_menu.show_menu()
    
    sys.exit(app.exec_())
