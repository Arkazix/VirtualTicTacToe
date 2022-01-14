import cv2
import mediapipe as mp
from point import Point
from tictactoe import TicTacToe

capture = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

WIN_WIDTH = capture.get(3)
WIN_HEIGHT = capture.get(4)

tictactoe = TicTacToe(0.9 * WIN_HEIGHT, WIN_WIDTH, WIN_HEIGHT)

run = True
finger_press = True

while run:
    _, img = capture.read()

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(image=rgb_img)

    tictactoe.draw_line(img)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            thumb_lmk = hand.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_point = Point(thumb_lmk.x, thumb_lmk.y)

            index_lmk = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_point = Point(index_lmk.x, index_lmk.y)

            dist = index_point.dist(thumb_point)
            if dist < 0.1 and not finger_press:
                # TODOE : check if fingers is in a tictactoe square
                print("--!--")
                finger_press = True
            if dist >= 0.1:
                finger_press = False

    img = cv2.flip(img, 1)
    img = cv2.resize(img, (1080, 720))
    cv2.imshow("Tic Tac Toe", img)

    key = cv2.waitKey(1)
    if key != -1:
        run = False

capture.release()
cv2.destroyAllWindows()
