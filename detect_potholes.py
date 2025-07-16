import cv2
import numpy as np
import os
import csv

# 👇 Define true pothole counts (you must manually provide this)
ground_truth = {
    'road2.jpg': 3,
    'road3.png': 2,
    'road5.jpg': 1,
    # Add more as needed
}

image_folder = 'images'
output_csv = 'pothole_report_with_accuracy.csv'

image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Prepare CSV to save results
with open(output_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Image', 'Ground Truth', 'Detected', 'TP', 'FP', 'FN', 'Accuracy (%)'])

    for img_name in image_files:
        print(f"\nProcessing: {img_name}")
        image_path = os.path.join(image_folder, img_name)
        image = cv2.imread(image_path)

        if image is None:
            print(f"[ERROR] Could not load image: {image_path}")
            continue

        # --- CLAHE for contrast ---
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        cl = clahe.apply(l)
        enhanced_lab = cv2.merge((cl, a, b))
        enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

        # --- Mask dark regions using HSV ---
        hsv = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2HSV)
        lower_dark = np.array([0, 0, 0])
        upper_dark = np.array([180, 255, 60])
        mask = cv2.inRange(hsv, lower_dark, upper_dark)

        # --- Morphological operations ---
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

        # --- Contour detection ---
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        detected_count = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 200:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                detected_count += 1

        # --- Accuracy calculation ---
        true_count = ground_truth.get(img_name, 0)
        TP = min(detected_count, true_count)
        FP = max(0, detected_count - TP)
        FN = max(0, true_count - TP)
        accuracy = (TP / (TP + FP + FN)) * 100 if (TP + FP + FN) > 0 else 0

        # --- Annotate image ---
        cv2.putText(image, f"Potholes: {detected_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(image, f"Accuracy: {accuracy:.2f}%", (10, 65),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        # --- Save output ---
        output_path = os.path.join(image_folder, f"output_{img_name}")
        cv2.imwrite(output_path, image)
        print(f"Saved: {output_path} | Detected: {detected_count}, Ground Truth: {true_count}, Accuracy: {accuracy:.2f}%")

        writer.writerow([img_name, true_count, detected_count, TP, FP, FN, f"{accuracy:.2f}"])

        # --- Display ---
        cv2.imshow("Pothole Detection", image)
        print("Press any key to continue...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

print(f"\n✅ Report saved as {output_csv}")
