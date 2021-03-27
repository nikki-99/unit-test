


class Student:

   

    def __init__(self, first, last):
        self.first = first
        self.last = last
        

    @property
    def gmail(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)    

    @property
    def name(self):
        return '{} {}'.format(self.first, self.last)     
    

   
