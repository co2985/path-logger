import pandas as pd
import folium

CSV_FILE = "routes.csv"
OUTPUT_FILE = "static/routes_map.html"

def show_map():
    df = pd.read_csv(CSV_FILE, header=None, names=["latitude", "longitude"])
    if df.empty:
        print("[!] CSVにデータがありません。")
        return

    # 地図の中心は最初の地点
    first_point = df.iloc[0]
    m = folium.Map(location=[first_point.latitude, first_point.longitude], zoom_start=17)

    # 全体の軌跡を線で描画
    points = df[["latitude", "longitude"]].values.tolist()
    folium.PolyLine(points, color="blue", weight=5, opacity=0.8).add_to(m)

    # 地図をHTMLで出力
    m.save(OUTPUT_FILE)
    print(f"[OK] 地図を作成しました: {OUTPUT_FILE}")

if __name__ == "__main__":
    show_map()
