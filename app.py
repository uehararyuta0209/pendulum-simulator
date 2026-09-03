from flask import Flask,render_template,send_file,request
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import io
from simulator import simulator
from double_pendulum import double_pendulum 
from stable_baselines3 import PPO
import gymnasium as gym
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph_rl')
def graph_rl():
    env = gym.make('Pendulum-v1')
    
    # 保存済みモデルを読み込む
    if os.path.exists("pendulum_model.zip"):
        model = PPO.load("pendulum_model", env=env)
    else:
        return "モデルが存在しません", 404
    # AIで振り子を制御
    obs, info = env.reset()
    rewards = []
    thetas = []
    times = []

    for i in range(200):
        action, _ = model.predict(obs)
        obs, reward, terminated, truncated, info = env.step(action)
        rewards.append(reward)
        thetas.append(obs[0])  # cos(θ)
        times.append(i)
        if terminated or truncated:
            break

    env.close()

    # グラフを生成
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(times, thetas, label='cos(θ)')
    ax.set_xlabel('Step')
    ax.set_ylabel('cos(θ)')
    ax.set_title('RL Pendulum Control')
    ax.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')
    
@app.route('/graph')
def graph():
    length = float(request.args.get('length', 1.0))
    angle  = float(request.args.get('angle', 30.0))
    b = float(request.args.get('b', 0.5))  # Get damping coefficient from query parameters
# ここにグラフを生成して返す処理
    t, theta, omega = simulator(length=length, angle_deg=angle, duration=10.0, b=b)  # Pass damping coefficient to simulator
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

@app.route('/graph2')
def graph2():
    l1     = float(request.args.get('l1', 1.0))
    l2     = float(request.args.get('l2', 1.0))
    angle1 = float(request.args.get('angle1', 90.0))
    angle2 = float(request.args.get('angle2', 45.0))

    t, theta1, theta2 = double_pendulum(
        l1=l1, l2=l2,
        angle1_deg=angle1, angle2_deg=angle2,
        duration=10.0
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t, theta1, label='pendulum1')
    ax.plot(t, theta2, label='pendulum2')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Angle (rad)')
    ax.set_title('Double Pendulum Motion')
    ax.legend()
    ax.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(True)
