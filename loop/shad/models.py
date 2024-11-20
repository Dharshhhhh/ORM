class bankloan(models.Model);
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.Charfield(max_length=10)
    loan_amt = models.IntegerField
    cust_acno = models.IntegerField
    cust_name = models.CharField(max_length=50)