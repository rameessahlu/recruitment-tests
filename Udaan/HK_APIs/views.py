from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import logging
from datetime import date, datetime

from django.conf import settings
from HK_APIs.models import Asset, Worker, Task, TaskAllocation


fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)
logging.basicConfig(format=fmt, level=lvl)
logging.debug("Logging started on %s for %s" % (logging.root.name, logging.getLevelName(lvl)))


@csrf_exempt 
def add_asset(request):
    return render(request, 'add_asset.html')

@csrf_exempt 
def add_asset_form(request):
	_assetName = request.POST['assetName']
	_assetId = request.POST['assetId']
	logging.debug('Successfully added! {}'.format(_assetId))
	_asset = Asset.objects.get_or_create(assetId=int(_assetId), assetName=_assetName)[0]
	return add_asset(request)
	#return render(request, 'add_asset.html', {'data':data})

@csrf_exempt 
def add_task(request):
    return render(request, 'add_task.html')

@csrf_exempt 
def add_task_form(request):
	_taskDescription = request.POST['taskDescription']
	_taskId = request.POST['taskId']
	logging.debug('Successfully added! {}'.format(_taskId))
	_task = Task.objects.get_or_create(taskId=int(_taskId), taskDescription=_taskDescription)[0]
	return add_task(request)

@csrf_exempt 
def add_worker(request):
    return render(request, 'add_worker.html')

@csrf_exempt 
def add_worker_form(request):
	_workerName = request.POST['workerName']
	_workerId = request.POST['workerId']
	logging.debug('Successfully added! {}'.format(_workerId))
	_worker = Worker.objects.get_or_create(workerId=int(_workerId), workerName=_workerName)[0]
	return add_worker(request)

@csrf_exempt 
def allocate_task(request):
    return render(request, 'allocate_task.html')


@csrf_exempt 
def allocate_task_form(request):
	task = Task.objects.filter( taskId=int(request.POST['taskId']) )[0]
	worker = Worker.objects.filter( workerId=int(request.POST['workerId']) )[0]
	asset = Asset.objects.filter( assetId=int(request.POST['assetId']) )[0]
	_taskToBePerformedBy = datetime.strptime(request.POST['taskToBePerformedBy'], "%Y-%m-%dT%H:%M")
	_timeOfAllocation = date.today().strftime("%Y-%m-%dT%H:%M")
	
	_taskAllocation = TaskAllocation.objects.get_or_create(_task=task, _worker=worker, 
						_asset=asset, taskToBePerformedBy=_taskToBePerformedBy,
						timeOfAllocation=_timeOfAllocation)[0]
	return allocate_task(request)

@csrf_exempt
def assets_all(request):
	w = Asset.objects.all()
	return HttpResponse(serializers.serialize("json", w))

@csrf_exempt
def get_tasks_for_workers(request, workerId):
	_worker = Worker.objects.filter(workerId=workerId)[0]
	taskAllocation = TaskAllocation.objects.filter(_worker=_worker)
	return HttpResponse(serializers.serialize("json", taskAllocation))

@csrf_exempt
def home(request):
	return render(request, 'home.html')

@csrf_exempt
def debug(request):
	w = Worker.objects.filter(workerId=1)
	return HttpResponse(getattr(w[0], 'workerName'))