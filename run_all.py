import subprocess

def run_gpx_converter():
    print("▶ GPX → CSV 変換中...")
    subprocess.run(["python3", "gpx_batch_convert.py"])

def run_map_generator():
    print("▶ 地図HTML生成中...")
    subprocess.run(["python3", "show_map.py"])

def open_map_html():
    print("▶ ブラウザで地図を表示します...")
    import webbrowser
    import os
    html_path = os.path.abspath("routes_map.html")
    webbrowser.open("file://" + html_path, new=2)


if __name__ == "__main__":
    run_gpx_converter()
    run_map_generator()
    open_map_html()
