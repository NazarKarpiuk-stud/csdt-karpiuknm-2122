Student - Karpiuk Nazar
Group - KI-48
Subject - CSTD

In this educational project was implemented a recognition system of European-style car license plates.

## How to run:
Install requirements:
``` bash
pip install -r requirements.txt
```

Run script:
``` bash
python3 main.py
```

## About
The OpenCV(https://github.com/opencv/opencv-python) library was used as the basis for the recognition of vehicle registration numbers (confirmation of their presence in the picture, finding their exact location) and pre-processing of images (resizing and reduction to a monochrome black and white pattern) as well. The decision to choose this library was based on software capabilities aimed at fast, non-resource-intensive calculations for graphics data processing.

As for the recognition of the text on the license plates, it was decided to use the EasyOCR library (https://github.com/JaidedAI/EasyOCR), due to its ability of data processing on the graphics core or CPU by choice. This step may decrease system performance, but at the same time reduce hardware requirements and energy consumption.

For the role of database was chosen SQLite. A simple, small, fast, full-featured SQL database engine.

Unit and Integrational tests was built using python unittest tool

v.1.0.
  - added tag
  - held tests

v.1.1
  - rewrote README.MD
  - added destination file for logging system

## Acknowledgement and References
EasyOCR project is based on research and code from several papers and open-source repositories. All deep learning execution is based on Pytorch. Detection execution uses the CRAFT algorithm from this official repository and their paper. The recognition model is a CRNN (paper). It is composed of 3 main components: feature extraction (Resnet) and VGG, sequence labeling (LSTM) and decoding (CTC). The training pipeline for recognition execution is a modified version of the deep-text-recognition-benchmark framework and Data synthesis is based on TextRecognitionDataGenerator.

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code. The library has more than 2500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects, etc.
