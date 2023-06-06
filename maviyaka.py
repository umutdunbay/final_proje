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
        except ValueError:
            print("Geçerli bir yıpranma payı değeri giriniz.")
            return

        if yipranma_payi < 0:
            print("Yıpranma payı negatif olamaz.")
            return

        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        if self.get_tecrube() < 2:
            return self.__yipranma_payi * 10
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            return (self.get_maas() % self.get_tecrube() / 2) + (self.__yipranma_payi * 10)
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            return (self.get_maas() % self.get_tecrube() / 3) + (self.__yipranma_payi * 10)
        else:
            return 0

    def __str__(self):
        yeni_maas = self.get_maas() + (self.get_maas() * self.zam_hakki()) / 100
        if yeni_maas == self.__maas:
            yeni_maas = self.__maas
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrübe: {self.get_tecrube()} ay\n" \
               f"Yeni Maaş: {yeni_maas}"
