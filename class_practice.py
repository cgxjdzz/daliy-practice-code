import numpy


class Student(object):
    '''
    a class contain name, age and score of a student, with methods for inquiry
    '''
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def get_name(self) -> str:
        print(self.name)

    def get_age(self) -> int:
        print(self.age)

    def get_course(self) -> int:
        print(max(self.score))


def student_test():
    zm = Student('zhangming',20,[69,88,100])
    zm.get_age()
    zm.get_name()
    zm.get_course()


class DictClass(object):
    '''
    a class save and edit dictionary
    '''
    def __init__(self,dict):
        self.dict=dict

    def del_dict(self,key):
        del self.dict[key]

    def get_dict(self,key):
        return 'not found' if not key in self.dict else self.dict[key]

    def get_key(self):
        return list(self.dict.keys())

    def update_dict(self,new_dict):
        self.dict={k:v for d in [self.dict,new_dict] for k,v in d.items()}
        return list(self.dict.values())


def dict_test():
    dict=DictClass({'timian':'1','butimian':'2'})
    print(dict.get_key(),
          dict.get_dict('timian'),
          dict.del_dict('timian'),
          dict.get_dict('timian'),
          dict.update_dict({'feichangtimian':'3'}),
          dict.dict)


class ListInfo(object):
    '''
    a class to save and edit a list
    '''
    def __init__(self,list):
        self.list=list

    def add_key(self,element):
        self.list.append(element)

    def get_key(self,number):
        return self.list[number]

    def update_list(self,new_list):
        self.list=self.list+new_list

    def del_key(self):
        ret=self.list[-1]
        del self.list[-1]
        return ret


def list_test():
    list=ListInfo([1,2,3])
    print(list.add_key(4),
          list.get_key(-1),
          list.update_list([5,6]),
          list.del_key())

if __name__ == '__main__':
    student_test()
    dict_test()
    list_test()