from flask import request, render_template
import torch
import cv2
import os
from ultralytics import ASSETS, YOLO
from app import app

# Load your trained YOLOv8 model
model = YOLO('app/runs/detect/train25/weights/best.pt')

# Ensure directories exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

if not os.path.exists('processed'):
    os.makedirs('processed')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Save the uploaded file
        video_path = os.path.join('uploads', file.filename)
        file.save(video_path)

        # Process the video with your model
        processed_video_path = process_video(video_path)

        return render_template('result.html', video_path=processed_video_path)

def process_video(video_path):
    # Load the video using OpenCV
    cap = cv2.VideoCapture(video_path)
    
    # Output video path
    output_video_path = os.path.join('processed', 'processed_' + os.path.basename(video_path))
    
    # Get the video writer initialized to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = None
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Use the model to detect flaws in the video frames
        results = model(frame)
        
        # Extract the annotated frame
        annotated_frame = results[0].plot()
        
        # Initialize the video writer if it hasn't been
        if out is None:
            height, width, _ = annotated_frame.shape
            out = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))
        
        # Write the annotated frame to the output video
        out.write(annotated_frame)
    
    # Release everything once job is finished
    cap.release()
    out.release()

    # Return the path of the processed video
    return output_video_path
