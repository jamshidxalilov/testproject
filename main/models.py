from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Davlat'
        verbose_name_plural = 'Davlatlar'

    def __str__(self):
        return self.name


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'

    def __str__(self):
        return self.name


class District(models.Model):
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tuman'
        verbose_name_plural = 'Tumanlar'

    def __str__(self):
        return self.name


class Partner(models.Model):
    TYPES = (
        (0, ("True")),
        (1, ("False"))
    )
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    district = models.ForeignKey(District, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    legal = models.IntegerField(choices=TYPES)
    firm = models.CharField(max_length=100, null=True)   #blank=True
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    birthday = models.DateTimeField()

    class Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = 'Hamkorlar'

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tashkilot'
        verbose_name_plural = 'Tashkilotlar'

    def __str__(self):
        return self.name


class Branch(models.Model):
    parent = models.ForeignKey('Branch', on_delete=models.RESTRICT, null=True, blank=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tarmoq'
        verbose_name_plural = 'Tarmoqlar'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Holat'
        verbose_name_plural = 'Holatlar'

    def __str__(self):
        return self.name


class Action(models.Model):
    parent = models.ForeignKey('Action', on_delete=models.RESTRICT, null=True, blank=True)
    name = models.TextField()

    class Meta:
        verbose_name = 'Harakat'
        verbose_name_plural = 'Harakatlar'

    def __str__(self):
        return self.name


class Report(models.Model):
    action = models.ForeignKey(Action, on_delete=models.RESTRICT)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)
    branch = models.ManyToManyField(Branch)
    organization = models.ManyToManyField(Organization)
    partner = models.ManyToManyField(Partner)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    district = models.ForeignKey(District, on_delete=models.RESTRICT)
    anons = models.TextField()
    result = models.TextField()
    expire_at = models.DateTimeField()
    amount = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Hisobot'
        verbose_name_plural = 'Hisobotlar'

    def __str__(self):
        return self.anons