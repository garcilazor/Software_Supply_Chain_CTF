while true
do 
    twine upload --repository aws package1/dist/*
    twine upload --repository aws package2/dist/*
    sleep 1000
done