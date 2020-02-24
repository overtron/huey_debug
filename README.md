# Huey Debug

This repo replicates an issue with the Hueyx library

## Replicate the issue
Run the following command from the root of the project (requires docker)

```shell script
docker-compose -f local.yml build && docker-compose -f local.yml up
```

## The issue

I'm unable to trigger tasks from the views.py file. Whenever I add this to

`from huey_debug.users.tasks import task1` to `huey_debug/users/views.py` I get the stacktrace below

```
huey-general-worker_1  | Traceback (most recent call last):
huey-general-worker_1  |   File "manage.py", line 30, in <module>
huey-general-worker_1  |     execute_from_command_line(sys.argv)
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/__init__.py", line 381, in execute_from_command_line
huey-general-worker_1  |     utility.execute()
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/__init__.py", line 375, in execute
huey-general-worker_1  |     self.fetch_command(subcommand).run_from_argv(self.argv)
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/base.py", line 323, in run_from_argv
huey-general-worker_1  |     self.execute(*args, **cmd_options)
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/django/core/management/base.py", line 364, in execute
huey-general-worker_1  |     output = self.handle(*args, **options)
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/hueyx/management/commands/run_hueyx.py", line 63, in handle
huey-general-worker_1  |     self.autodiscover()
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/hueyx/management/commands/run_hueyx.py", line 40, in autodiscover
huey-general-worker_1  |     imp.load_module(import_path, fp, path, description)
huey-general-worker_1  |   File "/usr/local/lib/python3.7/imp.py", line 234, in load_module
huey-general-worker_1  |     return load_source(name, filename, file)
huey-general-worker_1  |   File "/usr/local/lib/python3.7/imp.py", line 169, in load_source
huey-general-worker_1  |     module = _exec(spec, sys.modules[name])
huey-general-worker_1  |   File "<frozen importlib._bootstrap>", line 630, in _exec
huey-general-worker_1  |   File "<frozen importlib._bootstrap_external>", line 728, in exec_module
huey-general-worker_1  |   File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
huey-general-worker_1  |   File "/app/huey_debug/users/tasks.py", line 6, in <module>
huey-general-worker_1  |     @HUEY.task()
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/huey/api.py", line 169, in decorator
huey-general-worker_1  |     **kwargs)
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/huey/api.py", line 687, in __init__
huey-general-worker_1  |     self.huey._registry.register(self.task_class)
huey-general-worker_1  |   File "/usr/local/lib/python3.7/site-packages/huey/registry.py", line 24, in register
huey-general-worker_1  |     ' name= to register this task. "%s"' % task_str)
huey-general-worker_1  | ValueError: Attempting to register a task with the same identifier as existing task. Specify a different name= to register this task. "huey_debug.users.tasks.task1"
huey_debug_huey-general-worker_1 exited with code 1
```
