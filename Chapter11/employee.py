class Employee:
    '''A simple attempt to model a employee.'''

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        '''Raises the employee annual salary.'''
        self.salary += salary_raise