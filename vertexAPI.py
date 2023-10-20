# Aierken
# REST API for Chatbot in Vertex AI

import requests
import base64
import json
import apikeys as key

api_key = key.API_KEY
endpoint_url = key.ENDPOINT_URL
project_id = key.PROJECT_ID

# given the api_key, endpoint url and project id to ask the vertex AI chatbot question and it return the json format
def chatbison(API_KEY,ENDPOINT_URL,PROJECT_ID,userinput, chathistory):
    headers = {
        'Authorization': 'Bearer {}'.format(API_KEY),
        'Content-Type': 'application/json; charset=utf-8'
    }
    chathistory.append({"author": "user","content" : userinput})
    
    payload = {
        "instances": [{
            "context":  "My name is Ned. You are my personal assistant. My favorite movies are Lord of the Rings and Hobbit.",
            
            "messages":chathistory,
        
        }],
        'parameters': {
            "temperature": 0.3,
            "maxOutputTokens": 1000
        }
    }
       
    response = requests.post(ENDPOINT_URL, headers=headers, json=payload)
    # print(response.json())
    if response.status_code == 200:
        data = response.json()
        chathistory.append({"author": "bot","content" :  data['predictions'][0]['candidates'][0]['content']})
    else:
        print(f"Error: {response.status_code}")
    return response.json()


# vertex ai image caption rest api call return json 
def imageCaption(API_KEY,ENDPOINT_URL,PROJECT_ID,encoded_image):
    payload = {
    'instances': [
        {
            'image': {
                'bytesBase64Encoded': encoded_image
            }
        }
    ],
    'parameters': {
        'sampleCount': 3,
        'language': 'en' 
        }
    }

    headers = {
        'Authorization': 'Bearer {}'.format(API_KEY),
        'Content-Type': 'application/json; charset=utf-8'
    }

    response = requests.post(ENDPOINT_URL, headers=headers, json=payload)

    return response.json()
    
# vertex ai image visual Q&A api call return json
def ImageVisualQA(API_KEY,ENDPOINT_URL,PROJECT_ID,encoded_image,userinput):
    payload = {
    'instances': [
        {
            "prompt": userinput,
            'image': {
                'bytesBase64Encoded': encoded_image
            }
        }
        ],
        'parameters': {
            'sampleCount': 3,
            'language': 'en' 
        }
    }

    headers = {
        'Authorization': 'Bearer {}'.format(API_KEY),
        'Content-Type': 'application/json; charset=utf-8'
    }

    response = requests.post(ENDPOINT_URL, headers=headers, json=payload)

    return response.json()
    







# image load 
with open('dog_test.jpg', 'rb') as image_file:
    encoded_image_data = base64.b64encode(image_file.read()).decode('UTF-8')

print(imageCaption(key.API_KEY,
                   f'https://us-central1-aiplatform.googleapis.com/v1/projects/{key.PROJECT_ID}/locations/us-central1/publishers/google/models/imagetext:predict',
                   key.PROJECT_ID,
                   encoded_image=encoded_image_data))



# # image load 
# with open('dog_test.jpg', 'rb') as image_file:
#     encoded_image_data = base64.b64encode(image_file.read()).decode('UTF-8')

# print(ImageVisualQA(key.API_KEY,
#                    f'https://us-central1-aiplatform.googleapis.com/v1/projects/{key.PROJECT_ID}/locations/us-central1/publishers/google/models/imagetext:predict',
#                    key.PROJECT_ID,
#                    encoded_image=encoded_image_data,
#                    userinput="descript this image ?"))



# chat_history = []
# while True:
#     userinput = input("Your:")
#     chat_response = chatbison(key.API_KEY,
#                               f'https://us-central1-aiplatform.googleapis.com/v1/projects/{key.PROJECT_ID}/locations/us-central1/publishers/google/models/chat-bison:predict',
#                               key.PROJECT_ID,
#                               userinput, chat_history)
#     print(chat_response)
#     print("Bot:" + chat_response['predictions'][0]['candidates'][0]['content'])


