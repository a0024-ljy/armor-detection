import argparse
from pathlib import Path
import cv2
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument("--model", default="best.pt")
parser.add_argument("--source", default="video.mp4")
parser.add_argument("--output", default="runs/output")
parser.add_argument("--conf", type=float, default=0.25)
args = parser.parse_args()

model = YOLO(args.model)
Path(args.output).mkdir(parents=True, exist_ok=True)

cap = cv2.VideoCapture(args.source)
fps = cap.get(cv2.CAP_PROP_FPS) or 30
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter("runs/output/result.mp4",
                         cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

n = 0
while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break
    results = model.predict(frame, conf=args.conf, verbose=False)
    writer.write(results[0].plot())
    n += 1
    if n % 50 == 0:
        print("已处理", n, "帧")

cap.release()
writer.release()
print("完成！结果在 runs/output/result.mp4")
