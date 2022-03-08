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

## Build the docker image
```
docker build -t python-test .
```
## Run the container
```
docker run -it --name python-container -p 3200:3200 python-test
```
## Now visit the host
http://192.168.1.76:3200/temp  

## Fill in information in correct format
I did not implement edge case checks for proper formatting.. I just wanted proper functionality 😅

## View results
View the image coordinates array! 
🐶 Hopefully you enjoy 😃

