# gAItar

## Description

gAItar is a computer vision software that analyzes videos of users playing the guitar and highlights errors in their technique.

## Features

- Upload guitar videos for analysis (make sure guitar is fully in frame and video is clear!)
- Detects flaws (thumb, wrist, strumming placement)
- Processed video with highlighted featuers

## Getting Started

### Prerequisites

- Python 3.6+
- Flask
- Ultralytics
- Open CV
- Torch
- Numpy

### Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/ajitsxro/gAItar.git
   cd gAItar

   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt

   ```

3. Running the Application

   ```bash
   python app/__init__.py
   # OR #
   flask run
   ```

4. Open your web browswer and go to http://127.0.0.1:5000

5. Usage

   Upload a video of you playing the guitar.
   The model will analyze the video and return a processed video stored in the processed folder!

## Contribution

Contributions are welcome! Please open an issue or submit a pull request.

Enjoy!
