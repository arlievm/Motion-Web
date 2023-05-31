from django.db import models

class Services(models.Model):
    
    class Meta:
        db_table = 'services'
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        
    sourcing = models.CharField(verbose_name='аутсорсинг', max_length=36)
    design_one = models.CharField(verbose_name='Разработка дизайна', max_length=36)
    mobileappl_one = models.CharField(verbose_name='Разработка мобильных приложений', max_length=50)
    design_two = models.CharField(verbose_name='Разработка дизайна', max_length=36)
    design_three = models.CharField(verbose_name='Разработка дизайна', max_length=36)
    mobileappl_two = models.CharField(verbose_name='Разработка мобильных приложений', max_length=50)

    def __str__(self):
        return self.design_one
    
    
class Customer(models.Model):
    
    class Meta:
        verbose_name = "Наши клиенты"
        verbose_name_plural = "Наши клиенты"
        db_table = 'customers'
            
    photo = models.ImageField(verbose_name='Фотография', upload_to ='image/client')
    title_ru = models.TextField(verbose_name='Описание', blank=True, null=True)
    title_en = models.TextField(verbose_name='Description')
        

    def __str__(self):
        return self.title_en
                

class Proect(models.Model):
     
    class Meta:
        db_table = 'Our Projects'
        verbose_name = 'Наши проекты'
        verbose_name_plural = 'Наши проекты'
            
    photo = models.ImageField(verbose_name='Фотография', upload_to ='image/client')
    title_ru_pro = models.TextField(verbose_name='Описание', blank=True, null=True)
    url = models.URLField(verbose_name='Ссылка', blank=True, null=True)
        
    def __str__(self):
        return self.title_ru_pro
    
class Team(models.Model):
    
    class Meta:
        
        db_table = 'Our team'
        verbose_name = 'Наша комадна'
        verbose_name_plural ='Наша комадна'
        
    photo = models.ImageField(verbose_name='Фотография', upload_to ='image/client')
    title_ru_name = models.TextField(verbose_name='Описание имена', blank=True, null=True)
    designer = models.CharField(verbose_name='Дизайнер',max_length=32)
    whatsapp = models.URLField(verbose_name="Whatsapp", blank=True, null=True);
    instagram = models.URLField(verbose_name="Instagram", blank=True, null=True);
    linkedin = models.URLField(verbose_name="Linkedin", blank=True, null=True);
    
    def __str__(self):
        return self.linkedin
    
    
class Instruments(models.Model):
    
    class Meta:
        db_table = 'technologies_and_tools'
        verbose_name = 'Технологии и Инструменты'
        verbose_name_plural = 'Технологии и Инструменты'

    title_ru_tehnol = models.TextField(verbose_name='Описание Технологии и Инструменты ', blank=True, null=True)
    parent_instrument = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=255)

        
    def __str__(self):
        return self.name
    
    
class TechnologiesCategory(models.Model):
    
    class Meta:
        db_table = 'technologies_category'
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
    
    title = models.CharField(verbose_name="название категории", max_length=32)
    
    def __str__(self):
        return self.title
    
    
class Technologies(models.Model):
    
    class Meta:
        db_table = 'technologies'
        verbose_name = 'Технологии и Инструменты'
        verbose_name_plural = 'Технологии и Инструменты'
        
    category = models.ForeignKey(TechnologiesCategory, on_delete=models.CASCADE) 
    image = models.ImageField(verbose_name=" фотографии", upload_to="images/icon")
    name = models.CharField(verbose_name='название', max_length=32)
    
    def __str__(self):
        return self.name
        
        
class Feedback(models.Model):
    
    class Meta:
        db_table = 'Feedback'
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"
    
    name_one = models.CharField(verbose_name="Имя", max_length=36,blank=True,null=True)
    iphone = models.CharField("Номер телефона", max_length=50, blank=True,null=True)    
    email = models.EmailField(verbose_name="Почта", max_length=50, blank=True,null=True)

    def __str__(self):
        return self.email
