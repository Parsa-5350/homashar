from django.db import models



# تاریخچه 
class History(models.Model):

    headline = models.CharField(max_length= 20) # سر تیتر 
    text = models.TextField() # متن 

    def __str__(self):
        return self.headline
    
    
# اخبار 
class News(models.Model):
    
    headline = models.CharField(max_length=40) # تیتر خبر 
    title = models.CharField(max_length=40) # عنوان خبر 
    summary = models.TextField() # خلاصه خبر 
    display = models.TextField() # نمایش 
    date = models.CharField() # تاریخ 
    time = models.TimeField() # ساعت 
    image = models.ImageField(upload_to='news/images', blank=True, null=True)  # عکس 
    text = models.TextField() # تشریح خبر 

    def __str__(self):
        return self.headline
    
    
#پروژه ها 
class Project(models.Model):
    
    headline = models.CharField(max_length=20) # نام پروژه 
    date = models.CharField(max_length=20) # تاریخ پروژه 
    image = models.ImageField(upload_to='project/images', blank=True, null=True) # عکس پروژه 
    text = models.TextField() # توضیحات 

    def __str__(self):
        return self.headline


# شوراها 
class Councils(models.Model):
    
    headline = models.CharField(max_length=20) # نام و نام خانوادگی 
    date = models.CharField(max_length=20) # ساال خدمت 
    image = models.ImageField(upload_to='councils/images',  blank=True, null=True) # عکس شورا 
    text = models.TextField() # متن 

    def __str__(self):
        return self.headline
    

#شهردار 
class Mayor(models.Model):
    
    headline = models.CharField(max_length=20) # نام و نام خانوادگی 
    date = models.CharField(max_length=20) # سال خدمت 
    image = models.ImageField(upload_to='project/images',  blank=True, null=True) # عکس شهردار 
    text = models.TextField() # متن 

    def __str__(self):
        return self.headline
    

#مشاهیر 
class Celebrities(models.Model):

    headline = models.CharField(max_length=20) # عنوان 
    image = models.ImageField(upload_to='celebrities/images/', blank=True, null=True) # عکس 
    text = models.CharField() # توضیحات 

    def __str__(self):
         return self.headline
     
     
# شهیدها 
class Martyrs(models.Model):

    headline = models.CharField(max_length=40) # نام شهید 
    image = models.ImageField(upload_to='martyrs/images/', blank=True, null=True) # عکس شهید 
    text = models.CharField() # توضیحات 

    def __str__(self):
        return self.headline


# پرسنل 
class Personnel(models.Model):

    headline = models.CharField(max_length=40) # نام و نام خانوادگی 
    image = models.ImageField(upload_to='personnel/images', blank=True, null=True) # عکس پرسنل 
    semat = models.CharField(max_length=52) # سمت 
    
    def __str__(self):
        return self.headline
    

# مشخصات هماشهر 
class Municipality(models.Model):

    masahat = models.IntegerField() # مساحت 
    population = models.IntegerField() # جمعیت 
    
    def __str__(self):
        return f'{self.masahat} _ {self.population}'