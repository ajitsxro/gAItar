from ultralytics import YOLO

# Attempt to load the model
model = YOLO('runs/detect/train25/weights/best.pt')
print("Model loaded successfully!")
