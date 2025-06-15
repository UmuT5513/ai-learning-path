#soyut sınıf: temel özelliklerin tanımlandığı ve dğer sınıflarca miras alınarak somut 
#sınıfların kurulduğu bir şablondur. Soyut sınıflardan nesne üretilmez. Soyut metodları vardır. 
#Somut sınıflar bu metdoları uygulamak zorundadır.

from abc import ABC, abstractmethod


class Media(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Video(Media):
    def play(self):
        print("video oynatılıyor...")

    def stop(self):
        print("video durduruldu...")

class Audio(Media):
    def play(self):
        print("audio oynatılıyor...")

    def stop(self):
        print("audio durduruldu...")


video = Video()
audio = Audio()

audio.play()
video.play()
audio.stop()
video.stop()