# Cartoonify-Image-Using-opencv-Python
This project transforms any real-world image into a cartoon-style image using Python and OpenCV.
It applies a combination of edge detection, image smoothing, and color quantization techniques to give photos a cartoonish look.

🚀 Features

Upload an image using a file dialog (EasyGUI).

Convert the image into a cartoon effect with OpenCV.

Display original and cartoon images side by side.

Save the cartoonified image for later use.

Simple and lightweight project, great for beginners in Computer Vision.

🛠️ Technologies Used

Python 3.x

OpenCV (cv2) – image processing

NumPy – array and matrix operations

Matplotlib – visualization

EasyGUI – file selection dialog

Pillow (PIL) – image saving

Installation

Clone the repository or copy the project files, then install dependencies using:

pip install -r requirements.txt


Contents of requirements.txt:

opencv-python
numpy
matplotlib
easygui
Pillow

▶️ How to Run

Open the project folder in VS Code (or terminal).

Run the script:

python new.py


A file dialog will open → Select an image from your computer.

The cartoonified image will be generated and displayed.

Save the result if you want.

📂 Project Structure
📁 Cartoonify-Image
│── new.py                  # Main Python script
│── requirements.txt        # Dependencies
│── haarcascade_frontalface_default.xml   # Haarcascade file (optional, if face detection is used)
│── README.md               # Project documentation

🎨 Example Output

Original Image → Cartoonified Image

(Add sample before/after images here if available)

📌 Future Enhancements

Add webcam support for real-time cartoonification.

Create a Flask web app to upload and cartoonify images online.

Add different cartoon styles and filters.

A fun mini-project to explore Computer Vision and Image Processing.

![Image](https://github.com/user-attachments/assets/6018fd12-1d0e-4eb9-8fb8-5d03271f7042)
