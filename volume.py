import cv2 as cv
import pyautogui
import mediapipe as mp

cap = cv.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                      min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

hand_gesture = 'other'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = hands.process(frame)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

            index_finger_y = hand_landmark.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = hand_landmark.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            middle_finger_y = hand_landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
            ring_finger_y = hand_landmark.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
            pinky_finger_y = hand_landmark.landmark[mp_hands.HandLandmark.PINKY_TIP].y

            # Initialize hand_gesture
            hand_gesture = 'other'

            # Update hand_gesture based on finger positions
            if index_finger_y > thumb_y:
                hand_gesture = 'pointing up'
            
            if middle_finger_y > thumb_y:
                hand_gesture = 'pointing down'

            if ring_finger_y > thumb_y:
                hand_gesture = 'stop'

    if hand_gesture == 'pointing up':
        pyautogui.press('volumeup')
    elif hand_gesture == 'pointing down':
        pyautogui.press('volumedown')

    if hand_gesture == 'stop':
        pyautogui.press('playpause')

    cv.imshow('Hand gesture', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
