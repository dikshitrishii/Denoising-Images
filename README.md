## Denoising Low-Light Image using CNN Networks
## Project Description
This project aims to improve the quality of low-light images by leveraging a Convolutional Neural Network (CNN). Low-light conditions often result in images with poor visibility, high noise levels, and reduced detail, which can impede various computer vision tasks. Our goal is to develop a CNN-based model that can effectively denoise and enhance these images, making them more usable and improving their quality.

## Architecture
The model architecture consists of several convolutional layers designed to extract features and reduce noise. Key components include:
- **Input Layer**: Accepts RGB images of any resolution.
- **Convolution Layers**: Multiple layers with 32 filters each, using 3x3 kernels and ReLU activation.
- **Skip Connections**: Added to help retain and utilize information from previous layers.
- **Output Layer**: A convolutional layer with activation to create the final enhanced image.

## How to Run
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/dikshitrishii/Denoising-Images.git
    ```
2. **Go to project directory**:
    ```sh
    cd Denoising-Images
    ```
3. **Run the Main Script**:
    ```sh
    python main.py
    ```
## Keep low light image in test/low folder run the script and it's denoised image will be saved in test/predicted
