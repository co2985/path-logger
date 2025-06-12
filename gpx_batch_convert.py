import gpxpy
import csv
import os

GPX_FOLDER = "gpx_logs"
CSV_FILE = "routes.csv"

def gpx_file_to_coords(filepath):
    with open(filepath, "r", encoding="utf-8") as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        coords = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    coords.append((point.latitude, point.longitude))
        return coords

def convert_all_gpx():
    if not os.path.exists(GPX_FOLDER):
        print(f"[!] '{GPX_FOLDER}' フォルダが存在しません。作成してください。")
        return

    all_coords = []
    for filename in os.listdir(GPX_FOLDER):
        if filename.lower().endswith(".gpx"):
            full_path = os.path.join(GPX_FOLDER, filename)
            coords = gpx_file_to_coords(full_path)
            all_coords.extend(coords)
            print(f"[OK] 読み込み成功: {filename}")

    if not all_coords:
        print("[!] GPXデータが見つかりませんでした。")
        return

    with open(CSV_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for lat, lon in all_coords:
            writer.writerow([lat, lon])
    print(f"[OK] {len(all_coords)} 点を {CSV_FILE} に書き出しました。")

if __name__ == "__main__":
    convert_all_gpx()
