import gpxpy
import csv

GPX_FILE = "11-Jun-2025-0112.gpx"
CSV_FILE = "routes.csv"

def gpx_to_csv():
    with open(GPX_FILE, "r", encoding="utf-8") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    with open(CSV_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lat = point.latitude
                    lon = point.longitude
                    writer.writerow([lat, lon])
    print(f"[OK] {CSV_FILE} に座標を追記しました。")

if __name__ == "__main__":
    gpx_to_csv()
