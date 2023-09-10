import tensorflow as tf
import numpy as np
import chess

AI_MODEL = tf.keras.models.load_model("src/AI_MODEL/chess_model_colors_v2.h5")
LABELS = ['b', 'n', 'k', 'p', 'q', 'r', '.', 'B', 'N', 'K', 'P', 'Q', 'R']


def crop_img(img):
    tensor = tf.convert_to_tensor(img)
    return tf.image.crop_to_bounding_box(
      image = tensor,
      offset_height = 0,
      offset_width = 60,
      target_height = 182 - 60,
      target_width = 182 - 60
    )

def get_pred_label(tensor):
    pred_arr = AI_MODEL.predict([tensor], verbose=0)
    pred = pred_arr[0]
    max_value = max(pred)
    for i, ele in enumerate(pred): # try tf.argmax(tensor)
        if ele == max_value:
            return LABELS[i]

def simplify_fen(fen_unsiplified):
    fen_simplified = ""
    count = 0
    past_letter_dot = False
    for letter in fen_unsiplified:
        if letter == '.':
            count += 1
            if not past_letter_dot:
                past_letter_dot = True
        else:
            if past_letter_dot:
                past_letter_dot = False
                fen_simplified += str(count)
                count = 0
            fen_simplified += letter
    return fen_simplified[:-1]

def get_board_positions(img:object) -> object:
    """Returns the board as a chess object"""
    fen = ""
    LENGTH = int(1456/8)

    for y in range(8): #8
        for x in range(8): #8
            i = x * LENGTH
            j = y * LENGTH
            board_square = img.crop((i , j, i + LENGTH, j + LENGTH))
            tensor = crop_img(board_square)
            preped_tensor = tf.expand_dims(tensor, axis=0) 
            piece = get_pred_label(preped_tensor)
            fen += piece
        fen += '/'
    
    return chess.Board(simplify_fen(fen))   
