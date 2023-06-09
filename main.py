# DataFrame'de kullanabilmek adına pandas'ı import ettik
import pandas as pd

# Diğer class'lardaki fonksiyonları çağırmak ve kullanabilmek adına
# Bu class'ları import ettik
import insan
import issiz
import calisan
import maviyaka
import beyazyaka


# Nesnelerimizi oluşturmak adına main fonksiyonumuzu oluşturduk
def main():
    # İnsan sınıfı için örnek nesne ürettik
    insan1 = insan.Insan("13241203521", "Zekeriya", "Güven", 26, "Erkek", "Türkiye")
    insan2 = insan.Insan("98765432109", "Müge", "Oluçoğlu", 24, "Kadın", "Türkiye")

    # Insan nesnelerini __str__ metodunu da kullanarak yazdırdık
    print(insan1)
    print("******************************************")
    print(insan2)
    print("******************************************")

    # Issiz sınıfı için 3 örnek nesne oluşturduk
    issiz1 = issiz.Issiz("36123413516", "Mehmet", "Kara", 35, "Erkek", "Türkiye", 2, 10, 1)
    issiz2 = issiz.Issiz("98765432108", "Ali", "Yıldız", 28, "Erkek", "Türkiye", 10, 3, 1)
    issiz3 = issiz.Issiz("45123514623", "Ebru", "Koç", 40, "Kadın", "Türkiye", 2, 2, 8)

    # Issiz nesnelerini __str__ metodu ile yazdırdık
    print(issiz1)
    print("******************************************")
    print(issiz2)
    print("******************************************")
    print(issiz3)
    print("******************************************")

    # Calisan sınıfı için 3 örnek nesne oluşturduk
    calisan1 = calisan.Calisan("12345678920", "Altınay", "Türkmen", 19, "Kadın", "Türkmenistan", "Teknoloji", 33, 12127)
    calisan2 = calisan.Calisan("98765432121", "Bihter", "Sinler", 19, "Kadın", "Türkiye", "Muhasebe", 55, 18574)
    calisan3 = calisan.Calisan("24681357932", "Rabia", "Elif", 19, "Kadın", "Türkiye", "İnşaat", 77, 15117)

    # Calisan nesnelerini __str__ metodu ile yazdırdık
    print(calisan1)
    print("******************************************")
    print(calisan2)
    print("******************************************")
    print(calisan3)
    print("******************************************")

    # MaviYaka sınıfı için 3 örnek nesne oluşturduk
    maviyaka1 = maviyaka.MaviYaka("12345678930", "Ahmet", "Yılmaz", 30, "Erkek", "Türkiye", "Teknoloji", 27, 12000, 0.2)
    maviyaka2 = maviyaka.MaviYaka("98765432142", "Ayşe", "Demir", 25, "Kadın", "Türkiye", "Muhasebe", 37, 18000, 0.5)
    maviyaka3 = maviyaka.MaviYaka("35795186423", "Ali", "Kara", 35, "Erkek", "Türkiye", "İnşaat", 15, 10000, 0.3)

    # MaviYaka nesnelerini __str__ metodu ile yazdırdık
    print(maviyaka1)
    print("******************************************")
    print(maviyaka2)
    print("******************************************")
    print(maviyaka3)
    print("******************************************")

    # BeyazYaka sınıfı için 3 örnek nesne oluşturduk
    beyazyaka1 = beyazyaka.BeyazYaka("70134910234", "Tugay", "Kavas", 20, "Erkek", "Suriye", "Diğer", 17, 12000, 500)
    beyazyaka2 = beyazyaka.BeyazYaka("61145234626", "Aleyna", "Tok", 25, "Kadın", "Türkiye", "Muhasebe", 57, 18547, 200)
    beyazyaka3 = beyazyaka.BeyazYaka("90412390419", "Emirhan", "Dost", 35, "Erkek", "Türkiye", "İnşaat", 39, 11257, 300)

    # BeyazYaka nesnelerini __str__ metodu ile yazdırdık
    print(beyazyaka1)
    print("******************************************")
    print(beyazyaka2)
    print("******************************************")
    print(beyazyaka3)
    print("******************************************")

    # DataFrame kullanmak için dictionary oluşturmayı tercih ettim
    data = {
        "Çalışan": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka",
                    "Beyaz Yaka", "Beyaz Yaka"],
        "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(),
                  maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(),
                  beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
        "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(),
               maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(),
               beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],
        "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(),
                  maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(),
                  beyazyaka1.get_soyad(), beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
        "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(),
                maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(),
                beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],
        "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(),
                     maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(),
                     beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
        "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(),
                  maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(),
                  beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],
        "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(),
                   maviyaka2.get_sektor(), maviyaka3.get_sektor(), beyazyaka1.get_sektor(), beyazyaka2.get_sektor(),
                   beyazyaka3.get_sektor()],
        "Tecrübe (Yıl)": [calisan1.get_tecrube() / 12, calisan2.get_tecrube() / 12, calisan3.get_tecrube() / 12,
                          maviyaka1.get_tecrube() / 12, maviyaka2.get_tecrube() / 12, maviyaka3.get_tecrube() / 12,
                          beyazyaka1.get_tecrube() / 12, beyazyaka2.get_tecrube() / 12, beyazyaka3.get_tecrube() / 12],
        "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(),
                 maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas(),
                 beyazyaka1.get_maas(), beyazyaka2.get_maas(), beyazyaka3.get_maas()],
        "Yıpranma Payı": [0, 0, 0,
                          maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi(),
                          0, 0, 0],
        "Teşvik Prim": [0, 0, 0,
                        0, 0, 0,
                        beyazyaka1.get_tesvik_primi(), beyazyaka2.get_tesvik_primi(), beyazyaka3.get_tesvik_primi()],
        "Yeni Maaş": [calisan1.get_yeni_maas(), calisan2.get_yeni_maas(), calisan3.get_yeni_maas(),
                      maviyaka1.get_yeni_maas(), maviyaka2.get_yeni_maas(), maviyaka3.get_yeni_maas(),
                      beyazyaka1.get_yeni_maas(), beyazyaka2.get_yeni_maas(), beyazyaka3.get_yeni_maas()]
    }

    df = pd.DataFrame(data)

    # Gruplama yaptık ve ortalamaları hesapladık
    gruplama_tecrube = df.groupby("Çalışan")["Tecrübe (Yıl)"].mean()
    gruplama_yeni_maas = df.groupby("Çalışan")["Yeni Maaş"].mean()

    print("Tecrübe Ortalamaları:")
    print(gruplama_tecrube)

    print("\nYeni Maaş Ortalamaları:")
    print(gruplama_yeni_maas)

    # Maaşı 15.000 TL'nin üstünde olanların sayısını bulduk
    maas_ustunde = df[df["Maaş"] > 15000].shape[0]
    print("\n15.000 TL'nin Üstünde Maaş Alanların Sayısı:", maas_ustunde)

    # Yeni maaşa göre DataFrame'i küçükten büyüğe sıraladık
    sirali_df = df.sort_values(by="Yeni Maaş")
    print("\nSıralanmış DataFrame:")
    print(sirali_df.to_string())

    # Tecrübesi 3 seneden fazla olan Beyaz Yakalıları bulduk
    tecrube_fazla = df[(df["Çalışan"] == "Beyaz Yaka") & (df["Tecrübe (Yıl)"] > 3)]
    print("\nTecrübesi 3 Seneden Fazla Olan Beyaz Yakalılar:")
    print(tecrube_fazla.to_string())

    # Yeni DataFrame oluşturduk
    yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]
    print("\nYeni DataFrame:")
    print(yeni_df)

# Main fonksiyonumuzu çağırarak kodumuzu başlattık


if __name__ == "__main__":

    main()
