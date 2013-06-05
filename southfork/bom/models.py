from django.db import models

class ProductInfo(models.Model):
    part_number = models.CharField(max_length=30,primary_key=True,unique=True,null=False)
#    component = models.ManyToManyField('self', through='BOMInfo', symmetrical=False, blank=True, null=True)
#    component = models.ForeignKey(Components)
    description = models.CharField(max_length=60)
    product_generation = models.CharField(max_length=30, blank=True)
    revision = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
    product_category = models.CharField(max_length=30, blank=True)
    to_date = models.DateField()
    active = models.BooleanField()
    theoretical_cycle_time=models.IntegerField()
    product_file=models.FileField(upload_to="/product/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['part_number']
        
    @models.permalink
    def get_absolute_url(self):
        return ('southfork.bom.views.product_detail',(),{'partnumber':self.part_number}) #need to add product view partnumber

    def __unicode__(self):
        return u"%s %s %s %s" % (self.part_number, self.description, self.product_generation, self.product_category)

class BOMInfo(models.Model):
    bom_number = models.CharField(max_length=30,primary_key=True,unique=True,null=False)
    comps = models.ManyToManyField(ProductInfo, through='Components')   
#    components = models.ManyToManyField('self', through='Components', symmetrical=False, blank=True, null=True)   
#    parent= models.ForeignKey(ProductInfo, related_name='parent')
#    child= models.ForeignKey(ProductInfo, related_name='child')
#    component_number=models.ForeignKey(Components)    
#    bom_number=models.ForeignKey(ProductInfo)
#    description = models.CharField(max_length=100)
#    
    class Meta:
        ordering = ['bom_number']

#TODO: Dilan/Xuan - need to enable get absolute url for pulling up details under each bom number.
    @models.permalink
    def get_absolute_url(self):
        return ('southfork.bom.views.bom_detail',(),{'bomnumber':self.bom_number})
   
    def __unicode__(self):
        return u"%s" % (self.bom_number)

class Components(models.Model):
    part_number = models.ForeignKey(ProductInfo)
    bom = models.ForeignKey(BOMInfo)
    qty = models.IntegerField()
#    component_number = models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    description = models.CharField(max_length=100)
#    component_name = models.CharField(max_length=200)
#    revision = models.DecimalField(max_digits=10,decimal_places=5)
#    to_date = models.DateField()
#    component_category = models.CharField(max_length=100)
#    manufacturer = models.CharField(max_length=100)
#
    class Meta:
        ordering = ['part_number']
    
    def __unicode__(self):
        return u"%s" % (self.part_number)
