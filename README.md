# FaceID

FaceID is a small learning project for webcam-based face authentication.

The first version keeps the flow simple:

```text
Open webcam
Detect face
Compare with stored face
Access Granted / Access Denied
```

## Version 1 Goal

Build a local app that can recognize registered users from a webcam frame.

V1 includes:

* webcam input
* face detection
* face embedding comparison
* registered-user enrollment
* access granted or denied result

## Project Docs

* [Project scope](docs/scope.md)
* [System architecture](docs/architecture.md)

## Run Locally

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Run the webcam face detector:

```bash
venv/bin/python src/main.py
```

Press `q` to close the camera window.

## Planned Structure

```text
src/
├── main.py
├── camera/
├── detection/
├── recognition/
├── enrollment/
├── data/
├── config/
└── utils/
```

## Status

The project is currently in the planning stage. The scope and architecture are documented, and implementation will start with the simple webcam FaceID flow.

## Privacy

Face data is sensitive. Registered-user images and embeddings should stay local, stay out of source control, and only be created with permission.
