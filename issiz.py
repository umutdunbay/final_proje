from insan import insan

class Issiz(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statuler = {"beyaz yaka": 0, "mavi yaka": 0, "yönetici": 0}
        self.set_statu(tecrube)

    def get_statuler(self):
        return self.__statuler

    def set_statu(self, tecrube):
        self.__tecrube = tecrube



    def statu_bul(self,):
        mt = self.__statuler["mavi yaka"] * 0.20
        bt = self.__statuler["beyaz yaka"] * 0.35
        yt = self.__statuler["yönetici"] * 0.45
        if mt > bt:
            if mt > yt:
                self.__tecrube = mt
                print("En uygun statü mavi yakadır.")
            else:
                self.__tecrube = yt
                print("En uygun statü yöneticidir.")
        else:
            if bt > yt:
                self.__tecrube = bt
                print("En uygun statü beyaz yakadır.")
            else:
                self.__tecrube = yt
                print("En uygun statü yöneticidir")

    def __str__(self,):
        return f"Ad: {self.get_ad()}\n" \
               f"Soyad: {self.get_soyad()}\n" \
               f"Önerilen Statü: {self.__tecrube}"
