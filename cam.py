import cv2
from deepface import DeepFace
import serial
import time

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
ser = serial.Serial('/dev/tty.usbmodem14201', 9600)  

# Define a video capture object
vid = cv2.VideoCapture(0)
framex = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2
framey = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2
#print(x)
#print(y)



while True:
    # Capture the video frame by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Convert the frame to grayscale (for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Draw a bounding box around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Calculate and print the center coordinates of the face
        center_x = x + w // 2
        center_y = y + h // 2
        #print(center_x)
        #print(center_y)
        a = 30

        # Control the device based on face position
        if (center_x + a > framex and center_x - a > framex ):
            ser.write(b'l')  
            time.sleep(1)
            print("l")
        elif (center_x + a < framex and center_x - a < framex ):
            ser.write(b'r')  
            time.sleep(1)
            print("r")
        if(center_y + a > framey and center_y - a > framey):
            ser.write(b'u')  
            time.sleep(1)
            print("u")
        elif(center_y + a < framey and center_y - a < framey):
            ser.write(b'd')  
            time.sleep(1)
            print("d")

    

    # Display the frame with bounding boxes
    cv2.imshow('frame', frame)

    # Convert the frame to RGB (DeepFace requires RGB format)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        # Analyze emotions
        result = DeepFace.analyze(frame_rgb, actions=["emotion"])
        #print(result)
        font = cv2.FONT_HERSHEY_SIMPLEX
        e_position = (100, 100)
        c_position = (1000,1000)
        fontScale = 3
        color = (0, 0, 255)  # BGR color format (blue)
        thickness = 2
        text1 = result[0]["dominant_emotion"]
        print("Emotion: ", text1)
        if(text1 == "sad" or text1 == "angry"):
            ser.write(b'1')  
            time.sleep(1)    
        else:
            ser.write(b'2')  
            time.sleep(1)    

        cv2.putText(frame, text1, e_position, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        #cv2.putText(frame, text2, c_position, font, fontScale, color, thickness, cv2.LINE_AA)

    except ValueError:
        print("No face detected. Waiting for a face to be shown...")
        continue  # Skip to the next iteration of the loop


    # The 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop, release the capture object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
