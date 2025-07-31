class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    result = []
    for person in people:
        person_object = Person(name=person["name"], age=person["age"])
        result.append(person_object)
    for i, person in enumerate(people):
        if person.get("husband", False):
            result[i].husband = Person.people[person.get("husband")]
        elif person.get("wife", False):
            result[i].wife = Person.people[person.get("wife")]
    return result


# people = [{"name": "Ross", "age": 30, "wife": "Rachel"},
#           {"name": "Joey", "age": 29, "wife": None},
#           {"name": "Rachel", "age": 28, "husband": "Ross"}]

# print(create_person_list(people))
