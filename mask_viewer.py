import cv2
from agent.env.capture import ScreenCapture
from agent.env.item_detector import detect_item, get_item_mask


def main():
    cap = ScreenCapture()
    cv2.namedWindow("Frame")
    cv2.namedWindow("Item Mask")
    while True:
        obs, colorFrame = cap.get_frame()

        mask = get_item_mask(obs)

        cv2.imshow("Frame", obs)
        cv2.imshow("Item Mask", mask)

        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
