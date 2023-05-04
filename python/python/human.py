class Human:
    name= "Halit"
    #built -in
    #constructor
    #initialize
    def __init__(self,name):
        self.name=name
        print("Bir human instance i üretildi yapıcı blok bu ")
    
    def __str__(self):
      return f"STR Fonksiyonundan dönen değer:{self.name}"

    def talk(self,sentence):
        name="Ercan"
        print(f"{self.name}: {sentence}")
      #  print(f"Human: {sentence}")

    def walk(self):
        print(f"{self.name}  is walking..")