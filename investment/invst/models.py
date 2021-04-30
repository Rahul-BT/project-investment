from django.db import models

# Create your models here.

class Invst(models.Model):
    date = models.DateField(verbose_name='Date')
    rx = models.CharField(verbose_name='RX', max_length=30)
    invst_type = models.CharField(verbose_name='Type', max_length=10)
    amount = models.DecimalField(verbose_name='Amount', decimal_places=2, max_digits=9)
    mat = models.DecimalField(verbose_name='Maturity', blank=True, null=True, decimal_places=2, max_digits=9)
    end_date = models.DateField(verbose_name='Date', blank=True, null=True)
    roi = models.FloatField(verbose_name='RoI', blank=True, null=True)
    months = models.IntegerField(verbose_name='Months', blank=True, null=True)
    roiYear = models.FloatField(verbose_name='Roi/Year', blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Investment'

    def __str__(self):
        return f"{self.id}. {self.rx} - {self.invst_type}"

    def computeInvst(self):
        # Compute RoI
        self.roi = round((self.mat - self.amount) / self.amount * 100, 2)
        
        # Compute months
        self.months = (int(self.end_date.strftime('%Y')) - int(self.date.strftime('%Y'))) * 12 + int(self.end_date.strftime('%m')) - int(self.date.strftime('%m'))
        
        # Compute roi/Year
        self.roiYear = round(self.roi/self.months * 12, 2)

   # def returnVariable(self):
        

class MF(models.Model):
    date = models.DateField(verbose_name='Date')
    planName = models.CharField(verbose_name='Plan Name', max_length=90)
    platform = models.CharField(verbose_name='Platform', max_length=10)
    amount = models.DecimalField(verbose_name='Amount', decimal_places=2, max_digits=7)
    lockin = models.DecimalField(verbose_name='Lock-In', blank=True, null=True, decimal_places=1, max_digits=3)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Mutual Fund'

    def __str__(self):
        return f"{self.id}. {self.planName}"


