import csv
import argparse
from datetime import datetime
import os

CSV_FILE = "routes.csv"

# CSVにログを追加する関数
def add_location(route_name, lat, lon):
    today = datetime.now().strftime("%Y-%m-%d")
    data = [today, route_name, lat, lon]
    
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date", "route_name", "latitude", "longitude"])
        writer.writerow(data)
        
    print(f"[OK] {route_name} に位置情報を追加しました：({lat}, {lon})")

# コマンドライン引数を処理
def main():
    parser = argparse.ArgumentParser(description="道ログCLIツール")
    parser.add_argument("--add", nargs=3, metavar=("ROUTE", "LAT", "LON"),
                        help="ルート名と緯度・経度を記録する")
    
    args = parser.parse_args()
    
    if args.add:
        route, lat, lon = args.add
        try:
            lat = float(lat)
            lon = float(lon)
            add_location(route, lat, lon)
        except ValueError:
            print("[エラー] 緯度・経度は数字で入力してください。")
    else:
        print("使い方: python route_logger.py --add <ROUTE> <LAT> <LON>")

if __name__ == "__main__":
    main()
