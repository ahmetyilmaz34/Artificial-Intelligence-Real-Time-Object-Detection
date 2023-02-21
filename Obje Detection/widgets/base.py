import tkinter as tk
import tkinter.ttk as ttk
import PIL.Image
import PIL.ImageTk
import cv2 
import numpy as np


# internals
from .base_widget import BaseWidget
#from camera import Camera

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0,255,size=(len(CLASSES),3))

net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")

cap=cv2.VideoCapture(0)

class Base(BaseWidget):
    
    def __init__(self, *args, **kwargs):
        BaseWidget.__init__(self, *args, **kwargs)
        self.miliseconds = 1
            
    def capture(self):
        try:       
            res,frame=cap.read()
            if res:
                frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                (h,w) = frame.shape[:2]
                blob = cv2.dnn.blobFromImage(cv2.resize(frame,(300, 300)), 0.007843,(300, 300), 127.5)
                net.setInput(blob)
                detections = net.forward()
                for j in np.arange(0, detections.shape[2]):   
                    confidence = detections[0,0,j,2]    
                    if confidence > 0.10:     
                        idx = int(detections[0,0,j,1])
                        box = detections[0,0,j,3:7]*np.array([w,h,w,h])
                        (startX, startY, endX, endY) = box.astype("int")
            
                        label = "{}: {}".format(CLASSES[idx], confidence)
                        cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx],2)
                        y = startY - 16 if startY -16 >15 else startY + 16
                        cv2.putText(frame, label, (startX,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5,COLORS[idx],2)
                self.canvasframe = PIL.ImageTk.PhotoImage(
                image=PIL.Image.fromarray(frame))
                self.canvas_image.create_image(
                    0, 0, image=self.canvasframe, anchor="nw")
                self.after(self.miliseconds, self.capture)
        except Exception as exc:
            self.txt_log.insert('0.0',f"{exc}")           

    def stop(self):
        try:
          if cap.isOpened():
            cap.release()
        except Exception as exc:
            self.txt_log.insert('0.0',f"\n{exc}") 

    