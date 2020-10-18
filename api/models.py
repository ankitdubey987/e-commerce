from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class CustomerProfile(models.Model):
    UserId = models.ForeignKey(User,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=32)
    LastName = models.CharField(max_length=32)
    Address1 = models.TextField()
    Address2 = models.TextField()
    City = models.CharField(max_length=32)
    State = models.CharField(max_length=32)
    PostalCode = models.CharField(max_length=8)
    Country = models.CharField(max_length=32)
    BillingAddress = models.TextField()
    BillingCity = models.CharField(max_length=32)
    BillingRegion = models.CharField(max_length=32)
    BillingPostalCode = models.CharField(max_length=8)
    BillingCountry = models.CharField(max_length=32)
    ShipAddress = models.TextField()
    ShipCity = models.CharField(max_length=32)
    ShipRegion = models.CharField(max_length=32)
    ShipPostalCode = models.CharField(max_length=8)
    ShipCountry = models.CharField(max_length=32)
    DateEntered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("customer_profile")
        verbose_name_plural = ("customers_profile")

    def __str__(self):
        return self.FirstName

    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})

class Shippers(models.Model):

    CompanyName = models.TextField()
    Phone = models.CharField(max_length=13)

    class Meta:
        verbose_name = ("shippers")
        verbose_name_plural = ("shippers")

    def __str__(self):
        return self.CompanyName

    def get_absolute_url(self):
        return reverse("shippers_detail", kwargs={"pk": self.pk})

class Orders(models.Model):
    """Model definition for Orders."""

    CustomerID = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
    OrderNumber = models.TextField()
    PaymentID = models.TextField()
    OrderDate = models.DateTimeField()
    ShipDate = models.DateTimeField()
    RequiredDate = models.DateTimeField()
    ShipperID = models.ForeignKey(Shippers,on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(auto_now_add=True)
    TransactStatus = models.BooleanField(default=False)
    Paid = models.BooleanField(default=False)
    PaymentDate = models.DateTimeField()


    class Meta:
        """Meta definition for Orders."""

        verbose_name = 'Orders'
        verbose_name_plural = 'Orderss'

    def __str__(self):
        """Unicode representation of Orders."""
        pass


class Payment(models.Model):

    PaymentType = models.CharField(max_length=32)
    Allowed = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("payment")
        verbose_name_plural = ("payments")

    def __str__(self):
        return self.PaymentType

    def get_absolute_url(self):
        return reverse("payment_detail", kwargs={"pk": self.pk})

class Category(models.Model):
  
    name = models.CharField(max_length=32,unique=True)
    desc = models.TextField()
    picture = models.ImageField(upload_to='categories/images/')
    active = models.BooleanField(default=False)

class Supplier(models.Model):
    title_choices = (
        ('Mr','MR.'),
        ('Miss','MISS.'),
        ('Mrs','MRS.'),
    )

    pay_method = (
        ('cash','CASH ON DELIVERY'),
        ('netbanking','NET BANKING'),
        ('emi','EMI'),
    )
    company_name = models.CharField(max_length=32,null=False)
    first_name = models.CharField(max_length=32,null=False)
    last_name = models.CharField(max_length=32,null=False)
    title = models.CharField(choices=title_choices,max_length=8)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=32,null=False)
    state = models.CharField(max_length=32,null=False)
    postal_code = models.CharField(max_length=8)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    Email = models.CharField(max_length=32,null=False)
    customer_id = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
    payment_method = models.CharField(choices=pay_method,max_length=10,null=False)

class Product(models.Model):
    IDSKU = models.CharField(max_length=50)
    vendor_id = models.IntegerField()
    category_id =models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    desc = models.TextField()
    qty_per_unit = models.IntegerField()
    mrp = models.FloatField()
    market_price = models.FloatField()
    our_price = models.FloatField()
    image = models.ImageField(upload_to='product/images/')

class OrderDetail(models.Model):

    OrderId = models.ForeignKey(Orders,on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product,on_delete=models.CASCADE) 
    OrderNumber = models.CharField(max_length=32)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Total = models.IntegerField()
    IDSKU = models.CharField(max_length=50)
    ShipDate = models.DateTimeField()
    BillDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("orderdetail")
        verbose_name_plural = ("orderdetails")

    def __str__(self):
        return self.IDSKU

    def get_absolute_url(self):
        return reverse("orderdetail_detail", kwargs={"pk": self.pk})



