# YOLO Travel 主程式
- - -

## 開發環境 ##
Ubuntu 16.04

Python 3.5.2

Sqlite3

## 設定虛擬環境 ##

移動至YOLOTravel檔案目錄下之後

    virtualenv -p python3 venv

    source venv/bin/activate

## 初始化套件 ##

    pip install -r requirements.txt

## 初始化設定 ##

建立資料表所需之 migrate 文件

    python manage.py makemigrations

透過 migrate 建立資料表

    python manage.py migrate

建立後台管理員

    python manage.py createsuperuser

## 啟用Server ##

    python manage.py runserver
