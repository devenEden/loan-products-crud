from django.db import models

# Create your models here.
from django.db import models  
class LoanProduct(models.Model):  
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()

    class Meta:  
        db_table = "loan_product"  