import imutils
import numpy as np
import pickle
import cv2
import camera
import face_recognition

encoding = "path" #path to encoding.pickle file
data = pickle.loads(open(encoding, "rb").read())
def fr1(): 
    while(True):
      frame=camera.fra()
      rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      rgb = imutils.resize(frame, width=400)
      r = frame.shape[1] / float(rgb.shape[1])

      boxes = face_recognition.face_locations(rgb, model= "hog")
      if(boxes=={}):
          print("No person detected...please show your face...")
          continue
      else:
          encodings = face_recognition.face_encodings(rgb, boxes)
          names = []
       
          for encoding in encodings:
                    matches = face_recognition.compare_faces(np.array(encoding),np.array(data["encodings"]),0.6)
                    name = "Unknown"
                   
                    if True in matches:
                        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}
                        for i in matchedIdxs:
                            name = data["names"][i]
                            counts[name] = counts.get(name, 0) + 1
                            name = max(counts, key=counts.get)
                    names.append(name)
                    print("Person : ",name)
                    return(name)
                
                
          
              
        
