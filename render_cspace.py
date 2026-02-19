import numpy as np
import cv2 as cv
import math
from math import sin, cos

# Function to convert object to pixel coordinates
def cvt_coords(pt):
    return (int(pt[0] * 100 + 240), int(1000 - (pt[1] * 100 + 320)))

# Function to draw triangle 
def draw_triangle(img, pt1, pt2, pt3):
    # Convert points to pixel coords
    pt1 = cvt_coords(pt1)
    pt2 = cvt_coords(pt2)
    pt3 = cvt_coords(pt3)
    # Draw triangle
    cv.line(img,pt1,pt2,(255,0,0),1)
    cv.line(img,pt2,pt3,(255,0,0),1)
    cv.line(img,pt3,pt1,(255,0,0),1)

# Function to render arm
def draw_arm(img, t0, t1):
    # Define the transformations
    X_W2R1 = np.array([[cos(t0), -sin(t0), 0],
                      [sin(t0), cos(t0), 0],
                      [0, 0, 1]])
    X_R1J1 = np.array([[1, 0, 3],
                      [0, 1, 0],
                      [0, 0, 1]])
    X_J1R2 = np.array([[cos(t1), -sin(t1), 0],
                       [sin(t1), cos(t1), 0],
                       [0, 0, 1]])
    X_R2J2 = np.array([[0, 0, 3],
                       [0, 0, 0],
                       [0, 0, 1]])
    X_WJ2 = X_W2R1 @ X_R1J1 @ X_J1R2 @ X_R2J2

    # Compute position of points to draw in between
    origin = np.array([0, 0, 1])
    j1 = X_W2R1 @ X_R1J1 @ origin.reshape(3, 1)
    j2 = X_WJ2 @ origin.reshape(3, 1)

    # Convert to Pixel
    p0 = cvt_coords((0, 0))
    p1 = cvt_coords((j1[0][0], j1[1][0]))
    p2 = cvt_coords((j2[0][0], j2[1][0]))

    # Draw the lines
    cv.line(img,p0,p1,(255,0,0),1)
    cv.line(img,p1,p2,(255,0,0),1)

STEP = 0.05  # radians per key press
t0 = 0.0
t1 = math.pi / 2

# Arrow key codes (Linux, OpenCV waitKeyEx)
KEY_UP    = 65362
KEY_DOWN  = 65364
KEY_LEFT  = 65361
KEY_RIGHT = 65363
KEY_ESC   = 27

print("Controls: UP/DOWN = theta1 | LEFT/RIGHT = theta2 | ESC = quit")

while True:
    # Redraw scene each frame
    img = np.zeros((1000, 1000, 3), np.uint8)
    draw_triangle(img, (-2.3, -3.2), (-1, -1.2), (-0.5, -2.8))
    draw_triangle(img, (-2.4, 2.2), (-1.0, 4.0), (-0.4, 2.7))
    draw_triangle(img, (3.1, 2.2), (4.5, 4.0), (5.2, 2.6))
    draw_arm(img, t0, t1)

    cv.imshow('Image', img)

    key = cv.waitKeyEx(30)
    if key == KEY_ESC:
        break
    elif key == KEY_UP:
        t0 += STEP
    elif key == KEY_DOWN:
        t0 -= STEP
    elif key == KEY_RIGHT:
        t1 += STEP
    elif key == KEY_LEFT:
        t1 -= STEP

    if key != -1:
        print(f"theta1 = {np.mod(t0, 2 * math.pi) / math.pi:.4f} pi  |  theta2 = {np.mod(t1, 2 * math.pi) / math.pi:.4f} pi")

cv.destroyAllWindows()