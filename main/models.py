from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=55)
    addition = models.CharField(max_length=25)
    img = models.ManyToManyField(to='Image')


class Image(models.Model):
    img = models.ImageField(upload_to="banner_iamge/")
    img_desciption = models.CharField(max_length=12)

    def __str__(self):
        return self.img_desciption

class Sevice(models.Model):
    icon = models.ImageField(upload_to="icon_sevice/")
    title = models.CharField(max_length=25)
    desciption = models.CharField(max_length=27)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=55)
    rayting = models.FloatField(default=0)
    old_price = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    descipton = models.TextField()
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    additional = models.ManyToManyField(to="Additional")
    def __str__(self):
        return self.name

class Additional(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Section(models.Model):
    title = models.CharField(max_length=75)
    additional = models.CharField(max_length=75)
    desciption = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to="img_section/")

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=55)
    desciption = models.CharField(max_length=255)
    rayting = models.FloatField(default=0)
    img = models.ImageField(upload_to="testimobial_img/")
    professiom = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Info(models.Model):
    bran_name = models.CharField(max_length=55)
    adress = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)


    def __str__(self):
        return self.bran_name

class cart(models.Model):
    # user = models.OneToOneField(to="User", on_delete=models.PROTECT)
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name



class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)