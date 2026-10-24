from pathlib import Path
downloads=Path.home()/"Downloads"
klasorler = {
    "resim":downloads / "Resimler",
    "video": downloads / "Videolar",
    "metin": downloads / "Metin_Belgeleri",
    "ses": downloads / "Ses_Dosyalari",
    "setup": downloads / "Setup_Kurulum",
}
uzantilar={
    "resim": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico", ".heic"},
    "video": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".3gp"},
    "metin": {".txt", ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".md", ".rtf",".json"},
    "ses"  : {".mp3", ".wav", ".wma", ".ogg", ".m4a", ".flac", ".aac", ".amr"},
    "setup": {".exe", ".msi", ".apk", ".bat", ".dmg", ".pkg", ".iso", ".bin", ".zip", ".rar", ".7z",".py"}
}
number=1
numbers=0
for k_yolu in klasorler.values():
    k_yolu.mkdir(parents=True,exist_ok=True)
for file in downloads.iterdir():
    if file.is_file():
        uzanti=file.suffix.lower()
        for group, uzantikumesi in uzantilar.items():
            if uzanti in uzantikumesi:
                hedef_yol=klasorler[group]/file.name
                fname=file.stem
                uzanti2=file.suffix
                while hedef_yol.exists():
                    number+=1
                    new_file=f"{fname}({number}){uzanti2}"
                    hedef_yol=klasorler[group]/new_file
                if not hedef_yol.exists():
                    file.rename(hedef_yol)
                    print(file.name,"Taşındı-->",group)
                break

