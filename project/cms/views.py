
from django.http import HttpResponse
from .models import Content
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.shortcuts import redirect

form = """
<p>Introduce content:
<p>
<form action="" method="POST">
    Value: <input type="text" name="value">
    <br/><input type="submit" value="Submit">
</form>
"""


def loggedIn(request):

    if request.user.is_authenticated:
        logged = "Logged in as " + request.user.username
    else:
        logged = "Not logged in. <a href='/login'>Login via login</a>"

    return HttpResponse(logged)


def logout_view(request):
    logout(request)
    return redirect("/cms/")


def login_view(request):
    return redirect("/login")


@csrf_exempt
def index(request):
    return HttpResponse("You are in the root page.")


@csrf_exempt
def get_content(request, key):

    if request.method == "POST" and request.user.is_authenticated:
        value = request.POST['value']

        try:
            # if the key have been stored in a previous POST, we
            # remove it and add the new content.
            content = Content.objects.get(key=key)
            content.delete()
        except Content.DoesNotExist:
            pass

        content = Content(key=key, value=value)
        content.save()

    if request.method == "PUT" and request.user.is_authenticated:
        value = request.body.decode('utf-8')
        try:
            content = Content.objects.get(key=key)
            content.delete()
        except Content.DoesNotExist:
            pass

        content = Content(key=key, value=value)
        content.save()

    try:
        response = Content.objects.get(key=key).value
        status = 200
    except Content.DoesNotExist:
        response = 'There is no content to the key:  ' + key + '\n'
        if request.user.is_authenticated:
            response = response + form
        status = 404

    return HttpResponse(response, status=status)
