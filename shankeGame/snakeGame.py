import numpy as np
import cv2
import random
import findPositon

fn = findPositon.handPostion()

def genApple(apple_position, img=[], eat=False):
    if eat == True or apple_position == None:
        apple_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]

    cv2.rectangle(img, (apple_position[0], apple_position[1]), (apple_position[0] + 10, apple_position[1] + 10),
                  (0, 0, 255), 3)
    return apple_position


def snakeMove(snake_position, button_direction, img, apple_position):
    snake_head = snake_position[0]
    updated_head = snake_head
    cx, cy = snake_head
    size = 20
    if button_direction == 1:
        updated_head = [cx +size, cy]
    elif button_direction == 0:
        updated_head = [cx - size, cy]
    elif button_direction == 2:
        updated_head = [cx, cy + size]
    elif button_direction == 3:
        updated_head = [cx, cy - size]

    # initial apple create
    if len(apple_position) < 1:
        apple_position = genApple(None, img, eat=False)
    else:
        apple_position = genApple(apple_position, img, eat=False)

    if snake_head == apple_position:
        apple_position = genApple(apple_position, img, eat=True)
        snake_position.insert(0, updated_head)
    else:
        snake_position.insert(0, updated_head)
        snake_position.pop()

    # print(snake_position)
    for position in snake_position:
        cv2.rectangle(img, (position[0], position[1]), (position[0] + 10, position[1] + 10), (0, 255, 0), 3)
    return apple_position


def getSnakeDirection():
    # 0-Left, 1-Right, 3-Up, 2-Down, q-Break
    # a-Left, d-Right, w-Up, s-Down
    global key
    button_direction = 0
    if key == ord('a'):
        button_direction = 0
    elif key == ord('d'):
        button_direction = 1
    elif key == ord('w'):
        button_direction = 3
    elif key == ord('s'):
        button_direction = 2
    return button_direction

snake_position = [[270, 250], [250, 250], [230, 250]]
key = 100


apple_position = []
cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 600)
while True:
    img = np.zeros((600, 600, 3))
    _, camImg = cap.read()
    camImg = cv2.flip(camImg, 1)


    button_direction = getSnakeDirection()
    apple_position = snakeMove(snake_position, button_direction, img, apple_position)

    key = fn.getPlace(camImg, key)
    cv2.imshow("Snake Game", img)
    cv2.imshow("my Image", camImg)
    # print("myKey", myKey)

    key_ = cv2.waitKey(500)
    if key_ != -1:
        key = key_
    print(key)


# 119 |
# 97 <-