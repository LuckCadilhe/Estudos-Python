class Argentina():
    def capital(self):
        print("Buenos Aires é a capital da Argentina.")
    def lingua_oficial(self):
        print("O espanhol é a lingua oficial.")
class Brasil():
    def capital(self):
        print("brasilia é a capital do Brasil.")
    def lingua_oficial(self):
        print("O português é a lingua oficial.")
        
obj_arg = Argentina()
obj_br = Brasil()
for pais in (obj_arg, obj_br):
    pais.capital()
    pais.lingua_oficial()