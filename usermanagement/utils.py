from django.core.mail import send_mail as sendMail
from django.conf import settings
import json
from io import BytesIO
from django.http import FileResponse


def generate_user_from_email(email):
    return email.replace("@", "")

def generate_email_json(teamName, mailAddress, mailSubject, mailContent, password=None):
    email_json = {
        'teamName': teamName,
        "mailAddress": mailAddress,
        "mailSubject": mailSubject,
        "mailContent": mailContent,
        "password": password
    }
    return email_json

def send_mail(teamName, email, mailSubject, mailContent, password=None):

    subject = mailSubject
    message = mailContent
    if password:
        message += "\n\n Your user is: %s \n Your password is %s" % (generate_user_from_email(email), password)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]   
    sendMail(subject, "", email_from, recipient_list, html_message=message)


def export_teams(adminType, is_finalized):
     # I seriously tried to avoid this bullcrap, but finally because of serializers there was no ducking conditions.

    from .admin import OnlineTeamAdmin, OnsiteTeamAdmin
    from .api.serializers import OnsiteTeamGenerateSerializer, OnlineTeamGenerateSerializer
    from .models import OnlineTeam, OnsiteTeam

    if adminType is OnlineTeamAdmin:
        team_class = OnlineTeam
        serializer_class = OnlineTeamGenerateSerializer
    elif adminType is OnsiteTeamAdmin:
        team_class = OnsiteTeam
        serializer_class = OnsiteTeamGenerateSerializer
    if is_finalized:
        teams = team_class.objects.filter(status='PAID')
    else:
        teams = team_class.objects.all()
    serializer = serializer_class(teams, many=True)

    return serializer.data

def export_contestants(adminType, is_finalized):
    from .admin import OnlineTeamAdmin, OnsiteTeamAdmin
    from .api.serializers import OnsiteContestantGenerateSerializer, OnlineContestantGenerateSerializer
    from .models import OnsiteContestant, OnlineContestant

    if adminType is OnsiteTeamAdmin:
        serializer_class = OnsiteContestantGenerateSerializer
        contestant_class = OnsiteContestant
        team_class = "onsiteteam"
    elif adminType is OnlineTeamAdmin:
        serializer_class = OnlineContestantGenerateSerializer
        contestant_class = OnlineContestant
        team_class = "onlineteam"

    if is_finalized:
        team_ids = []
        contestants_all = contestant_class.objects.all()
        for contestant in contestants_all:
            team_ptr = getattr(contestant.team, team_class)
            if team_ptr.status == 'PAID':
                team_ids.append(team_ptr.id)
        contestants = contestant_class.objects.filter(team__id__in=team_ids).order_by('team__name')
    else:
        contestants = contestant_class.objects.order_by('team__name')

    serializer = serializer_class(contestants, many=True)
    return serializer.data


def create_sv_response(sv_str, file_name):
    sv_bytes = str.encode(sv_str, encoding='utf-8')
    sv_bytesIO = BytesIO(sv_bytes)
    response = FileResponse(sv_bytesIO)
    response['Content-Disposition'] = 'attachment; filename= %s' %file_name
    return response


# Separator is either comma or a tab character

def generate_sv_str(headers, separator):
    return separator.join(headers) + '\n'


def generate_current_line(headers, record, separator):
    currentLine = []
    for header in headers:
        if header in record.keys():
            currentLine.append(record[header])
        else:
            currentLine.append('')
    add_str = generate_sv_str(currentLine, separator)
    return add_str


def team_json_to_sv_file_response(json_obj, file_name, separator):

     # Keep track of headers in a set
    headers = json_obj[0].keys()

    # You only know what headers were there once you have read all the JSON once.
    # Now we have all the information we need, like what all possible headers are.
    
    sv_str = generate_sv_str(headers, separator)
    for record in json_obj:
        sv_str += generate_current_line(headers, record, separator)
    
    return create_sv_response(sv_str, file_name)

