from __future__ import division
import os
import cv2
from numpy import array
import dlib
from .eye import Eye
from .calibration import Calibration

class FaceTracking(object):
    def __init__(self):
        self.frame = None
        self.faces = array()
        self.calibration = Calibration()

        self._face_detector = dlib.get_frontal_face_detector()

    # @property
    # def faces_located(self):
        
    def _analyze(self):
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        faces = self._face_detector(frame)

        try:
            self.faces=faces
        
        except IndexError:
            #faces is the array of faces now
            self.faces=None

    def refresh(self, frame):
        self.frame = frame
        self._analyze()

    def annotated_frame(self):
        # remake this
        """Returns the main frame with pupils highlighted"""
        frame = self.frame.copy()

        if self.pupils_located:
            color = (0, 255, 0)
            x_left, y_left = self.pupil_left_coords()
            x_right, y_right = self.pupil_right_coords()
            cv2.line(frame, (x_left - 5, y_left), (x_left + 5, y_left), color)
            cv2.line(frame, (x_left, y_left - 5), (x_left, y_left + 5), color)
            cv2.line(frame, (x_right - 5, y_right), (x_right + 5, y_right), color)
            cv2.line(frame, (x_right, y_right - 5), (x_right, y_right + 5), color)

        return frame
