from random import choice

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Hello world, ' + self.name + '!'

def main():
    people = [Person('Jane'), Person('Jill'), Person('Bob')]
    person = choice(people)

    print(person)

if __name__ == '__main__':
    main()