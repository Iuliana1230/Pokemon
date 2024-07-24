from pokemon import Pokemon
from Antrenor import Antrenor
from Batalie import Batalie

def main():
    # Definim pokemoni pentru antrenor1
    charizard = Pokemon('Charizard', 'Foc', 100, 20)
    squirtle = Pokemon('Squirtle', 'Apa', 100, 15)
    sandshrew = Pokemon('Sandshrew', 'Pamant', 100, 10)

    # Definim pokemoni pentru antrenor2
    charmander = Pokemon('Charmander', 'Foc', 100, 25)
    bulbasaur = Pokemon('Bulbasaur', 'Apa', 100, 18)
    geodude = Pokemon('Geodude', 'Pamant', 100, 12)

    # Creăm antrenorii
    antrenor1 = Antrenor('Iuli', [charizard, squirtle, sandshrew])
    antrenor2 = Antrenor('Momo', [charmander, bulbasaur, geodude])

    # Pornim lupta
    batalie = Batalie()
    batalie.lupta(antrenor1, antrenor2)

    # Afișăm rezultatul final
    print("\nStarea finală a Pokemonilor:")
    for pokemon in antrenor1.pokemoni:
        print(f'{pokemon.nume} - {pokemon.viata} viață rămasă')
    for pokemon in antrenor2.pokemoni:
        print(f'{pokemon.nume} - {pokemon.viata} viață rămasă')

if __name__ == "__main__":
    main()
