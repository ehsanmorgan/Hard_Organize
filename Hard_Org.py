import os
import shutil



current_forder = os.path.dirname(__file__)



for filename in os.listdir(current_forder):
    if filename.endswith((".jpg" , "PNG" , "HEIC")):
        if not os.path.exists("images"):
            os.mkdir("images")
        shutil.copy((filename), "images")
        os.remove(filename)
        print('Done')
    
    
for filename in os.listdir(current_forder):
    if filename.endswith((".MP4","mov")):
        if not os.path.exists("viedos"):
            os.mkdir("viedos")
        shutil.copy((filename), "viedos")
        os.remove(filename)
        print('Done')
        
        
for filename in os.listdir(current_forder):
    if filename.endswith((".doc","docx")):
        if not os.path.exists("docs"):
            os.mkdir("docs")
        shutil.copy((filename), "docs")
        os.remove(filename)
        print('Done')