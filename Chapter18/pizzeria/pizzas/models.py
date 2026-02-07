from django.db import models

class Pizza(models.Model):
    '''A pizza.'''
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''Return the pizza name.'''
        return self.name
    
class Topping(models.Model):
    '''Pizza toppings.'''
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.name) > 50:
            return f'{self.name[:50]}...'
        return self.name