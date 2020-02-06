from django.shortcuts import render
from .forms import UserForm
from .exceptions import Deprecated
from subprocess import Popen, PIPE, TimeoutExpired
from django.conf import settings

timeout_django = settings.TIMEOUT
save_exec_code = \
"""
from django.conf import settings
try:
    import os
    del os
    import sys
    sys.modules['os'] = None
except:
    pass
 
import sys
sys.path.append("/home/app/web/executor/")
from exceptions import Deprecated

def deprecated_func(func_name):
    raise Deprecated()

exec = lambda *x: deprecated_func('`exec`')
eval = lambda *x: deprecated_func('`eval`')
open = lambda *x, **y: deprecated_func('`open`')
"""

def start(code, code_input, timeout):

    final_code = save_exec_code + code
    process = Popen(['python3', '-c', final_code], stdin=PIPE, stdout=PIPE,
                    stderr=PIPE, encoding='utf-8')

    try:
        out, err = process.communicate(input=code_input, timeout=timeout)
    except TimeoutExpired:
        return '', 'Time out!'
    except Deprecated:
        return '', 'Deprecated'
    return out, err


def python_executor(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            code = userform.cleaned_data['user_code']
            input_console = userform.cleaned_data['code_console']
            timeout_form = userform.cleaned_data['timeout']
            if timeout_form:
                try:
                    timeout_form = float(timeout_form)
                except ValueError:
                    return render(request, "executor/python_executor.html",
                                  {"form": userform, 'out_ans': '',
                                   'out_err': 'Incorrect timeout'})
                if timeout_form > timeout_django:
                    return render(request, "executor/python_executor.html",
                                  {"form": userform, 'out_ans': '',
                                   'out_err': 'Timeout is greater than '
                                              'was settled in config'})
            timeout = timeout_form or timeout_django
            out_ans, out_err = start(code, input_console, timeout)
            return render(request, "executor/python_executor.html",
                          {"form": userform, 'out_ans': out_ans,
                           'out_err': out_err})
        else:
            return render(request, "executor/python_executor.html",
                          {"form": userform, 'out_ans': '',
                           'out_err': 'Some error'})
    else:
        userform = UserForm()
        return render(request, "executor/python_executor.html", {"form": userform})
