# Project Scope

## Version 1: FaceID only

Registered user(s).

```text
Open webcam
Detect face
Compare with stored face
Access Granted / Access Denied
```

## Version 2: Uploaded image/video face identification

Given a registered user / images of that person, find occurences of the person in uploaded videos.

```text
Load video
Read frame by frame
Detect faces
Compare faces with known users
Draw names on video
Save output video
Generate simple report
```

### Uploaded Video Flow

```text
User uploads video
    ↓
System reads video frames
    ↓
Detect faces in each frame
    ↓
Generate face embeddings
    ↓
Compare with known face database
    ↓
Label each face as known / unknown
    ↓
Save processed video
    ↓
Save report with timestamps
```

Example result:

```text
00:00:03 - Andrew detected
00:00:08 - Unknown person detected
00:00:15 - Andrew detected
```

### Keep the First Version Simple

For video recognition, do not process every single frame at first.

Videos may have 30 frames per second. A 1-minute video can have:

```text
30 × 60 = 1800 frames
```

That can be slow.

So process every few frames:

```text
Process every 5th frame
```

or:

```text
Process 2 frames per second
```

This is much lighter.


### Main Features for Video Version

For the uploaded video feature, build these:

| Feature                              | Priority |
| ------------------------------------ | -------- |
| Load video file                      | High     |
| Read frames using OpenCV             | High     |
| Detect faces in frames               | High     |
| Compare faces with stored embeddings | High     |
| Draw box and name on face            | High     |
| Save output video                    | Medium   |
| Generate timestamp report            | Medium   |
| Track same person across frames      | Later    |
| Web upload interface                 | Later    |

