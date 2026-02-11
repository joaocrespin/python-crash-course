from django.db import models

class Blog(models.Model):
    '''Represents an individual blog.'''
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''String representation of a blog.'''
        return self.name
    
class BlogPost(models.Model):
    '''A post from a specific blog.'''
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'
    
    def __str__(self):
        if len(self.text) > 100:
            return f'{self.text[:100]}...'
        return self.text
