import cv2
from ultralytics import YOLO

# — PARAMETERS —
VIDEO_PATH = 'Cars Moving On Road Stock Footage - Free Download.mp4'
LINE_RATIO = 0.75            # line at 75% of frame height
EXIT_KEYS  = [ord('q'), 27]  # 'q' or ESC to quit

# — LOAD MODEL & SETUP —
model = YOLO('yolov8n.pt')   # YOLOv8 nano
car_count = 0
seen_ids = set()             # completed counts
prev_centroids = {}          # last‐frame centroid per ID
line_y = None

# — STREAM + TRACK —
results = model.track(
    source=VIDEO_PATH,
    stream=True,
    tracker='bytetrack.yaml',
    persist=True
)

for r in results:
    frame = r.orig_img
    if line_y is None:
        line_y = int(frame.shape[0] * LINE_RATIO)

    # draw the counting line
    cv2.line(frame, (0, line_y), (frame.shape[1], line_y),
             (255, 0, 0), 2)

    # process each detection
    for box, raw_id in zip(r.boxes.xyxy, r.boxes.id):
        obj_id = int(raw_id)                   # make sure it’s a Python int
        x1, y1, x2, y2 = map(int, box)
        cx, cy = (x1 + x2)//2, (y1 + y2)//2

        # draw box + centroid
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)

        # only attempt to count if we've seen it in a previous frame
        if obj_id in prev_centroids and obj_id not in seen_ids:
            prev_cy = prev_centroids[obj_id]
            # crossing downward?
            if prev_cy < line_y <= cy:
                car_count += 1
                seen_ids.add(obj_id)

        # update this ID’s last‐seen centroid
        prev_centroids[obj_id] = cy

    # overlay count
    cv2.putText(frame, f'Car Count: {car_count}', (10, 100),  # Increased Y-position
            cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)  # White color, bigger font and thicker


    cv2.imshow('YOLOv8 Traffic Counter', frame)
    if cv2.waitKey(1) & 0xFF in EXIT_KEYS:
        break

cv2.destroyAllWindows()
