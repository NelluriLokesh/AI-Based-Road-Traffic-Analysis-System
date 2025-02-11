# AI-Based Road Traffic Analysis System
=====================================

![Traffic Analysis Video](https://github.com/NelluriLokesh/AI-Based-Road-Traffic-Analysis-System/blob/main/output.avi)
## Table of Contents
-----------------

* [Overview](#overview)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Uploading a Video File](#uploading-a-video-file)
* [Requirements](#requirements)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)
* [Author](#author)
* [Contact](#contact)

## Overview
------------

This project utilizes advanced computer vision techniques and deep learning models to analyze road traffic in real-time. The system detects vehicles, counts them, and provides insights into traffic patterns, making it an essential tool for traffic management and urban planning.

### Key Benefits

* Real-time vehicle detection and counting
* Traffic visualization with annotated video feeds
* Output video with annotations for further analysis

## Features
------------

### Real-Time Vehicle Detection

* Leverages YOLOv5 for fast and accurate vehicle detection
* Supports various video formats and resolutions

### Vehicle Counting

* Counts vehicles passing a designated line in the video feed
* Provides accurate counting even in crowded scenes

### Traffic Visualization

* Displays annotated video feeds with detected vehicles
* Supports various annotation styles and colors

### Output Video

* Saves processed video with annotations for further analysis
* Supports various video formats and resolutions

## Installation
------------

To set up the project on your local machine, follow these steps:

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd AI-based-road-traffic-analysis-system
```

### Step 2: Install the Required Packages

```bash
pip install -r requirements.txt
```

## Usage
-----

### Step 1: Prepare your Video File

* Place your video file in the project directory

### Step 2: Run the Main Script

```bash
python Main.py
```

### Step 3: View the Output

* The processed video will be saved as `output.avi` in the project directory

## Uploading a Video File
-------------------------

To upload a video file for processing, follow these steps:

1. **Prepare Your Video**: Ensure your video file is in a supported format (e.g., MP4, AVI).
2. **Place the Video in the Project Directory**:
   - Copy your video file to the project directory where the `Main.py` script is located:
     ```
     c:\Visual Studio codes\Mini Projects\AI-based road traffic analysis system\
     ```
3. **Run the Script**: After placing the video file in the project directory, run the `Main.py` script to start processing the video.

4. **View the Output**: The processed video will be saved as `output.avi` in the same directory.

## Requirements
------------

* **Python**: Version 3.x
* **Libraries**:
	+ OpenCV
	+ PyTorch
	+ NumPy

## Contributing
------------

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License
-------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
------------

* **YOLOv5**: For providing the vehicle detection capabilities
* **OpenCV**: For video processing functionalities

## Author
-------
Nelluri Lokesh

## Contact
-------

For any inquiries or feedback, please reach out at [lokesh.nelluri12@gmail.com].
