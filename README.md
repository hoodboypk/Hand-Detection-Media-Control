# Hand-Detection-Media-Control

Using hand detections, you can control the volume of your device.
This program captures the landmarks of your palm, and then calls a function in the backend (according to landmark positions) which increases/decreases the device's volume and also play/pause music.

hand landmarks:

![hand_landmarks](https://github.com/hoodboypk/Hand-Detection-Media-Control/assets/93330691/d31aa073-c3d8-4b70-b1c4-400bcb3f2d98)

The program compares the y coordinates of INDEX_FINGER_TIP, MIDDLE_FINGER_TIP, and RING_FINGER_TIP with the y coordinate of THUMB_TIP and then calls the appropriate pyautogui function.


Output:
![image](https://github.com/hoodboypk/Hand-Detection-Media-Control/assets/93330691/cb06b00d-38b7-4dfc-9e4d-96e6830738f9)
