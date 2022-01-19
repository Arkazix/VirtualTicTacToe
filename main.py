try:
    import cv2
    import mediapipe as mp
except ImportError:
    print("OpenCV and mediapipe is require.")
    print("Install it via command:")
    print("    pip install opencv-contrib-python")
    print("    pip install mediapipe")
    raise
from src.tictactoe import TicTacToe
from src.point import Point
from src.const import (PIPE, MAX_HANDS, MIN_DETECTION, PROP_WIDTH, PROP_HEIGHT,
                   GRID_FACTOR, MIN_DIST_BETWEEN_FINGER, IS_FLIPED, WIN_SIZE)

capture = cv2.VideoCapture(PIPE)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=MAX_HANDS,
                       min_detection_confidence=MIN_DETECTION)
mp_draw = mp.solutions.drawing_utils

WIN_WIDTH = capture.get(PROP_WIDTH)
WIN_HEIGHT = capture.get(PROP_HEIGHT)

tictactoe = TicTacToe(GRID_FACTOR * WIN_HEIGHT, WIN_WIDTH, WIN_HEIGHT)

run = True
finger_press = True
is_circle = True

while run:
    _, img = capture.read()

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(image=rgb_img)

    tictactoe.draw_line(img)
    tictactoe.draw_shape(img)
    
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            thumb_lmk = hand.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_point = Point(thumb_lmk.x, thumb_lmk.y)

            index_lmk = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_point = Point(index_lmk.x, index_lmk.y)

            dist = index_point.dist(thumb_point)
            if dist < MIN_DIST_BETWEEN_FINGER and not finger_press:
                # TODOE : check if fingers is in a tictactoe square
                square_id = tictactoe.is_in(index_point, thumb_point)
                if square_id != -1:
                    square = tictactoe.get_square(square_id)
                    is_already_in = tictactoe.add_shape(square_id, is_circle,
                                                        square)
                    if is_already_in == 0:
                        is_circle = not is_circle
                finger_press = True
            if dist >= MIN_DIST_BETWEEN_FINGER:
                finger_press = False
    
    if IS_FLIPED:
        img = cv2.flip(img, 1)
    img = cv2.resize(img, WIN_SIZE)
    cv2.imshow("Tic Tac Toe", img)

    key = cv2.waitKey(1)
    if key != -1:
        run = False

capture.release()
cv2.destroyAllWindows()
