from google import genai
from dotenv import load_dotenv
import os
import files 
import json
from pydantic import BaseModel
#this defines the scheme{https://ai.google.dev/gemini-api/docs/structured-output?lang=python#define_a_schema_with_a_type} for the output from the ai
class rule(BaseModel):
  file_name: str
  destination_folder: str



def get_response(files_list, GEMINI_API_KEY):
    
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents='''Organize these files into folders based on their type or purpose. For each file, provide a JSON with two fields: json_path and destination_folder. Use categories like Images, Documents, Audio, etc. Output only the JSON, '
        '''+files_list,
        config={
            'temperature': 0.1,
            'response_mime_type': 'application/json',
            'response_schema': list[rule]
        })
    return response.text




def dothething(source_dir, destination_dir,json_path):
    load_dotenv()
    files_list=str(files.list_files(source_dir))

    GEMINI_API_KEY = os.environ.get("API_KEY")
    response=get_response(files_list, GEMINI_API_KEY)
    
    print('response_type=',type(response),response)

    json_file= json.loads(response)
    if os.path.exists(json_path):
        print(f"The file '{json_path}' already exists. Deleting it...")
    os.remove(json_path)  # Delete the file

    
    files.organize_files(json_file,source_dir,destination_dir)
    with open(json_path, "w") as file:
        json.dump(json_file, file, indent=4)
    return True

