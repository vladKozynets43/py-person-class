class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        if "wife" in Person.people:
            self.wife = None
        if "husband" in Person.people:
            self.husband = None
        Person.people[name] = self

    @classmethod
    def reset_people(cls) -> None:
        cls.people.clear()


def create_person_list(people_data: list[dict]) -> list[Person]:

    Person.reset_people()

    person_instances = [
        Person(data["name"], data["age"]) for data in people_data
    ]

    for data in people_data:
        current_person = Person.people[data["name"]]
        spouse_role = "wife" if "wife" in data else "husband"
        spouse_name = data.get(spouse_role)

        if spouse_name:
            spouse_instance = Person.people.get(spouse_name)
            setattr(current_person, spouse_role, spouse_instance)

            if spouse_role == "wife":
                spouse_instance.husband = current_person
            elif spouse_role == "husband":
                spouse_instance.wife = current_person

    return person_instances
