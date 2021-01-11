from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique order instances

class Customer(models.Model):
    """
    Model representing a Customer features
    """
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField()
    customer_phone = models.CharField('PhoneNumber',max_length=11, help_text='11 Character')
    # TODO: Validation for phonenumber
    customer_address = models.TextField(max_length=1000, help_text="Please Enter Complete Your Address Here")
    # customer_Location=? (use location field in django?)
    CITY_STATUS = (
        ('1','اراک'),
        ('2','اردبیل'),
        ('3','ارومیه'),
        ('4','اصفهان'),
        ('5','اهواز'),
        ('6','ایلام'),
        ('7','بجنورد'),
        ('8','بندرعباس'),
        ('9','بوشهر'),
        ('10','بیرجند'),
        ('11','تبریز'),
        ('12','تهران'),
        ('13','خرم‌آباد'),
        ('14','رشت'),
        ('15','زاهدان'),
        ('16','زنجان'),
        ('17','ساری'),
        ('18','سمنان'),
        ('19','سنندج'),
        ('20','شهرکرد'),
        ('21','شیراز'),
        ('22','قزوین'),
        ('23','قم'),
        ('24','کرج'),
        ('25','کرمان'),
        ('26','کرمانشاه'),
        ('27','گرگان'),
        ('28','مشهد'),
        ('29','همدان'),
        ('30','یاسوج'),
        ('31','یزد'),
    )
    customer_city  = models.CharField(max_length=2, choices=CITY_STATUS, blank=True, default='12',help_text='Please Choose your city')
    # state=? this field show all orders of a cstomer

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.customer_first_name)+" "+str(self.customer_last_name)


class Store(models.Model):
    """
    Model representing a Store features
    """
    store_name = models.CharField(max_length=100)
    store_phone = models.CharField('PhoneNumber',max_length=11, help_text='11 Character')
    # TODO: Validation for phonenumber
    store_address = models.TextField(max_length=1000, help_text="Please Enter Complete Your Address Here")
    email = models.EmailField()
    # store_Location=? (use location field in django?)
    CITY_STATUS = (
        ('1','اراک'),
        ('2','اردبیل'),
        ('3','ارومیه'),
        ('4','اصفهان'),
        ('5','اهواز'),
        ('6','ایلام'),
        ('7','بجنورد'),
        ('8','بندرعباس'),
        ('9','بوشهر'),
        ('10','بیرجند'),
        ('11','تبریز'),
        ('12','تهران'),
        ('13','خرم‌آباد'),
        ('14','رشت'),
        ('15','زاهدان'),
        ('16','زنجان'),
        ('17','ساری'),
        ('18','سمنان'),
        ('19','سنندج'),
        ('20','شهرکرد'),
        ('21','شیراز'),
        ('22','قزوین'),
        ('23','قم'),
        ('24','کرج'),
        ('25','کرمان'),
        ('26','کرمانشاه'),
        ('27','گرگان'),
        ('28','مشهد'),
        ('29','همدان'),
        ('30','یاسوج'),
        ('31','یزد'),
    )
    store_city  = models.CharField(max_length=2, choices=CITY_STATUS, blank=True, default='12',help_text='Please Choose your city')
    # state=? This attribiute is supposed to show all the orders that the store has made

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.store_name

class Order(models.Model):
    """
    Model representing order features
    """
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular orders")
    order_name = models.CharField(max_length=400, help_text="Please Enter your order name or comment")
    order_date = models.DateField(null=True, blank=True)
    order_customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    order_store = models.ForeignKey('Store',on_delete=models.SET_NULL, null=True)
    ORDERR_STATUS= (
        ('w','Waiting to accept by nearest store'),
        ('a', 'accept by store'),
        ('n', 'not accept'),
        ('p', 'In Progress'),
        ('r', 'Ready'),
        ('d', 'Delivered'),
    )
    order_status = models.CharField(max_length=1, choices= ORDERR_STATUS, blank=True, default='w')
    delivered_date = models.DateField(null=True, blank=True)
    # order_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ["order_date"]
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.order_customer,self.order_name)


class Product(models.Model):
    """
    Model representing products features
    """
    PRODUCT_CATEGORY = (
        ('1','Laundry Service'),
        ('2','Dry Cleaning & Ironed Laundry'),
        ('3','Home & Bedding'),
    )
    product_name = models.CharField(max_length=1, choices= PRODUCT_CATEGORY, blank=True, default='1')
    # product_price_choice=(
    # (if product_name == PRODUCT_CATEGORY[0] : ,
    #         product_price == '23$ per led of 6 kg'),
    # (elif product_name == PRODUCT_CATEGORY[1] :
    #         product_price == ' 2.50 $ per item '),
    # (else :
    #     product_price == ' 15$ per item')
    # )
    product_price = models.CharField(max_length=100)
    # product_customer =  models.ManyToManyField(Customer, help_text="Please Select customer for this Product", blank=True)
    # ManyToManyField used because customers can contain many order and products. Products can cover many customers.
    # Customers class has already been defined so we can specify the object above.
    # product_stores =  models.ManyToManyField(Store, help_text="Please Select Stores for this Product", blank=True)
    # ManyToManyField used because Stores can contain many order and products. Products can cover many Stores.
    # Stores class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.product_name
        # return str(self.product_name)+""+str(self.product_customer)+""+str(self.product_stores)


