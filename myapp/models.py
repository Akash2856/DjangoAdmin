from django.db import models



class emp_table(models.Model):
    emp_id = models.IntegerField()
    emp_first_name = models.CharField(max_length=10)
    emp_last_name = models.CharField(max_length=10)

    def __str__(self):
        return self.emp_first_name

class emp_salary(models.Model):
    id1 = models.ForeignKey(emp_table, on_delete=models.CASCADE)
    emp_sal = models.IntegerField()

