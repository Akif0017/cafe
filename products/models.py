from django.db import models 


class CoffeesModel(models.Model):
    coffee_name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='coffees/')
    price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = 'Coffee'
        verbose_name_plural = 'Coffees'
    
    def __str__(self):
        return self.coffee_name
    


class CroissantsModel(models.Model):
    croissant_name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='croissants/')
    price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = 'Croissant'
        verbose_name_plural = 'Croissants'

    def __str__(self):
        return self.croissant_name
    

class OurMenuModel(models.Model):
    our_menu_name = models.CharField(max_length=256)
    coffe = models.OneToOneField(CoffeesModel, on_delete=models.CASCADE)
    croissant = models.OneToOneField(CroissantsModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Our menu'
        verbose_name_plural = 'Ours menus'

    def __str__(self):
        return self.our_menu_name
    
