#!/bin/sh

# get the new name of the exercise directory

newdir=$(echo *.zip | grep -E -o '\d{3}')

# make and cd into the new dir

mkdir $newdir && cd $newdir

# unzip the python files to here

unzip ../*.zip "*.py"

# clean up

rm ../*.zip

# a commit message
# msg="submission Bite $newdir @ codechalleng.es"

