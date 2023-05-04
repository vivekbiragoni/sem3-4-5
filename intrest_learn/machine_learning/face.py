import cv2
import feat

# Load the model for facial expression recognition
model = feat.ExpressionModel()

# Open the video stream
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Detect the facial landmarks
    landmarks = feat.get_landmarks(frame)

    # Check if the landmarks were detected
    if landmarks is not None:
        # Predict the facial expression
        expression = model.predict(landmarks)

        # Display the predicted expression on the frame
        cv2.putText(frame, expression, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('frame', frame)

    # Wait for the user to press a key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close the window
cap.release()
cv2.destroyAllWindows()
