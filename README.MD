Student - Karpiuk Nazar
Group - KI-48
Subject - CSTD

In this educational project was implemented a recognition system of European-style car license plates.

The OpenCV(https://github.com/opencv/opencv-python) library was used as the basis for the recognition of vehicle registration numbers (confirmation of their presence in the picture, finding their exact location) and pre-processing of images (resizing and reduction to a monochrome black and white pattern) as well. The decision to choose this library was based on software capabilities aimed at fast, non-resource-intensive calculations for graphics data processing.

As for the recognition of the text on the license plates, it was decided to use the EasyOCR library (https://github.com/JaidedAI/EasyOCR), due to its ability of data processing on the graphics core or CPU by choice. This step may decrease system performance, but at the same time reduce hardware requirements and energy consumption.
