from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from .models import *
from forms import *
import datetime
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import hashlib
import random
from datetime import datetime, timedelta, date
from django.conf import settings as conf_settings
import os
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.mail import send_mail,  EmailMultiAlternatives
from django.contrib import messages

def login(request):
	form = QpadminForm(request.POST)
	content = {}
	content['form'] = form
	content.update(csrf(request))
	if request.method == "POST":
		print "post method00000000000000000000000000000000000000000000000000"
		username = request.POST['userid']
		# password = request.POST['password']
		password = request.POST['password']
		# password = hashpass(in_password)
		user_list = Qpadmin.objects.filter(user_id=username, password1=password)
		if(user_list):
			userobj = user_list[0]
			s=userlogin(username = userobj.username, userid = userobj.user_id, role = userobj.role, logintime = datetime.now())
			s.save()   
			request.session['user'] = userobj
			# return HttpResponse("This is Admin Home Page")
			return HttpResponseRedirect("/dashboard")
		else:
			content['err_msg'] = 'Invalid Credentials'
		return render_to_response('login.html', content, context_instance=RequestContext(request))

	return render_to_response('login.html', content, context_instance=RequestContext(request))
def dashboard(request):
	content = {}
	content.update(csrf(request))
	return render_to_response('dashboard.html', content, context_instance=RequestContext(request))
def viewemployee(request):
	content = {}
	content.update(csrf(request))
	return render_to_response('viewemployee.html', content, context_instance=RequestContext(request))
def registeremployee(request):
	form = employee_detailsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
	return render_to_response("registeremployee.html",locals(),context_instance=RequestContext(request))
def viewcompanies(request):
	content = {}
	content.update(csrf(request))
	return render_to_response('viewcompanies.html', content, context_instance=RequestContext(request))
def registercompanies(request):
	form = associative_companyForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
	return render_to_response("registercompanies.html",locals(),context_instance=RequestContext(request))
def viewdevices(request):
	content = {}
	content.update(csrf(request))
	return render_to_response('viewdevices.html', content, context_instance=RequestContext(request))
def registerdevices(request):
	form = device_infoForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
	return render_to_response("registerdevices.html",locals(),context_instance=RequestContext(request))
# def logout(request):
#     user = request.session['user']
#     s=userlogout(username = user.username, userid = user.user_id,
# role = user.role, logouttime = datetime.now())            
#     s.save()
#     session_keys = request.session.keys()
#     form = UserForm(request.POST)
#     for key in session_keys:
#         del request.session[key]
#     # content.update(csrf(request))
#     return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

