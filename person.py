class Person:
    """
   Beschreibt eine "allgemeine" Person mit
   - Name
   - Alter
   - Adresse

   Die Attribute sind über setter/getter zugreifbar.
   Für die Ausgabe am Stdout wird die Methode print() verwendet.
   """

    def __init__(self, name, age):
        '''
      Initialisiert das Objekt
      :param name: Name der Person
      :param alter: Alter der Person
      '''
        self._name = name
        self._age = age
        self._address = ''

    @property
    def name(self):
        '''
      Liefert den Namen der Person
      :return: Name der Person
      '''
        return self._name

    @property
    def age(self):
        '''
      Liefert das Alter der Person
      :return: Alter der Person
      '''
        return self._age

    @property
    def address(self):
        '''
      Liefert die Adresse der Person
      :return: Adresse der Person
      '''
        return self._address

    @address.setter
    def address(self, address):
        '''
      Setzt die Adresse der Person
      :param address: Adresse der Person
      '''
        self._address = address

    def print(self):
        '''
      Gibt alle Attribute der Person am Bildschirm aus
      '''
        print(f'Person: {self._name}\n\tAlter :   {self.age}\n\tAdresse : {self.address}')


# nur für Test
if __name__ == '__main__':
    p = Person('Max', 2000)
    p.address = 'Musterdorf'
    p.print()