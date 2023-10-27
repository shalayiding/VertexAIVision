from flask import Flask, render_template, url_for, request, jsonify
import vertexAPI as vertexapi
import apikeys as apikey
import re


app = Flask(__name__, static_folder='static')

chat_history = []


def extract_image_url(message):
    pattern = r'https?://\S+\.(jpg|jpeg|png|gif)'
    result = re.search(pattern, message)
    if result:
        return result.group(0)
    return None



@app.route('/')
def load_index():
    return render_template('interface.html')
 
 
@app.route('/process', methods=['POST'])
def process():
    message = request.form.get('message')
    image_url = extract_image_url(message)
    context = "if some one ask you who are you, reply : Hi, I am AIIIII, not your personal assistan"
    if image_url != None :
        imagecaption_bot = vertexapi.imageCaption(apikey.API_KEY,
                                                  f"https://us-central1-aiplatform.googleapis.com/v1/projects/{apikey.PROJECT_ID}/locations/us-central1/publishers/google/models/imagetext:predict",
                                                  apikey.PROJECT_ID,
                                                  image_url)
        imageQA_bot = vertexapi.ImageVisualQA(apikey.API_KEY,
                                                  f'https://us-central1-aiplatform.googleapis.com/v1/projects/{apikey.PROJECT_ID}/locations/us-central1/publishers/google/models/imagetext:predict',
                                                  apikey.PROJECT_ID,
                                                  image_url,
                                                  message)
        imageOCR_bot = vertexapi.VertexAI_OCR(apikey.API_KEY,
                   f'https://vision.googleapis.com/v1/images:annotate',
                   apikey.PROJECT_ID,
                   image_url="https://gdoc.io/uploads/minimalist-menu-design-1-web-712x984.webp")
        
        print("Current data format ======================================================================")
        print(imagecaption_bot)
        print(imageQA_bot)
        
        # print(imageOCR_bot)
        
        imagecaption_raw = imagecaption_bot
        imageQA_raw = imageQA_bot
        imageOCR_raw = imageOCR_bot
        context += "When analyzing the image at the provided URL and responding to the upcoming question, please use the information I'm about to share as a reference,"
        context += "but I want you to decide which one to use and if you think your answer is better you can use that. I expect an answer with the insight of a professional UI/UX designer."
        context += "I will provide you with different sets of information regarding the image:"
        context +="Image captioning details, which offer three different predicted descriptions of the image."
        context +="Visual QA information that attempts to answer user questions about the image."
        context+="OCR data, which extracts the text present in the image"
        context +="This is the image captioning information about the image:"+str(imageQA_raw)
        context += "this is the visual Q&A information : " + str(imagecaption_raw)
        context +"Here is the OCR return for the image their text and location information :" + str(imageOCR_raw)
        
        
   
    
    chat_response = vertexapi.chatbison(apikey.API_KEY,
                              f'https://us-central1-aiplatform.googleapis.com/v1/projects/{apikey.PROJECT_ID}/locations/us-central1/publishers/google/models/chat-bison:predict',
                              apikey.PROJECT_ID,
                              message, chat_history,
                              context)
    
    print(chat_response)
    json_response = {
    'message': chat_response['predictions'][0]['candidates'][0]['content'],
    'status': 200
	}
    return jsonify(response=json_response)


# @app.route('/pdffile',methods=['POST'])
# def pdffile():
#     uploaded_file = request.files['myFileInput']

#     if uploaded_file:
#         # Save the uploaded file to a specific location (e.g., 'uploads' folder)
#         file_path = f"uploads/{uploaded_file.filename}"
#         uploaded_file.save(file_path)

#         # Print the file name for demonstration purposes
#         print("Uploaded File:", uploaded_file.filename)

#         return jsonify({'message': f'Successfully uploaded file: {uploaded_file.filename}', 'status': 200})

#     return jsonify({'message': 'No file uploaded', 'status': 400})





if __name__ == '__main__':
    app.run(debug = True)
    #  app.run(host='replace this message with ip', port=5000) 
