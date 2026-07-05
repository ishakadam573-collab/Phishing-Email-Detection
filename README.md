# Phishing-Email-Detection

## Overview
This project is a machine learning-based phishing email detection system developed using Python and Scikit-learn. The model is trained on a dataset of phishing and legitimate emails and predicts whether an email is "Phishing" or "Safe".

## Features
- Train a machine learning model on email data.
- Extract text features using TF-IDF Vectorizer.
- Classify emails as Phishing or Safe.
- Display model accuracy.
- Generate a confusion matrix for evaluation.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- NumPy
- Matplotlib
- Seaborn (optional)

## Dataset
The project uses an email dataset (`emails.csv`) containing email text and corresponding labels (Phishing or Safe).

## Project Structure
```
Phishing-Email-Detection/
│── pnq.py
│── emails.csv
│── README.md
```

## How to Run
1. Install the required libraries:
   ```
   pip install pandas scikit-learn matplotlib
   ```
2. Place `emails.csv` in the project folder.
3. Run the Python program:
   ```
   python pnq.py
   ```

## Output
- Email classification (Phishing/Safe)
- Model Accuracy
- Confusion Matrix

## Future Improvements
- Add a graphical user interface (GUI).
- Use advanced machine learning or deep learning models.
- Integrate with an email client for real-time phishing detection.

## Author
**Isha Kadam**
