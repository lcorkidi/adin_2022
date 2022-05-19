#!/bin/bash -i
# source this file to setup your shell terminal
# The -i flag in the shebang comes from this awesome answer: 
# https://stackoverflow.com/questions/55507519/python-activate-conda-env-through-shell-script
# Allow async operations for notebook. lyh53 answer: 
# https://stackoverflow.com/questions/61926359/django-synchronousonlyoperation-you-cannot-call-this-from-an-async-context-u

conda activate --stack django

# Project paths
export BASEDIR='~/projects/github/adin_2022' # can be better
export APPNAME='adin'
export APPDIR=${BASEDIR}/code
export DOCSDIR=${BASEDIR}/docs

# Devtools
export DEVDIR=${BASEDIR}/dev
export DJANGO_ALLOW_ASYNC_UNSAFE=True
export PATH=$PATH:${APPDIR}:${DEVDIR}/scripts

chmod u=rwx ${DEVDIR}/scripts/*.sh

alias start_shell='start_shell.sh'
alias reset_all='reset_all.sh'
alias build_docs='build_docs.sh'

# Enter django codebase
cd $APPDIR
