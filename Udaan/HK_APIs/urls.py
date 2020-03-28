from django.urls import path

from . import views

urlpatterns = [
    path('add_asset/',  views.add_asset,  name="add_asset"),
    path('add_asset_form/',  views.add_asset_form,  name="add_asset_form"),
    path('add_task/',  views.add_task,  name="add_task"),
    path('add_task_form/',  views.add_task_form,  name="add_task_form"),
    path('add_worker/',  views.add_worker,  name="add_worker"),
    path('add_worker_form/',  views.add_worker_form,  name="add_worker_form"),
    path('allocate_task/',  views.allocate_task,  name="allocate_task"),
    path('allocate_task_form/',  views.allocate_task_form,  name="allocate_task_form"),
    path('assets/all/',  views.assets_all,  name="assets_all"),
    path('debug/',  views.debug,  name="debug"),
    path('',  views.home,  name="home"),
    path('get-tasks-for-workers/<int:workerId>/', views.get_tasks_for_workers, name='get_tasks_for_workers'),
]