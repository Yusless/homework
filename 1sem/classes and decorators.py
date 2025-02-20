import random
def shuffl(func):
    def _wrapper(self):
        res=func(self, self.count)
        random.shuffle(res)
        b=' '.join(res)
        print(b)
    return _wrapper

def add_first(cls):
    def counting(self):
        print(f'This sentance will have {self.count} words.')
    cls.counting = counting
    return cls
@add_first
class sent:
    def __init__(self,count):
        self.count=count
    @shuffl
    def words(self,count):
        if count>9:
            print('too much!')
        else:
            a=[]
            x='The quick brown fox jumps over the lazy dog'
            a =x.split()
            for i in range(9-count):
                a.pop()
        b=' '.join(a)
        print(b)
        return a

fox=sent(4)
dog=sent(8)
fox.counting()
dog.words()
