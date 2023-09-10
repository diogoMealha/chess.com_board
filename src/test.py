from PIL import Image
from board_identifier import get_board_positions

board_print = Image.open('src/board_print.png')
board = get_board_positions(board_print)

print(board)