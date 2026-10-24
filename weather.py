import time
import requests
import sqlite3
import numpy as np
URL = "https://api.open-meteo.com/v1/forecast"
db_connection=sqlite3.connect("weather.db")
imlec=db_connection.cursor()
imlec.execute("""
CREATE TABLE IF NOT EXISTS silivri_weather(
id INTEGER PRIMARY KEY AUTOINCREMENT,
temperature REAL,
wind_speed REAL,
date TEXT,
location TEXT,
time REAL

)


""")
user_latitude=200
user_longitude=200
while True:
    decision=input("Enter 'SAVE' to save wheather to database, 'VIEW' for see previous saves,'EXIT' to  exit,'EVENT' to view weather events,'AVERAGE' to see average weather conditions:").lower()
    if(decision=="save"):
        try:
            while not(-180<=user_longitude<=180 and -90<=user_latitude<=90):
                print("Geçerli bir enlem ve boylam değeri girin.")
                user_latitude=float(input("Enter latitude your coordinates:"))
                user_longitude=float(input("Enter longitudes your coordinates:"))
        except Exception:
            user_latitude=41.0737
            user_longitude=28.2479
            print("Silivri:",end="")
        location=str(user_latitude)+","+str(user_longitude)
        print(f"{location} konumunun hava durumu kaydedeilecek.")
        param = {
        "latitude": user_latitude,
        "longitude": user_longitude,
        "current": "temperature_2m,wind_speed_10m"
        }
        answer = requests.get(URL, params=param)
        status = answer.status_code
        if(status==200):
            data=answer.json()
            temperature=data["current"]["temperature_2m"]
            wind_speed=data["current"]["wind_speed_10m"]
            stime=time.time()
            date_1=time.localtime()
            date_2=time.strftime("TARİH_%d,%m,%Y,SAAT_%H,%M,%S")
            imlec.execute(
                "INSERT INTO silivri_weather(temperature,wind_speed,date,location,time)VALUES(?,?,?,?,?)",
                (temperature,wind_speed,date_2,location,stime)
    )
            db_connection.commit()
        else:
            print("Could not connected to API")
    elif(decision=="view"):
        imlec.execute("SELECT id,temperature,wind_speed,date,location FROM silivri_weather")
        saves=imlec.fetchall()
        if not saves:
            print("Could not find any saves.")
        else:
            for row in saves:
                no=row[0]
                temperature=row[1]
                wind_speed=row[2]
                date=row[3]
                location=row[4]
                print(f"{no}. kayıt_ {temperature}_derece {wind_speed}km/s  _rüzgar hızı {date} konum_{location}")
    elif(decision=="exit"):
        print("Program ended.")
        break
    elif(decision=="event"):
        imlec.execute("SELECT DISTINCT location FROM silivri_weather")
        distinct_location=imlec.fetchall()
        for x in distinct_location:
            location=x[0]
            imlec.execute("""
            SELECT temperature,wind_speed,time
            FROM silivri_weather
            WHERE location=?
            ORDER BY time DESC LIMIT 2
            """,(location,))
            two_weathers=imlec.fetchall()
            if (len(two_weathers)>=2):
                old_tuple=two_weathers[1]
                new_tuple=two_weathers[0]
                t1=old_tuple[0]
                t2=new_tuple[0]
                w1=old_tuple[1]
                w2=new_tuple[1]
                time1=old_tuple[2]
                time2=new_tuple[2]
                time_difference=time2-time1
                temperature_difference=t2-t1
                wind_speed_difference=w2-w1
                if time_difference!=0:
                    temperature_formule=(temperature_difference/time_difference)*3600
                    wind_speed_formule=(wind_speed_difference/time_difference)*3600
                    if temperature_formule<=-5:
                        print(location,":Şiddetli soğuk hava cephesi giriş yapıyor!")
                    if wind_speed_formule>=15:
                        print(location,":Rüzgar hızı artıyor,fırtına tehlikesi!")
                    if temperature_formule<=-5 and wind_speed_formule>=15:
                        print(location,"Şiddetli fırtına geliyor!")
                    if temperature_formule>-5 and wind_speed_formule<15:
                        print(location,"Hava koşulları kararlı.")
    elif(decision=="average"):
        imlec.execute("SELECT DISTINCT location FROM silivri_weather")
        distinct_location=imlec.fetchall()
        for x in distinct_location:
            location=x[0]
            imlec.execute("""
            SELECT temperature,wind_speed
            FROM silivri_weather
            WHERE location=?
            """,(location,))
            dizi=np.array(imlec.fetchall())
            if len(dizi)>0:
                t_aver=dizi[:,0].mean()
                w_aver=dizi[:,1].mean()
                print(f"KONUM={location} ORTALAMA SICAKLIK={t_aver} ORTALAMA RÜZGAR HIZI={w_aver}")
    else:
        print("Invalid syntax.")

db_connection.close()
    
