from calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

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

    def zam_hakki(self):
        if self.get_tecrube() < 2:
            self.set_yeni_maas(self.get_maas() + self.get_maas() * self.get_yipranma_payi() /10)
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            self.set_yeni_maas(self.get_maas() +  self.get_maas() * (self.get_maas() % self.get_tecrube() / 2 + self.get_yipranma_payi() / 10))
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (self.get_maas() % self.get_tecrube() / 3 + self.get_yipranma_payi() / 10))
    def __str__(self):
        self.zam_hakki()
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrübe: {self.get_tecrube()} ay\n" \
               f"Yeni Maaş: {self.get_yeni_maas()}"
