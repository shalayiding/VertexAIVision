import requests
import apikeys as key
# Define your API token and file ID
FILE_ID = 'G7TeLujPsJHPt13GSxxwFM'

# Set up the headers with the API token
headers = {
    'X-Figma-Token': key.FIGMA_API_KEY
}

# Make the API call
response = requests.get(f'https://api.figma.com/v1/files/{FILE_ID}', headers=headers)

# # Print the JSON response
all_child_document = []
for child_document in response.json()['document']['children']:
       all_child_document.append(child_document)
    

all_child_mobi_ui  = all_child_document[1]
for child_mobi_ui in all_child_mobi_ui['children']:
    if child_mobi_ui['name'] == 'Profile/Posts':
        target = child_mobi_ui      
        break

print(target)
target_img_list = []
for t_child in target['children']:
    target_img_list.append(t_child['id'])
       
       
# print(response.json()['document']['children'][2])
# for child in 
IMAGE_ID = '151:546'
for i in target_img_list:
    image_response = requests.get(f'https://api.figma.com/v1/images/{FILE_ID}?ids={i}',headers=headers)
    print(image_response.json())