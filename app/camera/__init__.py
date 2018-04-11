import cv2
import time
from app.camera.base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            pass()

#class CameraPi(BaseCamera):
#    import io
#    import picamera
#    @staticmethod
#    def frames():
#        with picamera.PiCamera() as camera:
#            # let camera warm up
#            time.sleep(2)
#
#            stream = io.BytesIO()
#            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
#                # return current frame
#                stream.seek(0)
#                yield stream.read()
#
#                # reset stream for next frame
#                stream.seek(0)
#                stream.truncate()

class CameraOpenCV(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
