from abc import ABC, abstractmethod
# bir txt dosyasındaki verileri başka bir txt dosyasına yazma/taşıma.

class EmptyFile(Exception):
    '''Okunan dosya boşluk içeriyorsa fırlatılır.'''
    pass

class FileCarry(ABC):
    def __init__(self, input_path, output_path):
        """
        __init__:
        input_path: okunacak dosyanın adresi
        output_path: dosyaların yazılacak adresi
        """
        self._output_path = output_path
        self._input_path = input_path

    @abstractmethod
    def carry(self):
        """
        Soyut metot, miras alınan sınıfların 
        dosyaları okuma/yazma işlemlerini gerçekleştirmesini sağlar.
        """
        pass

    def read(self):
        try:
            with open(self._input_path, 'r') as file:
                raw = file.read()
                if not raw.strip():
                    raise EmptyFile
                else:
                    return raw
        except FileNotFoundError:
            print("dosya bulunamadı")
        except EmptyFile:
            print("dosya boş")
        

    def write(self, raw):
        with open(self._output_path, 'w') as file:
            file.write(raw)


class TXTtoTXTcarry(FileCarry):
    def __init__(self, input_path, output_path):
        super().__init__(input_path, output_path)

    def carry(self):
        raw = self.read()
        self.write(raw)
        print("dosya taşındı")

carry = TXTtoTXTcarry("txt_dosya.txt", "carried.txt")
carry.carry()

        






    