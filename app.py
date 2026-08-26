from flask import Flask,render_template,send_file
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import io
from simulator import simulator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
# ここにグラフを生成して返す処理
    t, theta, omega = simulator(length=1.0, angle_deg=30.0, duration=10.0)
    plt.figure(figsize=(10, 6))
    plt.plot(t, theta)
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.title('Pendulum Motion')
    plt.grid(True)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(True)
