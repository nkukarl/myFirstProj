from random import choice

class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Hello world, ' + self.name + '!'

def main():
    people = [Person('Jane'), Person('Jill'), Person('Bob')]
    random_person = choice(people)
    print(random_person)

if __name__ == '__main__':
    main()