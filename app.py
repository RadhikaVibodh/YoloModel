from flask import Flask, render_template, Response
from inference import VideoCamera

app = Flask(__name__)

camera = None

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            break


@app.route('/video_feed')
def video_feed():
    global camera
    if camera is None:
        camera = VideoCamera()
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/start')
def start_camera():
    global camera
    camera = VideoCamera()
    return "Camera Started"


@app.route('/stop')
def stop_camera():
    global camera
    if camera:
        camera.stop()
    camera = None
    return "Camera Stopped"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
