# -*- coding:utf-8 -*-
from fabric.api import run, env, cd, local
from fabric.colors import green
import config

env.hosts = config.evn['hosts']
env.password = config.evn['password']

inter_path = '/home/ubuntu/django_inter/bin/'
app_path = '/home/ubuntu/jiu_school_back_end/'
host = '0.0.0.0:8000'

def update():
    local('git push', capture=False, shell=None)
    with cd(app_path):
        try:
            run('pkill python')
        finally:
            run('git pull')
            run(inter_path + 'pip install' + ' -r requirement.txt')
            run(inter_path + 'python '  + app_path + 'src/manage.py' + ' migrate')
            run('nohup ' + inter_path + 'python '  + app_path + 'src/manage.py' +' runserver ' + host)
