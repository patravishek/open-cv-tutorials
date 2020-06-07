from cv2 import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        print("camera warming up")

    def get_frame(self):
        ret, frame = self.cap.read()

        if ret==True:
            pass
        return frame

    def release_object(self):
        self.cap.release()

def main():
    while(True):
        frame = Camera().get_frame()
        print(frame)
        print("Got the frames")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(0) & 0XFF == ord('q'):
            break

    return()

if __name__ == '__main__':
    main()
    Camera().release_object()
    cv2.destroyAllWindows()