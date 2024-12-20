from django.db import models

STATE_CHOICE =(
    ("AP", "Andhra Pradesh"),
    ("AR", "Arunachal Pradesh"),
    ("AS", "Assam"),
    ("BR", "Bihar"),
    ("CT", "Chhattisgarh"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"),
    ("JK", "Jammu and Kashmir"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("MP", "Madhya Pradesh"),
    ("MH", "Maharashtra"),
    ("MN", "Manipur"),
    ("ML", "Meghalaya"),
    ("MZ", "Mizoram"),
    ("NL", "Nagaland"),
    ("OR", "Odisha"),
    ("PB", "Punjab"),
    ("RJ", "Rajasthan"),
    ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"),
    ("TG", "Telangana"),
    ("TR", "Tripura"),
    ("UP", "Uttar Pradesh"),
    ("UT", "Uttarakhand"),
    ("WB", "West Bengal"),
    ("AN", "Andaman and Nicobar Islands"),
    ("CH", "Chandigarh"),
    ("DN", "Dadra and Nagar Haveli and Daman and Diu"),
    ("DL", "Delhi"),
    ("LD", "Lakshadweep"),
    ("PY", "Puducherry"),
)

ROLE_CHOICES = (
    ("fe","Frontend"),
    ("be", "Backend"),
    ("fs", "FullStake")
)

class Resume(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    github = models.URLField()
    mobile = models.PositiveIntegerField()
    skill = models.CharField(max_length=80)
    role = models.CharField(choices=ROLE_CHOICES,max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=STATE_CHOICE , max_length=100)
    image = models.ImageField(upload_to='profileimg', blank=True)
    documents = models.FileField(upload_to='doc', blank=True)

    def __str__(self):
        return f"{self.name}"
