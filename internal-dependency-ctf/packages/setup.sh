#!/bin/bash
while true
do 
    twine upload --skip-existing --repository aws package1/dist/* 
    twine upload --skip-existing --repository aws package2/dist/* 
    twine upload --skip-existing --repository aws package3/dist/* 
    twine upload --skip-existing --repository aws package4/dist/*
    sleep 1000
done
