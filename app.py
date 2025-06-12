from flask import Flask, request, render_template, redirect, url_for
import os
import shutil
import subprocess

UPLOAD_FOLDER = 'gpx_logs'
ALLOWED_EXTENSIONS = {'gpx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 拡張子が.gpxかどうか確認
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# アップロード画面
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if 'file' not in request.files:
            return "ファイルがありません"

        file = request.files['file']
        if file.filename == '':
            return "ファイル名が空です"

        if file and allowed_file(file.filename):
            # ファイルを保存
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # 既存の変換・表示スクリプトを実行
            subprocess.run(["python3", "gpx_batch_convert.py"])
            subprocess.run(["python3", "show_map.py"])

            return redirect(url_for('show_map'))

    return '''
    <!doctype html>
    <title>GPXアップロード</title>
    <h1>GPXファイルをアップロードしてください</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file accept=".gpx">
      <input type=submit value=アップロード>
    </form>
    '''

# 地図表示ページ
@app.route("/map")
def show_map():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)
