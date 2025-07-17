# test1_input.py

import cv2
import platform
from input_handler import InputHandler

def main():
    # 라즈베리파이에서는 CAP_V4L2를 사용하는 것이 안정적
    if platform.machine().startswith("arm") or platform.system() == "Linux":
        source = cv2.CAP_V4L2
        cam_index = 0
        handler = InputHandler(source=cam_index)
    else:
        handler = InputHandler(source=0)

    if not handler.is_opened():
        print("❌ 카메라를 열 수 없습니다.")
        return

    print("✅ 카메라 연결 성공 - 'q' 키를 누르면 종료됩니다.")
    while True:
        frame = handler.get_frame()
        if frame is None:
            print("⚠️ 프레임을 읽어올 수 없습니다. 종료합니다.")
            break

        cv2.imshow("InputHandler Test", frame)

        # 1ms 대기 후 'q' 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("사용자 종료 요청 - 테스트 종료")
            break

    handler.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
