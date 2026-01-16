import cv2
import os

video_path = 'C:/Users/12445/DownloadS/MicrosoftTeams-video.mp4' #Training samples / input videos
output_folder = 'frames_50fps'
os.makedirs(output_folder, exist_ok=True)



cap = cv2.VideoCapture(video_path)


# Check if video opened
if not cap.isOpened():
    print("❌ Could not open video. Check the path OR codec.")
    print("Path used:", video_path)
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))  # frames per second of video

desired_fps = 5   # can modify as per video
save_every = max(1, int(fps / desired_fps))   # avoid zero

frame_count = 0
saved_count = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    if frame_count % save_every  == 0:  # save one frame per second
        frame_filename = os.path.join(output_folder, f"frame_{saved_count:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"✅ {saved_count} frames saved in '{desired_fps}' (1 frame/sec)")
