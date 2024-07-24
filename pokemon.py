
class Pokemon:
    TIPURI = ['Foc', 'Apa', 'Pamant']

    def __init__(self, nume, tip, viata, putere_atac):
        if tip not in Pokemon.TIPURI:
            raise ValueError(f"Tipul {tip} nu este suportat. Folositi unul din: {Pokemon.TIPURI}")
        self.nume = nume
        self.tip = tip
        self.viata = viata
        self.putere_atac = putere_atac

    def ataca(self, alt_pokemon):
        if self.este_viu():
            print(f'{self.nume} atacă pe {alt_pokemon.nume} cu {self.putere_atac} putere de atac.')
            alt_pokemon.viata -= self.putere_atac
            if alt_pokemon.viata < 0:
                alt_pokemon.viata = 0
        else:
            print(f'{self.nume} nu mai are viață și nu poate ataca.')

    def este_viu(self):
        return self.viata > 0
