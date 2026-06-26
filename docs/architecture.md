# System Architecture

## Overview

Version 1 is a small FaceID application for live webcam authentication.

The system opens the webcam, detects a face in the current frame, compares that face with stored registered-user face data, and returns one result:

```text
Access Granted / Access Denied
```

The v1 architecture should stay simple. Use a modular monolith rather than microservices, queues, alerts, tracking, or uploaded-video processing.

## Version 1 Scope

Included in v1:

* open the local webcam
* detect a face in webcam frames
* generate or load a face embedding
* compare the detected face with stored registered-user embeddings
* show access granted when the face matches a registered user
* show access denied when no match is found

Not included in v1:

* uploaded image or video recognition
* frame-by-frame video processing
* drawing names on saved videos
* timestamp reports
* person tracking across frames
* web upload interface
* notification or alert delivery
* real microservices or event-driven infrastructure

## High-Level Flow

```text
Start application
    |
Open webcam
    |
Read frame
    |
Detect face
    |
Generate face embedding
    |
Compare with registered-user embeddings
    |
Return Access Granted or Access Denied
```

## Main Modules

### 1. Application Entry Point

Starts the application and coordinates the webcam authentication flow.

Responsibilities:

* load configuration
* load registered-user face data
* start webcam capture
* call the face detection and recognition modules
* display the final result

### 2. Camera Module

Handles live webcam input.

Responsibilities:

* open the webcam
* read frames
* release the camera when the application exits
* report camera failures clearly

For v1, the camera module only needs to support one local webcam.

### 3. Detection Module

Finds faces in a webcam frame.

Responsibilities:

* receive an image frame
* detect whether a face is present
* return the face location or cropped face region
* handle the case where no face is detected

For v1, the simplest useful behavior is to authenticate one face at a time. If multiple faces are detected, the app can deny access or choose the largest/clearest face.

### 4. Recognition Module

Compares a detected face with registered-user face data.

Responsibilities:

* generate an embedding for the detected face
* compare it with stored registered-user embeddings
* apply a match threshold
* return a match result with a confidence or distance score

The recognition module should not decide UI behavior. It should return data such as `matched`, `user_id`, `name`, and `score`, and the application entry point can display `Access Granted` or `Access Denied`.

### 5. Enrollment Module

Registers a user for future recognition.

Responsibilities:

* capture or load a clear face image for a registered user
* generate the user's face embedding
* store the user's ID, display name, and embedding

Enrollment can be a simple script or command in v1. It does not need a full admin dashboard.

### 6. Data Module

Reads and writes registered-user data.

Responsibilities:

* load known users
* save new enrolled users
* keep embeddings in a predictable local format
* avoid storing unnecessary raw face images

For v1, a local file-based store is enough. A database can be added later if the project grows.

## Storage

### Registered Users Store

Stores the users who are allowed to pass FaceID authentication.

Suggested fields:

* user ID
* display name
* face embedding
* enrollment date
* active/inactive status

### Optional Local Log

V1 may keep a small local log for debugging.

Useful fields:

* timestamp
* result: granted or denied
* matched user ID if known
* confidence or distance score
* error message if authentication failed because of camera or detection issues

This log should stay local and simple. A full audit service is not needed for v1.

## Suggested Folder Structure

```text
src/
├── main.py
├── camera/
│   └── webcam.py
├── detection/
│   └── face_detector.py
├── recognition/
│   └── face_recognizer.py
├── enrollment/
│   └── enroll_user.py
├── data/
│   ├── known_faces/
│   └── logs/
├── config/
│   └── settings.py
└── utils/
    └── image_utils.py

tests/
├── test_detection.py
├── test_recognition.py
└── test_enrollment.py

requirements.txt
README.md
.gitignore
```

## Error Handling

The v1 app should handle these cases clearly:

* webcam cannot be opened
* no face is detected
* more than one face is detected
* face embedding cannot be generated
* no registered users exist
* detected face does not match any registered user

Authentication should fail closed. If the app is unsure, it should return `Access Denied`.

## Security and Privacy Considerations

Because the system handles face data, v1 should keep privacy rules simple and strict:

* only enroll people with permission
* avoid storing raw face images unless needed for testing or re-enrollment
* store embeddings outside source control
* keep local data files out of git
* restrict access to enrolled-user data
* do not use the system for unauthorized surveillance

Encryption and formal retention policies can be added later, but v1 should already avoid collecting unnecessary data.

## Future Architecture

Version 2 can add uploaded image or video recognition:

```text
Load video
Read selected frames
Detect faces
Compare faces with known users
Draw names on video
Save output video
Generate simple timestamp report
```

If the project grows beyond v1, consider adding:

* a database for users and embeddings
* a web interface
* background jobs for video processing
* richer audit logs
* notification or alert delivery
* microservices only if separate deployment becomes necessary

These are future extensions, not part of the v1 architecture.
