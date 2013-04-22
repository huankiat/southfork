from django.db import models
# copied from eclipse and modified 12/5/2012

class ProductInfo(models.Model):
    part_number = models.CharField(max_length=30,primary_key=True,unique=True,null=False)
    Description = models.CharField(max_length=60)
    ProductGeneration = models.CharField(max_length=30)
# choice field - django choice field form impelementation
    Revision = models.DecimalField(max_digits=10, decimal_places=5)
    ProductCategory = models.CharField(max_length=30)
    TODate = models.DateField()
    Active = models.BooleanField()
    BOMID = models.ManyToManyField('self', through='BOMInfo', symmetrical=False, null = True, blank = True)
    TheoreticalCycleTime=models.IntegerField()
    ProductFile=models.FileField(upload_to="/productfiles", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['part_number']

    def __unicode__(self):
        return u"%s %s" % (self.part_number, self.Description, self.ProductGeneration)

class Components(models.Model):
    ComponentID = models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    BOMID = models.ForeignKey(ProductInfo)
    Description = models.CharField(max_length=100)
    ComponentName = models.CharField(max_length=200)
    Revision = models.DecimalField(max_digits=10,decimal_places=5)
    TODate = models.DateField()
    ComponentCategory = models.CharField(max_length=100)
    Manufacturers = models.CharField(max_length=100)
#    ComponentDrawing = models.FileField(upload_to="c:/users/dilan/documents/djcode/wss code/product/componentdrawings")

    class Meta:
        ordering = ['ComponentID']
    
    def __unicode__(self):
        return u"%s %s" % (self.ComponentID, self.ComponentName, self.Description)

class BOMInfo(models.Model):
    parent_product= models.ForeignKey(ProductInfo, related_name='parent_product')
    child_component= models.ForeignKey(ProductInfo, related_name='child_component')
    description = models.CharField(max_length=100)


#For below filelocation field, what should be the correct data type?
#ComponentDrawingFileLocation=models.FileField()

#class Product_BOM_History(models.Model):
#    BOMID = models.ForeignKey('MfgBOM') #Is this the right way to define foreign key?
#    ProductID=models.ForeignKey(ProductInfo)
#        
#    class Meta:
#        ordering = ['BOMID']
#
#class MfgBOM(models.Model):
#    BOMID = models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    Description = models.CharField(max_length=100)
#    
#    class Meta:
#        ordering = ['BOMID']
#class BOMID_ComponentID(models.Model):
#    BOMID=models.ForeignKey(MfgBOM)
#    ComponentQty=models.DecimalField(max_digits=10, decimal_places=5)
#    
#    class Meta:
#        ordering = ['BOMID']
#The datatype of ComponentID is not defined in the database, defined here as floating point

#class Component_Manufacturer(models.Model):
#    ComponentID=models.ForeignKey(Components)
    
#class Product_Route(models.Model):
#    ProductID=models.ForeignKey(ProductInfo)
#    RouteID=models.ForeignKey('Route')
    
#    class Meta:
#        ordering = ['RouteID']

#class Route(models.Model):
#    RouteID=models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    CycleTime=models.DecimalField(max_digits=10,decimal_places=5)
#    ProcessTime=models.DecimalField(max_digits=10,decimal_places=5)
    
#    class Meta:
#        ordering = ['RouteID']

#class Operation_Recipe_Equipment(models.Model):
#    OperationID=models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    RouteID=models.ForeignKey(Route)
#    RecipeID=models.ForeignKey('Recipe')
#    EquipmentGroupID=models.ForeignKey('EquipmentGroup_Equipment')
#    Sequence=models.IntegerField() # Sequence's data type is not defined in the database
#    
#    class Meta:
#        ordering = ['OperationID']

#deled by Dilan 12/2/2012
#class EquipmentGroup_Equipment(models.Model):
#    EquipmentGroupID=models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#Only one field defined in the database model for this table, is this correct?

#class Equipment(models.Model):
#    EquipmentID=models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    LocationID=models.CharField(max_length=50)
#    Description=models.CharField(max_length=100)
#    EquipmentGroupID=models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    
#    class Meta:
#        ordering = ['EquipmentID']

#class Recipe(models.Model):
#    RecipeID=models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    SpecialInstruction=models.CharField(max_length=200)
#    
#    class Meta:
#        ordering = ['RecipeID']

#class Manufacturers(models.Model):
#    ManufacturerID=models.CharField(max_length=50,primary_key=True,unique=True,null=False)
#    ManufacturerName=models.CharField(max_length=100)
#    ManufacturerInternalPartNumber=models.CharField(max_length=100)
#    Sites=models.CharField(max_length=100)
#    Factory=models.CharField(max_length=100)
#    TheoreticalCycleTime=models.IntegerField()
#    Cost=models.DecimalField(max_digits=10,decimal_places=5)
#    Active=models.BooleanField()
    
#    class Meta:
#        ordering = ['ManufacturerName']

#class PriceHistory(models.Model):
#    ProductID=models.ForeignKey(ProductInfo)
#    Price=models.DecimalField(max_digits=10,decimal_places=5)
#    PriceDate=models.DateField()
#CustomerID=models.CharField(max_length=100)
#CustomerID is to be added field
#    class Meta:
#        ordering = ['Price']

#class Order_Product(models.Model):
#    ProductID=models.ForeignKey(ProductInfo)
#    OrderID=models.ForeignKey('Order')
#    
#    class Meta:
#        ordering = ['OrderID']

#class Order(models.Model):
#    OrderID=models.CharField(max_length=100,primary_key=True,unique=True,null=False)
#    Site=models.CharField(max_length=100)
#    Carriers=models.CharField(max_length=100)
#    PackingCratingConstrains=models.CharField(max_length=200)
#    Quantity=models.DecimalField(max_digits=10,decimal_places=5)
#CustomerID=models.ForeignKey(PriceHistory)
#CustomerID is to be added field
#    class Meta:
#        ordering = ['OrderID']