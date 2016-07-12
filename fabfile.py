# -*- coding:utf-8 -*-
from fabric.api import run, env, cd, local
from fabric.colors import green
import config

env.hosts = config.evn['hosts']
env.password = config.evn['password']
git_host = config.evn['git_host']

inter_path = '/home/ubuntu/django_inter/bin/'
app_path = '/home/ubuntu/jiu_school_back_end/'
host = '0.0.0.0:8000'

def update(drop_data=None):
    local('git push', capture=False, shell=None)
    with cd(app_path):
        try:
            run('pkill python')
        finally:
            run('git pull ' + git_host)
            if drop_data is not None:
                run('mysql -u root')
            run(inter_path + 'pip install' + ' -r requirement.txt')
            run(inter_path + 'python '  + app_path + 'src/manage.py' + ' migrate')
            if drop_data is not None:
                run(inter_path + 'python '  + app_path + 'src/manage.py' + ' test')
            run('nohup ' + inter_path + 'python '  + app_path + 'src/manage.py' +' runserver ' + host)
