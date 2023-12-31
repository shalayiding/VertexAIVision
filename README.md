# Project: Vertex AI Integration with Flask

This project is a web application using Python Flask as the backend and HTML, CSS, and JavaScript for the frontend. 
It integrates with Google Cloud's Vertex AI services through three different API calls( REST format).
The goal of the project is to help the chatbot understand the image and give feed back according to image.

## Features:

- **Backend powered by Flask.**
- **Sleek and responsive frontend using HTML, CSS, and JS.**
- **Integration with three different Vertex AI API calls.**
- **Utilizes several Python libraries such as Flask, Requests, etc.**

## Pre-requisites:

1. **Python 3**
2. **The following Python libraries:**
   - Flask
   - Requests
   (You can install them using pip: `pip install Flask requests`)
3. **Google Cloud's Vertex AI account** and the necessary permissions to make API calls.

## Setup:

1. **Clone the repository.**
```
git clone https://github.com/shalayiding/VertexAIVision.git
```

```
cd VertexAIVison
```


2. **Setup API.** 

Ensure you have a file named `apikeys.py` in the root directory of the project. This file should contain your Vertex AI authentication token and the project ID. The format should be:

```python
PROJECT_ID = 'YOUR_VERTEX_AI_PROJECT_ID'
API_KEY = 'YOUR_VERTEX_AI_AUTH_TOKEN'
```

2. **Install the necessary Python packages.** 

```
pip install -r requirements.txt
```

3.**Run the program.**

```
python3 main.py
```
Your server will start, and you can access the application in your web browser through the displayed URL (typically http://127.0.0.1:5000/).


## Contributing:
We welcome contributions! If you're interested in improving the project or adding new features, please make sure to follow the general coding conventions of the project and submit a pull request.



## Application Demo
Bot answering question with given web application design image:

![alt text](/IMAGES/interface.png)

![alt text](/IMAGES/interface2.PNG)


Bot returning Highlighted code :

![alt text](/IMAGES/interface3.PNG)

