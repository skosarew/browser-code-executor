from django.shortcuts import render
from .models import UserForm
from threading import Thread


import subprocess as sub
import os
import sys


def execute(command, directory):
    os.chdir(directory)
    working_dir = sys.stdout
    p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = p.communicate()
    os.chdir(working_dir)
    return output, errors


def start_new_thread(function):
    def decorator(*args, **kwargs):
        t = Thread(target = function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator



def forma(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        userform.stopped = False
        if userform.is_valid() and not userform.stopped:
            # print('valid!')
            code = userform.cleaned_data['user_code']
            input_console = userform.cleaned_data['code_console']
            input_gen = (x for x in input_console.splitlines())

            def input(*x):
                if x:
                    print(x)
                res = next(input_gen)
                return res

            old_stdout = sys.stdout
            old_stderr = sys.stderr

            try:
                sys.stdout = open('out.txt', 'w')
                sys.stderr = open('err.txt', 'w')
                exec(code)

            except Exception as ex:
                print(ex, file=sys.stderr)
            finally:
                sys.stdout.close()  # close out.txt
                sys.stderr.close()  # close err.txt
                sys.stdout = old_stdout
                sys.stderr = old_stderr

            with open('out.txt') as out:
                out_ans = out.read()
                print(len(out_ans.splitlines()))
            with open('err.txt') as e:
                out_err = e.read()

            return render(request, "executor/forma.html",
                          {"form": userform, 'out_ans': out_ans,
                           'out_err': out_err})
        else:
            print('form is not valid')
    else:
        userform = UserForm()
        return render(request, "executor/forma.html", {"form": userform})
