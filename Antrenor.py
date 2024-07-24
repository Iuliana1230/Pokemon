

from pokemon import Pokemon
class Antrenor:
    def __init__(self, nume, pokemoni):
        self.nume = nume
        self.pokemoni = pokemoni

    def alege_pokemon(self):
        pokemoni_vii = [pokemon for pokemon in self.pokemoni if pokemon.este_viu()]
        if not pokemoni_vii:
            print(f'{self.nume} nu mai are pokemoni vii.')
            return None
        print(f'Pokemonii disponibili pentru {self.nume}:')

        for idx, pokemon in enumerate(pokemoni_vii):
            print(f'{idx + 1}. {pokemon.nume} (Viata: {pokemon.viata})')

        while True:
            alegere = input(f'{self.nume}, alege Pokemon-ul pentru lupta (1-{len(pokemoni_vii)}): ')
            try:
                alegere = int(alegere)
                if 1 <= alegere <= len(pokemoni_vii):
                    return pokemoni_vii[alegere - 1]
                else:
                    print(f'Alege un numar între 1 și {len(pokemoni_vii)}.')
            except ValueError:
                print('Introdu un numar valid.')

    def are_pokemoni_vii(self):
        for pokemon in self.pokemoni:
            if pokemon.este_viu():
                return True
        return False
