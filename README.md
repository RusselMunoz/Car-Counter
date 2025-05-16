# Car-Counter

🚗 YOLOv8 Traffic Counter
This project uses Ultralytics YOLOv8 and OpenCV to detect and count cars crossing a virtual line in a video.

📁 Project Structure
bash
Copy
Edit
.
├── main.py                  # The Python script (the code you provided)
├── yolov8n.pt               # Pre-trained YOLOv8 Nano model (downloaded automatically or manually)
├── bytetrack.yaml           # Tracker config file (optional if using default)
├── video.mp4                # Your traffic video file (rename accordingly)
└── README.md                # This file

### 🛠️ Requirements
- Python 3.8+

- [ultralytics (YOLOv8)](https://docs.ultralytics.com/models/yolov8/)

- [opencv-python](https://opencv.org/)

##🐍 Installation
1. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate

2. Install dependencies
pip install ultralytics opencv-python

📥 Download or Replace Video
Replace the default video with your own by renaming it:
mv "YourVideo.mp4" "Cars Moving On Road Stock Footage - Free Download.mp4"

▶️ Run the Script
python main.py
You should see a window pop up showing car detections and a live car count. Press q or Esc to quit.

🧠 How It Works
Uses YOLOv8 Nano (yolov8n.pt) for real-time detection.

Tracks objects using ByteTrack.

When a car crosses a horizontal line at 75% frame height (customizable), the counter increments.

Object IDs ensure cars are only counted once.

📝 Customization
Change detection line position: Modify LINE_RATIO in main.py (e.g. 0.6 for 60% height).

Use a different YOLO model: Replace 'yolov8n.pt' with other model variants like 'yolov8s.pt'.

📌 Notes
The model file (yolov8n.pt) will be downloaded automatically on first run, or you can download manually from Ultralytics.
