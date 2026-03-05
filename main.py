from dataclasses import dataclass

@dataclass
class Kitob:
    nomi: str
    muallif: str
    sahifa_soni: int
    narx: int

    def chegirma(self):
        self.narx = self.narx * 0.9
        print(f'10% chegirma bilan'
              f'narx: {self.narx}')
