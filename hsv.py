import numpy as np
import cv2
class HSVDescriptor:
 def __init__(self,bins):
  self.bins=bins
 def describe(self,image):
  image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
  features=[]
  (h,w)=image.shape[:2]
  (cx,cy)=(int(w*0.5),int(h*0.5))
  segments=[(0,cx,0,cy),(cx,w,0,cy),(cx,w,cy,h),(0,cx,cy,h)]
  (axesx,axesy)=(int(w*0.75)/2,int(h*0.75)/2)
  ellipmask=np.zeros(image.shape[:2],dtype="uint8")
  cv2.ellipse(ellipmask,(cx,cy),(axesx,axesy),0,0,360,255,-1)
  for (startx,endx,starty,endy) in segments:
   cornermask=np.zeros(image.shape[:2],dtype="uint8")
   cv2.rectangle(cornermask,(startx,starty),(endx,endy),255,-1)
   cornermask=cv2.subtract(cornermask,ellipmask) 
   hist=self.histogram(image,cornermask)
   features.extend(hist)
  hist=self.histogram(image,ellipmask)
  features.extend(hist)
  return np.array(features)
 def histogram(self,image,mask=None):
  hist=cv2.calcHist([image],[0,1,2],mask,self.bins,[0,180,0,256,0,256])
  hist=cv2.normalize(hist).flatten()
  return hist
