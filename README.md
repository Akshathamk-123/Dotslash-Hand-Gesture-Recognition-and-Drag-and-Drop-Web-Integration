# dotslash_10_eliteforce
This is the Project that was built as a part of a 24-hackathon called dotslash in Campus.

# Hand Gesture Recognition and Drag-and-Drop Web Integration

## Project Overview

This project implements hand gesture recognition for drawing and drag-and-drop functionalities using OpenCV and MediaPipe. The recognized gestures are used to draw shapes and move images on a virtual canvas. Additionally, this project integrates the hand gesture application into a Flask web application, providing a web interface for the user.

## Features

1. **Hand Gesture Recognition**: Uses MediaPipe and OpenCV to detect hand gestures.
2. **Drawing Shapes**: Recognize gestures to draw lines, rectangles, circles, and free-hand drawings.
3. **Drag-and-Drop**: Allows dragging and dropping images using hand gestures.
4. **Web Integration**: Integrates the hand gesture application into a Flask web app for live video streaming and interaction.

## Project Structure

```plaintext
.
├── ai_virtual_painter.py
├── app_for_drag_and_drop.py
├── app_integration_into_a_website.py
├── templates
│   ├── first_page.html
│   └── index.html
└── static
    ├── assets
    │   └── back.jpeg
    └── css
        └── styles.css
```

## Setup and Installation

### Prerequisites

- Python 3.x
- OpenCV
- MediaPipe
- Flask
- cvzone

### Installation

1. **Clone the Repository**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install Dependencies**

    ```bash
    pip install opencv-python mediapipe flask cvzone
    ```

3. **Download Hand Tools Image**

    Download `tools.png` and place it in the project directory.

4. **Prepare Images for Drag-and-Drop**

    Create a directory named `ImagesPNG` and place the images you want to use for drag-and-drop.

### Running the Application

1. **Hand Gesture Drawing Application**

    ```bash
    python ai_virtual_painter.py
    ```

2. **Hand Gesture Drag-and-Drop Application**

    ```bash
    python app_for_drag_and_drop.py
    ```

3. **Web Integration**

    ```bash
    python app_integration_into_a_website.py
    ```

    Open your web browser and navigate to `http://127.0.0.1:5000` to access the web application.

## File Descriptions

### `ai_virtual_painter.py`

This script implements a virtual painter using hand gestures. It recognizes the following tools based on the position of the index finger:

- **Line**: Draws lines.
- **Rectangle**: Draws rectangles.
- **Draw**: Free-hand drawing.
- **Circle**: Draws circles.
- **Erase**: Erases drawn content.

### `app_for_drag_and_drop.py`

This script implements a drag-and-drop feature using hand gestures. The application detects the position of the index finger to move images around the screen.

### `app_integration_into_a_website.py`

This script integrates the hand gesture functionalities into a Flask web application. It provides live video streaming from the webcam and allows users to interact with the application through the web interface.

### `templates/first_page.html`

The home page of the web application with a button to start the live streaming.

### `templates/index.html`

The page that displays the live streaming and allows interaction with the hand gesture application.

## Usage

- Run `app_integration_into_a_website.py` to start the Flask web application.
- Access the home page at `http://127.0.0.1:5000`.
- Click on the "Try out" button to start the live streaming and interact with the hand gesture application.

## Notes

- Ensure your webcam is connected and functioning properly.
- The `tools.png` image should contain icons for the tools (line, rectangle, draw, circle, erase) placed horizontally.

## License

This project is licensed under the MIT License.

---

Enjoy interacting with the hand gesture recognition and drag-and-drop web application!
