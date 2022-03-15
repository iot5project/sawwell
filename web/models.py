from django.db import models


class Cust(models.Model):
    custno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    regdate = models.DateField(auto_now=True)

    class Meta:
        db_table = 'cust'


class Categori(models.Model):
    cid = models.AutoField(primary_key=True)
    categoriname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'categori'


class Food(models.Model):
    foodid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    regdate = models.DateField(auto_now=True)

    class Meta:
        db_table = 'food'


class Market(models.Model):
    marketno = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Categori, models.DO_NOTHING, db_column='cid')
    foodid = models.ForeignKey(Food, models.DO_NOTHING, db_column='foodid')
    marketname = models.CharField(max_length=100, blank=True, null=True)
    marketaddress = models.CharField(max_length=100, blank=True, null=True)
    regdate = models.DateField(auto_now=True)
    open = models.TimeField(blank=True, null=True)
    close = models.TimeField(blank=True, null=True)
    holiday = models.DateField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'market'


class Ceo(models.Model):
    ceoid = models.AutoField(primary_key=True)
    marketno = models.ForeignKey('Market', models.DO_NOTHING, db_column='marketno')
    id = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'ceo'


class Reply(models.Model):
    replyid = models.AutoField(primary_key=True)
    reviewno = models.ForeignKey('Review', models.DO_NOTHING, db_column='reviewno')
    ceoid = models.ForeignKey(Ceo, models.DO_NOTHING, db_column='ceoid')
    content = models.CharField(max_length=100, blank=True, null=True)
    regdate = models.DateField(auto_now=True)

    class Meta:
        db_table = 'reply'


class Review(models.Model):
    reviewno = models.AutoField(primary_key=True)
    marketno = models.ForeignKey(Market, models.DO_NOTHING, db_column='marketno')
    custno = models.ForeignKey(Cust, models.DO_NOTHING, db_column='custno')
    content = models.CharField(max_length=100, blank=True, null=True)
    star = models.FloatField(blank=True, null=True)
    regdate = models.DateField(auto_now=True)

    class Meta:
        db_table = 'review'


class Seocho(models.Model):
    seochono = models.IntegerField(primary_key=True)
    marketname = models.CharField(max_length=50, blank=True, null=True)
    ceoname = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    categori = models.CharField(max_length=100, blank=True, null=True)
    food = models.CharField(max_length=100, blank=True, null=True)
    open = models.CharField(max_length=100, blank=True, null=True)
    close = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'seocho'


class Seochofood(models.Model):
    foodid = models.AutoField(primary_key=True)
    seochono = models.ForeignKey(Seocho, models.DO_NOTHING, db_column='seochono')
    name = models.CharField(max_length=30, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    regdate = models.DateField(auto_now=True)

    class Meta:
        db_table = 'seochofood'
