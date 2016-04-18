# Run script to create repository in github
file=$(git --no-pager diff HEAD~1 --name-only -- `find . -iname *.yml`)

python create.py -p $file -o "vengatlnx"
