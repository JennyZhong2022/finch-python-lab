from django.db import models
from django.urls import reverse

MEALS=(
    ('B','Breakfast'),
    ('L','Lunch'),
    ('D','Dinner') 
)

# Create your models here.
class Finch(models.Model):
  name=models.CharField(max_length=100)
  breed=models.CharField(max_length=100)
  description=models.TextField(max_length=250)
  age=models.IntegerField()

  def __str_(self):
    return f'{self.name}: {self.id}'

  def get_absolute_url(self):
    return reverse('detail',kwargs={'finch_id':self.id})  

class Feeding(models.Model):    
  date=models.DateField('feeding date')
  meal=models.CharField(
    max_length=1,
    # add the 'choices' field option
       choices=MEALS,
    # set the default value for meal to be 'B'
       default=MEALS[0][0]
    )

# Since a Feeding belongs to a Cat, it must hold the id of the cat object it belongs to — yep, it needs a foreign key!
# the ForeignKey field-type is used to create a one-to-many relationship.

# In a one-to-many relationship, the on_delete=models.CASCADE is required. It ensures that if a Cat record is deleted, all of the child Feedings will be deleted automatically as well - thus avoiding orphan records
  finch=models.ForeignKey(Finch, on_delete=models.CASCADE)  

  def __str_(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f'{self.get_meal_display()} on {self.date}'  

   # change the default sort
  class Meta:
    ordering = ['-date']