# Insan class'ından kalıtım yoluyla kullanacağımız Issiz class'ı için
# Öncelikle insan.py dosyasından Insan class'ını import ettik
from insan import Insan


# Insan class'ına kalıtımla bağlı olacak olan Calisan class'ını oluşturduk
class Calisan(Insan):
    # Uygun değişkenler için Initializer metot kullandık
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        # Daha önceden tanımlı değişkenler için super(). metodunu uyguladık
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = None

    # Gerekli set/get fonksiyonları ile değişkenlerimi ulaşılabilir ve kullanılabilir hale getirdik
    def get_yeni_maas(self):
        return self.__yeni_maas

    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas

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
            if tecrube < 0:
                print("Tecrübe ayı negatif olamaz.")
            self.__tecrube = tecrube
        except ValueError:
            print("Lütfen ay değerinden geçerli bir tecrübe giriniz.")

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

    # Zam hakkı fonksiyonu ile çalışanın tecrübesine ve maaşına bağlı olarak belirli bir oranda
    # Zam oranının önerilmesini sağladık
    def zam_hakki(self):
        if self.get_tecrube() < 2:
            self.set_yeni_maas(self.get_maas())
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (self.get_maas() % self.get_tecrube()) / 100)
        elif self.__tecrube > 4 and self.__maas < 25000:
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (self.get_maas() % self.get_tecrube()) / 200)

    # Ekrana yazdırmak için kullanacağımız __str__ fonksiyonunu atadık
    def __str__(self):
        self.zam_hakki()
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrübe: {self.get_tecrube()} ay\n" \
               f"Yeni Maaş: {self.get_yeni_maas()}"
