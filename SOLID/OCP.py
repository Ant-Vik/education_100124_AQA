# Пример с нарушением принципа

class Person:
    def __init__(self, name, age):
        self.nane = name
        self.age = age


class PersonInfo:
    def print_info(self, person):
        return f'Name {person.name}, "Age:" {person.age}'

def test_get_person_data():
    person = Person("hooch", 25)
    pointer = PersonInfo()
    assert pointer.print_info(person) == 'Name hooch, "Age:" 25'



