import pyautogui
import keyboard
import json
from common import VECTOR

SAVE = "previous.bak"
pyautogui.PAUSE = 1e-9

def bye():
    raise SystemExit(1)

keyboard.add_hotkey('ctrl+c', bye)
def restore_backup() -> int:
    try:
        with open(SAVE, mode="r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 1

def draw_json(data: dict) -> None:
    pyautogui.FAILSAFE = False
    features = data["features"]
    for f in features:
        coords = f["geometry"]["coordinates"]
        for polygon in coords:
            pyautogui.moveTo(polygon[0][0]*3, polygon[0][1]*3)
            pyautogui.mouseDown()
            for point in polygon[1:]:
                pyautogui.moveTo(point[0]*3, point[1]*3)
            pyautogui.mouseUp()
    pyautogui.FAILSAFE = True

def main():
    global i
    print("Awaiting enter key press...")
    keyboard.wait("enter")
    
    with open(VECTOR / "img1001.json") as f:
        data = json.load(f)
    draw_json(data)
    # running = True
    # while running:
    #     current_frame = f"img{i:04}.json"

    #     # Get JSON for this frame
    #     with open(VECTOR / current_frame) as f:
    #         data = json.load(f)

    #     print(data)
    #     raise Exception()

    #     i += 1
    #     if i > 6572:
    #         running = False
    # print(current_frame)

if __name__ == "__main__":
    i = restore_backup()
    # try:
    main()
        # raise Exception()
    # except Exception as e:
        # print(e)
        # with open(SAVE, "w") as f:
        #     f.write(str(i))