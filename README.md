# coding-task
### You can see the calculator app by visiting:  
https://q-beyond-calculator.herokuapp.com/

### Task description:
I created a simple flask app that accepts JSON inputs and gives JSON outputs.  
The expected JSON format is:  
```
{
  "input1": 2,
  "input2": 3,
  "operator":"+"
}
```
Where:  
| key | valid value |
| :-: | :-: |
| input1 | any number |
| input2 | any number |
| operator | any one of "+", "-", "*", "/" |


#### Note
The app doesn't have any validations, error handling or authorization in place.  
Providing anything other than the allowed values will result in _Internal Server Error_.

To run Docker images you need to install Docker in your machine.
    Follow instructions in [Download and install](https://docs.docker.com/desktop/) section.

## Run Docker image from:
### Git repository
1. To build Docker image:  
    `docker build -t flask-test:latest .`
2. To run Docker image on your machine:  
    `docker run -d -p 5000:5000 flask-test`
3. App will be accessible using url:  
    http://127.0.0.1:5000/

### Docker Hub repository:
1. To run Docker image on your machine:  
    `docker run -d -p 5000:5000  leamone/codingtask:first`
2. App will be accessible using url:   
    http://127.0.0.1:5000/
