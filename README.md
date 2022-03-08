# fetchMLE
project for MLE apprenticeship

## file structure
fetch /  
|---Dockerfile : contains docker image info  
|---pixelcoords.py : script that solves the problem (generate even coordinates from dimensions and corners)  
|---reqs.txt : requirements needed for environment  
|---templates /  
|------index.html : webpage structure  

# How to run

## Navigate to proper directory
Navigate to fetch directory (using command line) wherever you have downloaded the zip. Once there you can begin!

## Build the docker image
```
docker build -t python-test .
```
## Run the container
```
docker run -it --name python-container -p 3200:3200 python-test
```
You can verify that its running by 
```
docker ps -a
```

## Now visit the host
http://192.168.1.76:3200/temp  

## Fill in information in correct format
I implemented checks for proper length of dimensions tuple and corner list of tuples 😅 It will crash if there is other improper input!
![Website](/webpage.png)  

## View results
View the image coordinates array! 
![Results](/answer.png)  
🐶 Hopefully you enjoy 😃

