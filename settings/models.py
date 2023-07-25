from django.db import models

# Create your models here.

class company(models.Model):
    company=models.CharField(max_length=100,null=True)
    address1=models.CharField(max_length=100,null=True,blank=True)
    address2=models.CharField(max_length=100,null=True,blank=True)
    address3=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True,blank=True)
    website=models.CharField(max_length=100,null=True,blank=True)
    logo=models.ImageField(null=True)
    active=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural='companies'
    def __str__(self):
        return self.company
    
class state(models.Model):
    statename=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.statename

STATE_CHOICES = (
    ('kerala','KERALA'),
    ('karnataka','KARNATAKA'),
    ('tamilnadu','TAMILNADU'),
    ('rajasthan','RAJASTHAN')
)
class district(models.Model):
    state=models.CharField(max_length=10,choices=STATE_CHOICES)
    districtname=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.state
DISTRICT_CHOICES = (
    ('kasargod','KASARGOD'),
    ('kannur','KANNUR'),
    ('kozhikkode','KOZHKKODE'),
    ('wayanad','WAYANAD'),
    ('malappuram','MLAPPURAM'),
    ('palakkad','PALAKKAD')
)

class branch(models.Model):
    branch=models.CharField(max_length=100,null=True)
    branchcode=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    street=models.CharField(max_length=100,null=True,blank=True)
    state=models.ForeignKey(state,on_delete=models.CASCADE,null=True)
    district=models.ForeignKey(district,on_delete=models.CASCADE,null=True)
    pincode=models.IntegerField(null=True,blank=True)
    mobile=models.CharField(max_length=10,null=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    active=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural='branches'
    def __str__(self):
        return self.branch

class enquiry_source(models.Model):
    enquirysourcename=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural='Enquiry sources'
        verbose_name='enquiry sources'

    def __str__(self):
        return self.enquirysourcename

FOLLOWUP_CHOICE = (
    ('yes','Yes'),
    ('no','No')
)
class follow_up_statuses(models.Model):
    Followupstatusname=models.CharField(max_length=100,null=True)
    Followupstatus=models.CharField(max_length=100,choices=FOLLOWUP_CHOICE)
    active=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural='Follow up statuses'
        verbose_name='follow up status'
    def __str__(self):
        return self.Followupstatusname


class qualification(models.Model):
    Qualificationname=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.Qualificationname


COURSE_CHOICES = (
    ('python django','PYTHON DJANGO'),
    ('mean stack','MEAN STACK'),
    ('digital marketing','DIGITAL MARKETING')
)
TRAINER_CHOICES = (
    ('radhika','RADHIKA'),
    ('rohini','ROHINI')
)
class batch(models.Model):
    Course=models.CharField(max_length=100,null=True,choices=COURSE_CHOICES)
    Trainer=models.CharField(max_length=7,null=True,choices=TRAINER_CHOICES)
    Start_date=models.DateField()
    End_date=models.DateField()
    Closed=models.BooleanField()
    active=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural='batches'
    def __str__(self):
        return self.Course


class course(models.Model):
    pass

class master_data(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Value=models.CharField(max_length=100,null=True)
    Type=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True) 
    class Meta:
        verbose_name_plural='Master Data'
        verbose_name='master data' 
    def __str__(self):
        return self.Name

