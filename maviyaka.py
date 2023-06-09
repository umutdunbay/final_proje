# Calisan class'ından kalıtım yoluyla kullanacağımız MaviYaka class'ı için
# Öncelikle calisan.py dosyasından Calisan class'ını import ettik
from calisan import Calisan


# Calisan class'ına kalıtımla bağlı olacak olan MaviYaka class'ını oluşturduk
class MaviYaka(Calisan):
    # Uygun değişkenler için Initializer metot kullandık
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        # Daha önceden tanımlı değişkenler için super(). metodunu uyguladık
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    # set/get komutlarını kullandığımız fonksiyonları oluşturduk
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        try:
            yipranma_payi = float(yipranma_payi)
            if yipranma_payi < 0:
                print("Yıpranma payı negatif olamaz.")
            self.__yipranma_payi = yipranma_payi

        except ValueError:
            print("Geçerli bir yıpranma payı değeri giriniz.")

    # Zam hakkı fonksiyonu ile çalışanın tecrübesine ve maaşına bağlı olarak belirli bir oranda
    # Zam oranının önerilmesini sağladık
    def zam_hakki(self):
        if self.get_tecrube() < 2:
            self.set_yeni_maas(self.get_maas() + self.get_maas() * self.get_yipranma_payi() / 10)
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (self.get_maas() % self.get_tecrube() / 2 +
                                                                    self.get_yipranma_payi() / 10))
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (self.get_maas() % self.get_tecrube() / 3 +
                                                                    self.get_yipranma_payi() / 10))

    # Ekrana yazdırma işlemlerinin gerçekleşceği __str__ fonksiyonunu oluşturduk
    def __str__(self):
        self.zam_hakki()
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrübe: {self.get_tecrube()} ay\n" \
               f"Yeni Maaş: {self.get_yeni_maas()}"
