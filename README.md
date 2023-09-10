# chess.com Image to Board 
Simple program that uses tensorflow and computer vision to describe a chess.com chess board from board image.

## Example
the following code is in test.py
```python
from PIL import Image
from board_identifier import get_board_positions

board_print = Image.open('src/board_print.png')
board = get_board_positions(board_print)

print(board)
```

## A.I. Model
The used cnn model was trained to a particular set of chess pieces of chess.com.

## License
This project is licensed under the MIT License

## Dependencies
tensorflow ^2.13.0\
numpy ^1.24.3\
chess ^1.10.0\
PIL.Image ^9.5.0


