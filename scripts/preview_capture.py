"""Preview live screen capture frames with OpenCV."""

import cv2

from app.capture import FrameCapture


def main() -> None:
    capture = FrameCapture()
    try:
        for frame in capture.frames():
            cv2.imshow("NEXDRIVE AI capture preview", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        capture.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
