import numpy as np


def test_exercise_2_part_I(read_population_data):
    population_data = read_population_data("europe_population_large.csv")    
    
    assert isinstance(population_data, list)
    assert all(isinstance(country_data, dict) for country_data in population_data)
    assert len(population_data) == 36

    country_data = population_data[12]
    assert country_data["name"] == "Moldova"
    assert isinstance(country_data["population"], int)
    assert country_data["population"] == 2620000
    assert country_data["female_fraction"] == 0.5239
    assert country_data["male_life_expectancy"] == 67.7
    assert country_data["female_life_expectancy"] == 76.3
    assert country_data["birth_rate"] == 9.8
    assert country_data["death_rate"] == 11.8
    
    country_data = population_data[23]
    assert country_data["name"] == "Latvia"
    assert isinstance(country_data["population"], int)
    assert country_data["population"] == 1900000
    assert country_data["female_fraction"] == 0.5362
    assert country_data["male_life_expectancy"] == 70.9
    assert country_data["female_life_expectancy"] == 80.1
    assert country_data["birth_rate"] == 9.2
    assert country_data["death_rate"] == 15.2


def test_exercise_3_II(battle, Pokemon):
    charmander = Pokemon(name='Charmander', max_health=25, speed=5)
    charmander.level = 6
    squirtle = Pokemon(name='Squirtle', max_health=30, speed=10)
    squirtle.level = 5

    np.random.seed(23)
    winner, loser, rounds = battle(charmander, squirtle)
    assert loser.is_knocked_out()
    assert not winner.is_knocked_out()
    assert winner.name == "Squirtle"
    assert loser.name == "Charmander"
    assert winner.hp == 6
    assert loser.hp == 0
    assert rounds == 15
