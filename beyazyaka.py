# Calisan class'ından kalıtım yoluyla kullanacağımız BeyazYaka class'ı için
# Öncelikle calisan.py dosyasından Calisan class'ını import ettik
from calisan import Calisan


# Calisan class'ına kalıtımla bağlı olacak olan BeyazYaka class'ını oluşturduk
class BeyazYaka(Calisan):
    # Uygun değişkenler için Initializer metot kullandık
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        # Zaten halihazırda Insan class'ında tanımlı değişkenler için super(). metodunu uyguladık
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    # Gerekli set/get fonksiyonları ile değişkenlerimi ulaşılabilir ve kullanılabilir hale getirdik
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

    # Zam hakkı fonksiyonu ile çalışanın tecrübesine ve maaşına bağlı olarak belirli bir oranda
    # MaviYaka'lardan farklı olarak direkt bir zam miktarı önerilmesini sağladık.
    def zam_hakki(self):
        if self.get_tecrube() < 2:
            self.set_yeni_maas(self.get_maas() + self.get_tesvik_primi())
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            self.set_yeni_maas(self.get_maas() + ((self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()))
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            self.set_yeni_maas((self.get_maas() + (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()))

    # Ekrana yazdırmak için kullanacağımız __str__ fonksiyonunu atadık
    def __str__(self):
        self.zam_hakki()
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Tecrübe: {self.get_tecrube()} ay\n" \
               f"Yeni Maaş: {self.get_yeni_maas()}"
