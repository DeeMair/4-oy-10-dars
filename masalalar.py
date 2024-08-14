class Personal:
    def __init__(self, ismi, yoshi, manzili):
        self.ismi = ismi
        self.yoshi = yoshi
        self.manzili = manzili

    def yoshini_oshir(self):
        self.yoshi += 1

    def manzilini_ozgartir(self, manzil):
        self.manzili = manzil

    def malumotni_chop_et(self):
        print(f"ismi: {self.ismi}, yoshi: {self.yoshi}, manzili: {self.manzili}")


class Xodim(Personal):
    def __init__(self, ismi, yoshi, manzili, maoshi, bolimi, ishga_kirgan_sanasi):
        super().__init__(ismi, yoshi, manzili)
        self.maoshi = maoshi
        self.bolimi = bolimi
        self.ishga_kirgan_sanasi = ishga_kirgan_sanasi

    def ish_yili(self):
        return f"Ishga {self.ishga_kirgan_sanasi}-sanada kirgan"

    def maoshini_oshirish(self, oshir):
        self.maoshi = self.maoshi * oshir / 100 + self.maoshi
        return self.maoshi

    def bolimini_ozgartir(self, yangi_bolim):
        self.bolimi = yangi_bolim

    def malumotlarni_chop_et(self):
        print(f"Maosh oshirildi: {self.maoshi}\nBo'lim o'zgartirildi: {self.bolimi}")


class Manager(Xodim):
    def __init__(self,ismi, yoshi, manzili, maoshi, bolimi, ishga_kirgan_sanasi, jamoasi):
        super().__init__(ismi, yoshi, manzili, maoshi, bolimi, ishga_kirgan_sanasi)
        self.jamoasi = []

    def xodim_qosh(self, xodim):
        self.jamoasi.append(xodim)

    def jamo_malomotlari(self):
        print("Jamoda quyidagi xodimlar bor:")
        for xodim in self.jamoasi:
            xodim.malumotni_chop_et()

xodim1 = Xodim("Ziyovuddin", 14, "Kirguli", 1000, "Developers", "13/08/2024")

manager = Manager("Sardor", 35, "Toshkent", 2000, "IT", "01/01/2020")

manager.xodim_qosh(xodim1)
manager.jamo_malomotlari()
xodim1.malumotlarni_chop_et()