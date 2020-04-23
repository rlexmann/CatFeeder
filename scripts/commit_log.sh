#!/bin/sh

cd $HOME/CatFeeder
git pull
cp $HOME/catfeeder.log ./feeding.log
cp ./README.template ./README.md
cat feeding.log >> README.md
git add feeding.log README.md
git commit -m "Log update."
git push
