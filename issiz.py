from insan import insan

class Issiz(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statuler = {"beyaz yaka": 0, "mavi yaka": 0, "yönetici": 0}
        self.__statu = ""

    def set_statuler(self, deger1, deger2, deger3):
        self.__statuler = {"beyaz yaka": deger1, "mavi yaka": deger2, "yönetici": deger3}

    def get_statuler(self):
        return self.__statuler

    def set_statu(self, statu):
        self.__statu = statu

    def get_statu(self):
        return self.__statu


    def statu_bul(self,):
        mavi_yaka = (self.__statuler["mavi yaka"] * 0.20)
        beyaz_yaka = (self.__statuler["beyaz yaka"] * 0.35)
        yonetici = (self.__statuler["yönetici"] * 0.45)
        self.__statuler = {"beyaz yaka": beyaz_yaka, "mavi yaka": mavi_yaka, "yönetici": yonetici}
        self.__statu = max(self.__statuler, key=self.__statuler.get)


    def __str__(self,):
        self.statu_bul()
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Önerilen Statü: {self.get_statu()}"

