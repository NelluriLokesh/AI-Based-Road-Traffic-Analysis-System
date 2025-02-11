import sys
import os
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if module_path not in sys.path:
    sys.path.insert(0, module_path)
os.chdir(module_path)
os.environ['YOLOV5_SKIP_GIT'] = '1'
os.environ['SKIP_GIT'] = '1'

import sys
sys.path.append(os.path.join(module_path, 'yolov5'))

import cv2
import torch
import numpy as np
from models.experimental import attempt_load
from utils.general import non_max_suppression
from utils.torch_utils import select_device

model_path = os.path.join(module_path, 'yolov5', 'yolov5s.pt') 
device = select_device('')  

model = attempt_load(model_path, device=device)  
model.eval()
VEHICLE_CLASSES = [2, 3, 5, 7]  
total_vehicle_count = 0
counted_centroids = []

def detect_vehicles(frame, conf_thresh=0.4, iou_thresh=0.5):
    """
    Detect vehicles in a video frame using YOLOv5.
    """
    # Capture original dimensions
    original_h, original_w = frame.shape[:2]
    # Resize image for detection
    img = cv2.resize(frame, (640, 640))  
    scale_w = original_w / 640.0
    scale_h = original_h / 640.0
    img = img[:, :, ::-1].transpose(2, 0, 1)
    img = np.ascontiguousarray(img)  
    img = torch.from_numpy(img).float() / 255.0
    img = img.unsqueeze(0)  

    with torch.no_grad():
        pred = model(img, augment=False)[0]
    pred = non_max_suppression(pred, conf_thresh, iou_thresh)

    vehicles = []
    for det in pred:  
        if det is not None and len(det):
            for *box, conf, cls in det:
                if int(cls) in VEHICLE_CLASSES:  
                    x1, y1, x2, y2 = map(int, box)  
                    x1 = int(x1 * scale_w)
                    y1 = int(y1 * scale_h)
                    x2 = int(x2 * scale_w)
                    y2 = int(y2 * scale_h)
                    vehicles.append((x1, y1, x2, y2, conf, int(cls)))  
    return vehicles

def draw_boxes(frame, boxes):
    """
    Draw bounding boxes around detected vehicles.
    """
    for (x1, y1, x2, y2, conf, cls) in boxes:
        label = f"Vehicle: {conf:.2f}"  
        color = (0, 255, 0)  
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)  
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  
    return frame

video_path = os.path.join(module_path, 'Cars Moving On Road Stock Footage - Free Download.mp4') 
cap = cv2.VideoCapture(video_path)

vehicle_count = 0

frame_count = 0
skip_frames = 8  
if skip_frames == 0: skip_frames = 1
prev_vehicles = []

while cap.isOpened():
    ret, frame = cap.read()  
    if not ret:
        break  

    if frame_count % skip_frames == 0:
        vehicles = detect_vehicles(frame)
        prev_vehicles = vehicles
    else:
        vehicles = prev_vehicles

    frame = draw_boxes(frame, vehicles)

    crossing_line = int(frame.shape[0] * 0.66)
    cv2.line(frame, (0, crossing_line), (frame.shape[1], crossing_line), (255, 0, 0), 2)

    for v in vehicles:
        x1, y1, x2, y2, conf, cls = v
        centroid_x = int((x1 + x2) / 2)
        centroid_y = int((y1 + y2) / 2)
        if centroid_y >= (crossing_line - 20):
            already_counted = False
            for cx, cy in counted_centroids:
                if abs(centroid_x - cx) < 30 and abs(centroid_y - cy) < 30:
                    already_counted = True
                    break
            if not already_counted:
                counted_centroids.append((centroid_x, centroid_y))
                total_vehicle_count += 1

    count_text = f"."
    cv2.putText(frame, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Traffic Analysis", frame)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 30.0, (frame.shape[1], frame.shape[0]))
    out.write(frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_count += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Total vehicles detected: {total_vehicle_count}")
