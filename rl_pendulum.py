import gymnasium as gym
from stable_baselines3 import PPO
import os

env = gym.make('Pendulum-v1')

# 保存済みモデルがあれば読み込む
if os.path.exists("pendulum_model.zip"):
    print("保存済みモデルを読み込みます...")
    model = PPO.load("pendulum_model", env=env)
    # 学習する
    model.learn(total_timesteps=500000)
else:
    print("新しいモデルを作成します...")
    model = PPO("MlpPolicy", env)
    # 学習する
    model.learn(total_timesteps=500000)


# 保存する
model.save("pendulum_model")
print("モデルを保存しました！")

# 確認する
obs, info = env.reset()
print(f"最初の状態: {obs}")

for i in range(10):
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"Step {i+1}: 報酬={reward:.2f}")

env.close()