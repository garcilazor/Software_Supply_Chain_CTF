while true
do 
    twine upload --repository aws package1/dist/*
    twine upload --repository aws package2/dist/*
    twine upload --repository aws package3/dist/*
    twine upload --repository aws package4/dist/*
    sleep 1000
done
