from django.db import models


class ProductInfo(models.Model):
    part_number = models.CharField(max_length=30,primary_key=True,unique=True,null=False)
    description = models.CharField(max_length=60)
    product_generation = models.CharField(max_length=30)
    revision = models.DecimalField(max_digits=10, decimal_places=5)
    product_category = models.CharField(max_length=30)
    to_date = models.DateField()
    active = models.BooleanField()
    bom_number = models.ManyToManyField('self', through='BOMInfo', symmetrical=False, blank=True, null=True)
    theoretical_cycle_time=models.IntegerField()
    product_file=models.FileField(upload_to="c:/users/dilan/documents/djcode/wss code/product/uploaded_productfiles", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['part_number']
        
    @models.permalink
    def get_absolute_url(self):
        return ('',(),{'part_number':self.part_number}) #need to add product view partnumber
    

    def __unicode__(self):
        return u"%s %s %s %s" % (self.part_number, self.description, self.product_generation, self.product_category)

class Components(models.Model):
    component_number = models.CharField(max_length=50,primary_key=True,unique=True,null=False)
    description = models.CharField(max_length=100)
    component_name = models.CharField(max_length=200)
    revision = models.DecimalField(max_digits=10,decimal_places=5)
    to_date = models.DateField()
    component_category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)

    class Meta:
        ordering = ['component_number']
    
    def __unicode__(self):
        return u"%s %s %s %s %s" % (self.component_number, self.description, self.component_name, self.component_category, self.manufacturer)

class BOMInfo(models.Model):
    parent= models.ForeignKey(ProductInfo, related_name='parent')
    child= models.ForeignKey(ProductInfo, related_name='child')
    description = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['parent']

