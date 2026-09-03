![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

# 🔵 pendulum-simulator
A physics simulator for pendulum motion.
Visualize the motion of a pendulum by adjusting its length, initial angle, and observation time.
Supports both normal pendulum and double pendulum simulation, demonstrating chaotic motion.

# 🚀 Getting Started
1. Clone the repository
```bash
git clone https://github.com/uehararyuta0209/pendulum-simulator.git
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Start the server
```bash
flask run
```

4. Open your browser
    Navigate to `http://127.0.0.1:5000`

# 🛠 Tech Stack
| Library    | Purpose |
|------------|---------|
| Python     | Main programming language |
| Flask      | Web server & browser display |
| NumPy      | Numerical computation |
| SciPy      | Solving pendulum equations of motion |
| Matplotlib | Graph rendering & image generation |

# 📁 Project Structure
```text
pendulum-simulator/
├── app.py
├── simulator.py
├── double_pendulum.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

# ✨ Features
- Adjust pendulum length
- Adjust initial angle
- Adjust damping coefficient
- Visualize motion graph in browser
- Switch between normal and double pendulum simulation
- Real-time graph update without page reload

# 📝 License
MIT License