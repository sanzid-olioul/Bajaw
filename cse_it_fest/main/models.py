from django.db import models

# Create your models here.

class ContestName(models.Model):
    PROJECT_EXHITION = 'PE'
    PROGRAMMING_CONTEST = 'PC'
    IT_QUIZ = 'ITQ'
    NAME = [
        ('PROJECT_EXHITION',PROJECT_EXHITION),
        ('PROGRAMMING_CONTEST',PROGRAMMING_CONTEST),
        ('IT_QUIZ',IT_QUIZ),
    ]
    contest_name = models.CharField(max_length=20,choices=NAME,primary_key=True,default=PROGRAMMING_CONTEST)

    def __str__(self):
        return self.contest_name
    



class Team(models.Model):
    team_name = models.CharField(max_length=50,primary_key=True)
    department = models.CharField(max_length=50)
    contest_type = models.ForeignKey(ContestName, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.team_name



class Contestent(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    reg_no = models.IntegerField()
    full_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.full_name

class TeamContestent(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    contestent = models.ForeignKey(Contestent, on_delete=models.CASCADE)

    def __str__(self):
        return self.contestent + " of team "+ self.team