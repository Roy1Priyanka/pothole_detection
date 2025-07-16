# Pothole Detection Using Images

This project automatically detects potholes in road images using classical image processing techniques like color filtering, edge detection, and contour analysis. It also compares detection results with ground truth labels and generates accuracy reports.

🔍 Project Objective

To identify potholes in static images using OpenCV, evaluate detection accuracy, and generate annotated output images and CSV reports for analysis.

🌐 Input Example

Here is a sample input image used for pothole detection:

🖼️ Input Image: road2.jpg



🌀 Output Example

Here is the output image after processing:

🖼️ Output Image: output_road2.jpg



✔️ Highlights:

Green rectangles indicate detected potholes

Image includes labels for detected count and accuracy



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
