from insan import insan

class Issiz(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, beyaz_tecrube, mavi_tecrube, yonetici_tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statuler = {"beyaz yaka": beyaz_tecrube, "mavi yaka": mavi_tecrube, "yönetici": yonetici_tecrube}
        self.__statu = None
    def set_statuler(self, deger1, deger2, deger3):
        self.__statuler = {"beyaz yaka": deger1, "mavi yaka": deger2, "yönetici": deger3}

    def get_statuler(self):
        return self.__statuler

    def set_statu(self, statu):
        self.__statu = statu

    def get_statu(self):
        return self.__statu

    def statu_bul(self):
        mavi_yaka = (self.__statuler["mavi yaka"] * 0.20)
        beyaz_yaka = (self.__statuler["beyaz yaka"] * 0.35)
        yonetici = (self.__statuler["yönetici"] * 0.45)
        if mavi_yaka > beyaz_yaka:
            if mavi_yaka > yonetici:
                self.set_statu("mavi yaka")
            else:
                self.set_statu("yönetici")
        else:
            if beyaz_yaka > yonetici:
                self.set_statu("beyaz yaka")
            else:
                self.set_statu("yönetici")


    def __str__(self):
        self.statu_bul()
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Önerilen Statü: {self.get_statu()}"

