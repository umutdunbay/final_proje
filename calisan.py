from insan import insan


class Calisan(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        if sektor in ["teknoloji", "muhasebe", "inşaat", "diğer"]:
            self.__sektor = sektor
        else:
            print("Lütfen geçerli bir sektör giriniz.")

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        try:
            tecrube = int(tecrube)
        except ValueError:
            print("Lütfen ay değerinden geçerli bir tecrübe giriniz.")
            return

        if tecrube < 0:
            print("Tecrübe ayı negatif olamaz.")
            return

        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        try:
            maas = float(maas)
        except ValueError:
            print("Geçerli bir maaş değeri giriniz.")
            return

        if maas < 0:
            print("Maaş negatif olamaz.")
            return

        self.__maas = maas

    def zam_hakki(self):
        if self.__tecrube < 2:
            return 0
        elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
            return self.__maas % self.__tecrube
        elif self.__tecrube > 4 and self.__maas < 25000:
            return (self.__maas % self.__tecrube) / 2
        else:
            return 0

    def __str__(self):
        yeni_maas = self.__maas + (self.__maas * self.zam_hakki()) / 100
        if yeni_maas == self.__maas:
            yeni_maas = self.__maas
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrübe: {self.__tecrube} yıl\n" \
               f"Yeni Maaş: {yeni_maas}"
