# Hand Tracking 
### Aim 
* To accurately detect and track human hands in images and videos

### Libraries used 
* OpenCV
* mediapipe
* Time 

### How I did it 
This is a Python script that uses the Mediapipe library and OpenCV to detect and track hand landmarks in real-time video. The script uses the mpHands module from Mediapipe to detect hand landmarks and the mpdraw module to draw lines between the landmarks. It also calculates the frames per second (FPS) and displays it on the video feed.

The script first imports the necessary libraries, including Mediapipe and OpenCV. It then creates an instance of the mpHands module and the mpdraw module. It also initializes variables for calculating FPS.

Next, the script initializes a video capture object using OpenCV's VideoCapture function. It then enters a while loop that captures frames from the video feed using the read function of the video capture object. It converts the captured frames to RGB format since Mediapipe requires RGB input. It then passes the RGB image to the hands.process function of the mpHands module to detect the hand landmarks.

If the hand landmarks are detected, the script iterates through each detected hand and the landmarks for each hand. It then calculates the pixel coordinates of each landmark and draws lines between adjacent landmarks using the mpdraw.draw_landmarks function.

The script also calculates the FPS by calculating the time difference between the current and previous frames. It then displays the FPS on the video feed using the cv2.putText function.

The while loop exits when the 'f' key is pressed. Finally, the script releases the video capture object and destroys all windows.