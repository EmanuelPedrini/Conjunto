import random

def generate_a_random_name():
    silabasnomeprincipal = ["ki", "me", "ra", "ar", "em", "ik"]
    nome = []
    for i in range(random.randint(2, 3)):
        nome.append(random.choice(silabasnomeprincipal))

    nomefinal = ("".join(nome).capitalize())

    return (nomefinal)

def generate_a_random_second_name():
    listadesobrenomes=["Bafemoth", "Teeths", "Intestines", "Smash"]
    sobrenome = random.choice(listadesobrenomes)
    return sobrenome

def generate_a_random_surname():
    listadeapelidos=['"Blow"','"Small Head"', '"Hammer Head"', '"Nail"', '"Hand Finger"']
    surn=random.choice(listadeapelidos)
    return surn
def generate_a_full_name():
    fullname = (f"{generate_a_random_name()} {generate_a_random_surname()} {generate_a_random_second_name()}")
    return fullname

print(generate_a_full_name())