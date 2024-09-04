# class Personal:
#     def __init__(self, ismi, yoshi, manzili):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.manzili = manzili
#
#     def yoshini_oshir(self):
#         self.yoshi += 1
#
#     def manzilini_ozgartir(self, manzil):
#         self.manzili = manzil
#
#     def malumotni_chop_et(self):
#         print(f"ismi: {self.ismi}, yoshi: {self.yoshi}, manzili: {self.manzili}")
#
#
# class Xodim(Personal):
#     def __init__(self, ismi, yoshi, manzili, maoshi, bolimi, ishga_kirgan_sanasi):
#         super().__init__(ismi, yoshi, manzili)
#         self.maoshi = maoshi
#         self.bolimi = bolimi
#         self.ishga_kirgan_sanasi = ishga_kirgan_sanasi
#
#     def ish_yili(self):
#         return f"Ishga {self.ishga_kirgan_sanasi}-sanada kirgan"
#
#     def maoshini_oshirish(self, oshir):
#         self.maoshi = self.maoshi * oshir / 100 + self.maoshi
#         return self.maoshi
#
#     def bolimini_ozgartir(self, yangi_bolim):
#         self.bolimi = yangi_bolim
#
#     def malumotlarni_chop_et(self):
#         print(f"Maosh oshirildi: {self.maoshi}\nBo'lim o'zgartirildi: {self.bolimi}")
#
#
# class Manager(Xodim):
#     def __init__(self,ismi, yoshi, manzili, maoshi, bolimi, ishga_kirgan_sanasi, jamoasi):
#         super().__init__(ismi, yoshi, manzili, maoshi, bolimi, ishga_kirgan_sanasi)
#         self.jamoasi = []
#
#     def xodim_qosh(self, xodim):
#         self.jamoasi.append(xodim)
#
#     def jamo_malomotlari(self):
#         print("Jamoda quyidagi xodimlar bor:")
#         for xodim in self.jamoasi:
#             xodim.malumotni_chop_et()
#
# xodim1 = Xodim("Ziyovuddin", 14, "Kirguli", 1000, "Developers", "13/08/2024")
#
# manager = Manager("Sardor", 35, "Toshkent", 2000, "IT", "01/01/2020")
#
# manager.xodim_qosh(xodim1)
# manager.jamo_malomotlari()
# xodim1.malumotlarni_chop_et()

"""Inkapsulyatsyaga aloqador masala"""

# class Student:
#     def __init__(self, ismi, yoshi, id_card):
#         self.__ismi = ismi
#         self.__yoshi = yoshi
#         self.__id_card = id_card
#
#     def get_ismi(self):
#         return self.__ismi
#
#     def set_ismi(self, ismi):
#         if isinstance(ismi, int):
#             print("Xato malumot turi kiritding")
#             return
#         self.__ismi = ismi
#
#
#     def get_yoshi(self):
#         return self.__yoshi
#
#     def set_yoshi(self, yoshi):
#         self.__yoshi = yoshi
#
#
#     def get_id(self):
#         return self.__id_card
#
# student = Student("Sohibjon", 19, "AB5801213")
#
# student.set_ismi(546465)
# print(student.get_ismi())


"""Property bilan"""


# class Student:
#     def __init__(self, ismi, yoshi, id_card):
#         self.__ismi = ismi
#         self.__yoshi = yoshi
#         self.__id_card = id_card
#
#     @property
#     def ismi(self):
#         return self.__ismi
#
#     @ismi.setter
#     def ismi(self, ismi):
#         if not isinstance(ismi, str):
#             print("Xato malumot turi kiritding")
#             return
#         self.__ismi = ismi
#
#     @property
#     def yoshi(self):
#         if self.__yoshi < 18:
#             return "Yoshi 18 dan kichik"
#         return self.__yoshi
#
#     @yoshi.setter
#     def yoshi(self, yoshi):
#         self.__yoshi = yoshi
#
#
#     def get_id(self):
#         return self.__id_card
#
# student = Student("Sohibjon", 19, "AB5801213")
#
# student.ismi = 167251726
# print(student.ismi)
# print(student.yoshi)


"""Masala"""


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self._age  = age
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self):
#         if age > 0:
#             self._age = age
#         else:
#             print("xato kiritilgan")
#
#     def yoshni_oshirish(self):
#         self._age += 1
#
#     def malumotlarni_chop_et(self):
#         print(f"Ismi: {self.__name}, Yoshi: {self._age}")
#
#
# class Student(Person):
#     def __init__(self, name, age, student_id, gpa):
#         super().__init__(name, age)
#         self.__id = student_id
#         self._gpa = gpa
#
#     def get_id(self):
#         return self.__id
#
#     def get_gpa(self):
#         return self._gpa
#
#     def set_gpa(self, gpa):
#          self._gpa = gpa
#
#     def gpa_oshirish(self, value):
#         self._gpa += value
#
#     def malumotlarni_chiqar(self):
#         super().malumotlarni_chiqar()
#         print(f"ID: {self.__id}, GPA: {self._gpa}")
#
#
# person = Person("Ziyovuddin", 14)
# person.malumotlarni_chop_et()
