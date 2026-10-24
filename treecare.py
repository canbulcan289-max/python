import time
import sqlite3
aylara_gore_budama = {
    1: [], 
    
    2: [
        "elma", "armut", "ayva", "erik", "kiraz", 
        "vişne", "badem", "zeytin", "incir", "nar"
    ],  
    
    3: [
        "elma", "armut", "ayva", "şeftali", "kayısı", 
        "erik", "kiraz", "vişne", "badem", "ceviz", 
        "zeytin", "incir", "nar", "portakal","mandalina"
    ],  
    
    4: [
        "şeftali", "kayısı", "ceviz", "zeytin", "portakal", "mandalina"
    ],  
}
# Takvimdeki tüm benzersiz meyve ağaçları listesi

meyve_agaclari = [
    "armut",
    "ayva",
    "badem",
    "ceviz",
    "elma",
    "erik",
    "incir",
    "kayısı",
    "kiraz",
    "nar",
    "şeftali",
    "portakal",
    "mandalina",
    "vişne",
    "zeytin"
]

db_connection=sqlite3.connect("tree.db")
imlec=db_connection.cursor()
imlec.execute("""
CREATE TABLE IF NOT EXISTS tree_care(
id INTEGER PRIMARY KEY AUTOINCREMENT,
tree TEXT

)


""")
def okuyucu():
    imlec.execute("SELECT tree FROM tree_care")
    veriler=imlec.fetchall()
    x=[satir[0] for satir in veriler]
    return x


while True:
    buda_agac=[]
    karar=input("Yeni ağaç türü eklemek için GİR, ağaç türü kaldırmak için SİL, ağaçların budama zamanlarını görmek için GÖR, kayıtlı ağaçları görmek için LİSTE, çıkmak için ÇIK yazın. ").lower()
    if karar=="gir":
        trees=okuyucu()
        new_tree=input("Yeni ağacı girin:").lower()
        if new_tree in meyve_agaclari and new_tree not in trees:
            imlec.execute(
                "INSERT INTO tree_care(tree)VALUES(?)",
                (new_tree,)
                )
            db_connection.commit()
            print("Yeni ağaç kaydedildi.")
        elif new_tree in meyve_agaclari and new_tree in trees:
            print("Bu ağaç türü zaten kayıtlı")
        else:
            print("Ağaç kaydedilemedi.Sistem bu ağacı tanımıyor.")
    elif karar=="sil":
        trees=okuyucu()
        silinecek=input("Kaldırmak istediğiniz ağaç türünü girin:").lower()
        if silinecek in trees:
            imlec.execute(
                "DELETE FROM tree_care WHERE tree=?",
                (silinecek,)
                )
            db_connection.commit()
            print("Ağaç kaldırıldı.")
        else:
            print("Listede böyle bir ağaç yok.")
    elif karar=="gör":
        local_time=time.localtime()
        guncel_ay=int(time.strftime("%m"))
        uygun_agaclar=aylara_gore_budama.get(guncel_ay,[])
        trees=okuyucu()
        for x in trees:
            if x in uygun_agaclar:
                buda_agac.append(x)
        print(f"Budanabilen ağaçlar={buda_agac}")
    elif karar=="çık":
        print("Program sonlandı.")
        break
    elif karar=="liste":
        trees=okuyucu()
        print(trees)
    else:
        print("Anlamsız karar.")
db_connection.close()