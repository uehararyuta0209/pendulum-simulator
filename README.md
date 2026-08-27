![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)
# pendulum-simulator
    物理シミュレーターを実装する
    振り子の長さ、初期角度、観察時間を変化させて
    そのグラフを作成する
# 使い方
    1.リポジトリをクローンする
        https://github.com/uehararyuta0209/pendulum-simulator からすべてのリポジトリを使用者のローカル環境に以下のコマンドでクローンする
        ```bash
        git clone https://github.com/uehararyuta0209/pendulum-simulator.git
        ```
    2.ライブラリをインストールする
        ```bash
        pip install -r requirements.txt
        ```
        この中のに環境があるので、このコマンドを実行してダウンロードする
    3.サーバーを起動する
        ```bash
        flask run
        ```
        このコマンドを入力してflaskを起動する
    4.ブラウザで開く
        http://127.0.0.1:5000 をURLに張り付けて開くと使用可能
# 技術スタック
    python, flask, numpy, scipy, matplotlib
# フォルダ構成
```
pendulum-simulator/
├── app.py
├── simulator.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
```
# 機能
- 振り子の長さを変更できる
- 初期角度を変更できる
- グラフをブラウザで表示できる