import cv2
import sys
import numpy as np

#The main function. Load the cascade classifier from the xml file.
if __name__ == '__main__':

  faceCascade = cv2.CascadeClassifier('C:/Ellen/Udacity/Computer_Vision/data/haarcascade_frontalface_default.xml')
  faceNeighborsMax = 10
  neighborStep = 1
  
  print("Hello")

  #frame = cv2.imread("hillary_clinton.jpg")
  #frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  # Perform multi scale detection of faces 
  #for neigh in range(1, faceNeighborsMax, neighborStep):
  #  faces = faceCascade.detectMultiScale(frameGray, 1.2, neigh)
  #  frameClone = np.copy(frame)
    
    # Display the image
   # for (x, y, w, h) in faces:
   #   cv2.rectangle(frameClone, (x, y), (x + w, y + h), (255, 0, 0), 2)

    #cv2.putText(frameClone, "# Neighbors = {}".format(neigh), (10, 50), 
    #cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
    #cv2.imshow('Face Detection Demo', frameClone)
    #if cv2.waitKey(500) & 0xFF == 27:
    #  cv2.destroyAllWindows()
    #  sys.exit()