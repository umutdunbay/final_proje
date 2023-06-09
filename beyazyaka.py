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

            if tesvik_primi < 0:
                print("Teşvik primi değeri negatif olamaz.")
                return

            self.__tesvik_primi = tesvik_primi
        except ValueError:
            print("Lütfen geçerli bir teşvik primi değeri giriniz.")
            return

    def zam_hakki(self):
        if self.get_tecrube() < 2:
            self.set_yeni_maas(self.get_maas() + self.get_tesvik_primi())
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            self.set_yeni_maas(self.get_maas() + ((self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()))
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            self.set_yeni_maas((self.get_maas() + (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()))

    def __str__(self):
        self.zam_hakki()
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrübe: {self.get_tecrube()} ay\n" \
               f"Yeni Maaş: {self.get_yeni_maas()}"
