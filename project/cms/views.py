
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


def logged_in(request):

    if request.user.is_authenticated:
        logged = "Logged in as " + request.user.username
    else:
        logged = "Not logged in. <a href='/login'>Login via login</a>"

    return HttpResponse(logged)


def logout_view(request):
    logout(request)
    return redirect("/cms/")


def login_view():
    return redirect("/login")


@csrf_exempt
def index():
    return HttpResponse("You are in the root page.", status=200)


@csrf_exempt
def get_content(request, key):

    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponse("Cannot add content with POST. Not logged in. <a href='/login'>Login</a>", status=404)
        else:
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

    if request.method == "PUT":
        if not request.user.is_authenticated:
            return HttpResponse("Cannot add content with PUT. Not logged in. <a href='/login'>Login</a>", status=404)
        else:
            value = request.body.decode('utf-8')
            try:
                content = Content.objects.get(key=key)
                content.delete()
            except Content.DoesNotExist:
                pass

            content = Content(key=key, value=value)
            content.save()

    try:
        response = "Key '" + key + "' value is: " + Content.objects.get(key=key).value + "<br>"
        status = 200
        if request.user.is_authenticated:
            response += "Logged in as " + request.user.username
        else:
            response += "Not logged in. <a href='/login'>Login</a>"

    except Content.DoesNotExist:
        response = 'There is no content for key: ' + key + '<br>'
        if request.user.is_authenticated:
            response += form + "Logged in as " + request.user.username
        else:
            response += "Not logged in. <a href='/login'>Login</a>"

        status = 404

    return HttpResponse(response, status=status)
