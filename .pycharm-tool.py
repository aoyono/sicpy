#!/home/cris/WORKSPACE/python_virtual_envs/pycris/bin/python
# -*- coding: utf-8 -*-
"""
"""
import os
import re
import threading
from importlib import import_module

import click


def next_exercise(chapter, previous, page):
    url_tpl = 'https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-{page}.html#%_thm_{chapter}.{number}'
    filename_to_create = 'exercise{chapter}_{number}.py'
    subfolder = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'Chapter{}'.format(chapter),
        'exercises'
    )

    if not os.path.isdir(subfolder):
        os.mkdir(subfolder)
    exercise_number = previous + 1
    with open(os.path.join(subfolder, filename_to_create.format(chapter=chapter, number=exercise_number)), 'w') as fd:
        try:
            fd.writelines([
                '# -*- coding: utf-8 -*-\n',
                '"""\n',
                url_tpl.format(page=page, chapter=chapter, number=exercise_number),
                '\n"""\n',
                '\n',
                '\n',
                'def run_the_magic():\n',
                '    pass\n',
                '\n',
                '\n',
                'if __name__ == "__main__":\n',
                '    run_the_magic()\n',
                '\n'
            ])
        except:
            print('Failure : Could not write new file')
        else:
            print('Success')


def get_chapters(filename=''):
    if os.path.isabs(filename):
        yield os.path.basename(os.path.dirname(filename))
    else:
        with open('.chapters.txt', 'r') as fd:
            while True:
                l = fd.readline()
                if not l:
                    break
                yield l.strip()


def magic_work(filename):
    if os.path.exists(filename):
        module_name = os.path.basename(filename).split('.')[0]
        for chapter in get_chapters(filename=filename):
            try:
                module = import_module('.'.join((chapter.replace('/', '.'), module_name)))
            except ImportError:
                continue
            else:
                if hasattr(module, 'run_the_magic'):
                    click.echo('\nRunning {}'.format(filename))
                    click.echo('------------------[start]-------------------')
                    module.run_the_magic()
                    click.echo('-------------------[end]--------------------')
                break
    else:
        click.echo('File {} does not exist'.format(filename))


@click.group()
def master_command():
    pass


@master_command.command()
@click.argument('filename', type=click.STRING)
def run_the_magic(filename):
    magic_work(filename)


def run_in_threads(target):
    thread_list = [
        threading.Thread(
            target=target,
            args=(os.path.join(chapter, module_name),),
            name='.'.join((chapter.replace('/', '.'), module_name.replace('.py', '')))
        )
        for chapter in get_chapters()
        for module_name in filter(
            lambda x: all((
                not os.path.isdir(x), not x.endswith('.pyc'), not os.path.basename(x).startswith('.'),
                '__init__' not in x
            )),
            os.listdir(chapter)
        )
    ]
    for thread in thread_list:
        click.echo('start running thread {}'.format(thread.name))
        thread.start()

    for thread in thread_list:
        thread.join()
        click.echo('thread {} terminated'.format(thread.name))


@master_command.command()
def run_all_the_magic():
    run_in_threads(magic_work)


@master_command.command()
def build_rtm():
    def rtm_runner(filename):
        with open(filename, 'r') as fd:
            lines = fd.readlines()
        # Saving a copy of the data
        with open(os.path.join(os.path.dirname(filename), '.{}'.format(os.path.basename(filename))), 'w') as fd:
            fd.writelines(lines)
        if "if __name__ == '__main__':\n" in lines:
            if "def run_the_magic():\n" not in lines:
                lines[lines.index("if __name__ == '__main__':\n")] = "def run_the_magic():\n"
                lines.append('\n')
                lines.append('\n')
                lines.append("if __name__ == '__main__':\n")
                lines.append("    run_the_magic()\n")
                lines = list(map(
                    (
                        lambda line: line
                        if 'from __main__ import' not in line
                        else line.replace('__main__', '{}.{}'.format(os.path.basename(os.path.dirname(filename)),
                                                                     os.path.basename(filename).split('.')[0]))
                    ),
                    lines
                ))
                with open(filename, 'w') as fd:
                    fd.writelines(lines)

    run_in_threads(rtm_runner)


@master_command.command()
@click.argument('filename', type=click.STRING)
def create_next_exercise_file(filename):
    current_exercise_filename = filename
    match = re.match(r'^exercise(?P<chap_nb>[\d])_(?P<exo_nb>[\d]{1,2})\.py$', current_exercise_filename)
    if match:
        chapter = match.group('chap_nb')
        previous = int(match.group('exo_nb'))
        with open('Chapter{}/exercises/{}'.format(chapter, current_exercise_filename), 'r') as fd:
            line = fd.readline()
            while line:
                if line.startswith('http'):
                    break
                line = fd.readline()
            match = re.match(
                r'^https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-(?P<page>[\d]{1,3}).html'
                r'#%_thm_(?P<chapter>[\d]{1,3})\.(?P<number>[\d]{1,2})$',
                line
            )
            if match:
                chap = match.group('chapter')
                prev = int(match.group('number'))
                page = match.group('page')
                if chap == chapter and prev == previous:
                    next_exercise(chap, prev, page)
                else:
                    click.echo('Failure: Bad setup of previous file')
    else:
        click.echo('Failure: Bad file name')


if __name__ == '__main__':
    master_command()
