from django.db import models

# Create your models here.
class mentors(models.Model):
    mentor_id = models.AutoField
    image = models.ImageField(upload_to='GHRCE_Konverge_Website/static/img', default="")
    image_name=models.CharField(max_length=50,default=str(image).split('/')[-1])
    mentor_name = models.CharField(max_length=50)
    position= models.CharField(max_length=50, default="")
    company = models.CharField(max_length=50, default="")
    description= models.CharField(max_length=300)
    read_more = models.CharField(max_length=50, default="#")
    pub_date = models.DateField()

    def __str__(self):
        return self.mentor_name

class m_team(models.Model):
    member_id = models.AutoField
    m_image = models.ImageField(upload_to='GHRCE_Konverge_Website/static/img', default="")
    image_name=models.CharField(max_length=50,default=str(m_image).split('/')[-1])
    member_name = models.CharField(max_length=50,default="")
    position= models.CharField(max_length=50, default="")
    company = models.CharField(max_length=50, default="")
    description= models.CharField(max_length=300)
    read_more = models.CharField(max_length=50, default="#")
    pub_date = models.DateField()

    def __str__(self):
        return self.member_name

class main_project(models.Model):
    id=models.AutoField
    number=models.IntegerField(default=0)
    image=models.ImageField(upload_to='GHRCE_Konverge_Website/static/img', default="")
    image_name=models.CharField(max_length=50,default=str(image).split('/')[-1])
    title=models.CharField(max_length=50,default="")
    subtitle=models.CharField(max_length=50, default="")
    short_description= models.CharField(max_length=300, default="")
    description= models.CharField(max_length=2000)
    link_read_more = models.CharField(max_length=50, default="project/")
    pub_date = models.DateField()
    def __str__(self):
        return self.title

class related_project(models.Model):
    id=models.AutoField
    number=models.IntegerField(default=0)
    image=models.ImageField(upload_to='GHRCE_Konverge_Website/static/img', default="")
    image_name=models.CharField(max_length=50,default=str(image).split('/')[-1])
    title=models.CharField(max_length=50,default="")
    subtitle=models.CharField(max_length=50, default="")
    short_description= models.CharField(max_length=300, default="")
    description= models.CharField(max_length=2000)
    link_read_more = models.CharField(max_length=50, default="r_project/")
    pub_date = models.DateField()
    def __str__(self):
        return self.title
    
class all_research(models.Model):
    id=models.AutoField
    number=models.IntegerField(default=0)
    image=models.ImageField(upload_to='GHRCE_Konverge_Website/static/img', default="")
    image_name=models.CharField(max_length=50,default=str(image).split('/')[-1])
    title=models.CharField(max_length=50,default="")
    subtitle=models.CharField(max_length=50, default="")
    short_description= models.CharField(max_length=300, default="")
    description= models.CharField(max_length=2000)
    link_read_more = models.CharField(max_length=50, default="research/")
    pub_date = models.DateField()
    def __str__(self):
        return self.title

class all_blog(models.Model):
    id=models.AutoField
    number=models.IntegerField(default=0)
    image=models.ImageField(upload_to='GHRCE_Konverge_Website/static/img', default="")
    image_name=models.CharField(max_length=50,default=str(image).split('/')[-1])
    title=models.CharField(max_length=100,default="")
    subtitle=models.CharField(max_length=50, default="")
    short_description= models.CharField(max_length=300, default="")
    description= models.CharField(max_length=2000, default="")
    link_read_more = models.CharField(max_length=80, default="blog/")
    pub_date = models.DateField()
    def __str__(self):
        return self.title

class contact(models.Model):
    contact_id=models.AutoField
    name=models.CharField(max_length=100,default="Name")
    email=models.EmailField(max_length=100,default='user@domain')
    subject=models.CharField(max_length=200,default='Subject')
    description=models.CharField(max_length=1000,default='Hello User')

    def __str__(self):
        return self.email
