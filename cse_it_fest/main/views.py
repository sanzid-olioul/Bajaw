from django.shortcuts import render
from django.views import View
from .models import Team,Contestent,ContestName,TeamContestent
# Create your views here.


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, "demoForm.html")
    def post(self, request, *args, **kwargs):
        if request.POST.get('first_roll') != request.POST.get('secound_roll')\
         or request.POST.get('first_roll') != request.POST.get('third_roll')\
            or request.POST.get('secound_roll') != request.POST.get('third_roll'):
            first_roll = request.POST.get('first_roll')
            secound_roll = request.POST.get('secound_roll')
            third_roll = request.POST.get('third_roll')
            first_roll = request.POST.get('first_roll')
            secound_roll = request.POST.get('secound_roll')
            third_roll = request.POST.get('third_roll')
            first_reg = request.POST.get('first_reg')
            secound_reg = request.POST.get('secound_reg')
            third_reg = request.POST.get('third_reg')
            first_name = request.POST.get('first_name')
            secound_name = request.POST.get('secound_name')
            third_name = request.POST.get('third_name')
            depaerment = request.POST.get('team_department')
            team_name = request.POST.get('team_name')
            contest_type = request.POST.get('contest_type')
            
            print(contest_type," ------------",secound_name)
            contest = ContestName.objects.get(contest_name = contest_type)

            team = Team(team_name = team_name,department = depaerment,contest_type= contest)
            team.save()
            user1 = Contestent.objects.filter(roll_no = first_roll)
            if not user1:
                user1 = Contestent(roll_no = first_roll,reg_no = first_reg,full_name= first_name)
                user1.save()
            else:
                user1 = user1[0]
            user2 = Contestent.objects.filter(roll_no = secound_roll)
            if not user2:
                user2 = Contestent(roll_no = secound_roll,reg_no = secound_reg,full_name= secound_name)
                user2.save()
            else:
                user2 = user2[0]
            user3 = Contestent.objects.filter(roll_no = third_roll)
            if not user3:
                user3 = Contestent(roll_no = third_roll,reg_no = third_reg,full_name= third_name)
                user3.save()
            else:
                user3 = user3[0]
            cnt1 = TeamContestent(team = team,contestent=user1)
            cnt1.save()
            cnt2 = TeamContestent(team = team,contestent=user2)
            cnt2.save()
            cnt3 = TeamContestent(team = team,contestent=user3)
            cnt3.save()

        return render(request, "demoForm.html")