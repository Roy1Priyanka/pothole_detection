# Pothole Detection Using Images

This project automatically detects potholes in road images using classical image processing techniques like color filtering, edge detection, and contour analysis. It also compares detection results with ground truth labels and generates accuracy reports.

🔍 Project Objective

To identify potholes in static images using OpenCV, evaluate detection accuracy, and generate annotated output images and CSV reports for analysis.

🌐 Input Examples

Below are all five input images used for pothole detection:

🖼️ https://github.com/Roy1Priyanka/pothole_detection/blob/main/road1.jpg

🖼️ https://github.com/Roy1Priyanka/pothole_detection/blob/main/road2.jpg

🖼️ https://github.com/Roy1Priyanka/pothole_detection/blob/main/road3.png

🖼️ https://github.com/Roy1Priyanka/pothole_detection/blob/main/road4.jpg

🖼️ https://github.com/Roy1Priyanka/pothole_detection/blob/main/road5.jpg

🌀 Output Examples

Below are the processed output images with detected potholes highlighted:

🖼️ output_road1.jpg

🖼️ output_road2.jpg

🖼️ output_road3.png

🖼️ output_road4.jpg

🖼️ output_road5.jpg

✔️ Highlights:

Green rectangles indicate detected potholes

Each image is annotated with pothole count and accuracy



📊 Accuracy Calculation

Each detection is evaluated with this formula:

Accuracy = TP / (TP + FP + FN)

Where:

TP = True Positives (correctly detected)

FP = False Positives (wrongly detected)

FN = False Negatives (missed detections)

🤔 Future Improvements

Integrate YOLOv5 for AI-based detection

Real-time video pothole detection from dashcam

Web/Mobile reporting system for smart cities
