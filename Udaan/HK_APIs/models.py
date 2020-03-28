from django.db import models
from datetime import date, datetime

class Asset(models.Model):
    assetName = models.CharField(max_length=128, unique=True)
    assetId = models.IntegerField(default=0)

    def __unicode__(self):
        return self.assetName

class Task(models.Model):
    taskDescription = models.CharField(max_length=128, unique=True)
    taskId = models.IntegerField(default=0)

    def __unicode__(self):
        return self.taskDescription

class Worker(models.Model):
    workerName = models.CharField(max_length=128, unique=True)
    workerId = models.IntegerField(default=0)

    def __unicode__(self):
        return self.workerName

class TaskAllocation(models.Model):
	_asset = models.ForeignKey(Asset, on_delete=models.PROTECT)
	_task = models.ForeignKey(Task, on_delete=models.PROTECT)
	_worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
	timeOfAllocation = models.DateTimeField(default=datetime.now, blank=True)
	taskToBePerformedBy = models.DateTimeField()
    #title = models.CharField(max_length=128)
    #url = models.URLField()
    #views = models.IntegerField(default=0)