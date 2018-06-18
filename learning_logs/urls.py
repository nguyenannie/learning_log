"""Define URL patterns for learning_logs"""

"""Defines url patterns for learning_logs."""

from django.urls import path, re_path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    #Show all topics.
    path('topics', views.topics, name='topics'),

    #Detail page for a single topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #Page for adding new topic
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),

    #Page for adding new Entry
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #Page for edditing an Entry
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]