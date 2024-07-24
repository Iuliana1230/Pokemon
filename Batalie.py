from Antrenor import Antrenor

class Batalie:
    def lupta(self, antrenor1, antrenor2):
        while antrenor1.are_pokemoni_vii() and antrenor2.are_pokemoni_vii():
            pokemon1 = antrenor1.alege_pokemon()
            pokemon2 = antrenor2.alege_pokemon()

            if not pokemon1 or not pokemon2:
                break

            print(f"\n{antrenor1.nume} lupta folosind {pokemon1.nume}!")
            print(f"{antrenor2.nume} lupta folosind {pokemon2.nume}!\n")

            while pokemon1.este_viu() and pokemon2.este_viu():
                pokemon1.ataca(pokemon2)
                if pokemon2.este_viu():
                    pokemon2.ataca(pokemon1)

                print(f'{pokemon1.nume} are {pokemon1.viata} viata ramasa.')
                print(f'{pokemon2.nume} are {pokemon2.viata} viata ramasa.')
        if antrenor1.are_pokemoni_vii():
            print(f'\n{antrenor1.nume} a castigat!')
        else:
            print(f'\n{antrenor2.nume} a castigat!')
