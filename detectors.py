import cv2
import utils
import dlib
import numpy as np
from profile_detection import profile_detection
from emotion_detection import emotion_detection
from blink_detection import   blink_detection

# Detectors
frontal_face_detector    = dlib.get_frontal_face_detector()
profile_detector         = profile_detection.detect_face_orientation()
emotion_detector         = emotion_detection.predict_emotions()
blink_detector           = blink_detection.eye_blink_detector() 

def detect_liveness(im,COUNTER=0,TOTAL=0):
    # Process Image to Gray
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Face detection
    rectangles = frontal_face_detector(gray, 0)
    print(rectangles)
    boxes_face = utils.convert_rectangles2array(rectangles,im)
    if len(boxes_face)!=0:
        areas = utils.get_areas(boxes_face)
        index = np.argmax(areas)
        rectangles = rectangles[index]
        boxes_face = [list(boxes_face[index])]
        print(boxes_face)
        print(rectangles)

    # Emotion Detection
        _,emotion = emotion_detector.get_emotion(im,boxes_face)

    # Blink Detections
        COUNTER,TOTAL = blink_detector.eye_blink(gray,rectangles,COUNTER,TOTAL)
    else:
        boxes_face = []
        emotion = []
        TOTAL = 0
        COUNTER = 0

    # Profile Detection
    box_orientation, orientation = profile_detector.face_orientation(gray)

    output = {
        'box_face_frontal': boxes_face,
        'box_orientation': box_orientation,
        'emotion': emotion,
        'orientation': orientation,
        'total_blinks': TOTAL,
        'count_blinks_consecutives': COUNTER
    }
    return output

