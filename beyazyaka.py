from calisan import Calisan


class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        try:
            tesvik_primi = float(tesvik_primi)
        except ValueError:
            print("Lütfen geçerli bir teşvik primi değeri giriniz.")
            return

        if tesvik_primi < 0:
            print("Teşvik primi değeri negatif olamaz.")
            return

        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        if self.get_tecrube() < 2:
            return self.__tesvik_primi
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            return (self.get_maas() % self.get_tecrube()) * 5 + self.__tesvik_primi
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            return (self.get_maas() % self.get_tecrube()) * 4 + self.__tesvik_primi
        else:
            return 0

    def __str__(self):
        yeni_maas = self.get_maas() + self.zam_hakki()
        if yeni_maas == self.__maas:
            yeni_maas = self.__maas
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrübe: {self.get_tecrube()} ay\n" \
               f"Yeni Maaş: {yeni_maas}"
