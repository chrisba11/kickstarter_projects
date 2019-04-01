from django.db import models

# Create your models here.


class Project(models.Model):
    """

    """
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=48)
    main_category = models.CharField(max_length=48)
    currency = models.CharField(max_length=12)
    deadline = models.DateField()
    goal = models.IntegerField()
    launched = models.DateTimeField()
    pledged = models.FloatField()
    state = models.CharField(max_length=24)
    backers = models.IntegerField()
    country = models.CharField(max_length=12)
    usd_pledged = models.FloatField()
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()

    def __repr__(self):
        return '<Project: {} | State: {}>'.format(self.name, self.state)

    def __str__(self):
        return 'Project: {} | State: {}'.format(self.name, self.state)
