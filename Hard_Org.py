import os
import shutil



current_forder = os.path.dirname(__file__)



for filename in os.listdir(current_forder):
    if filename.endswith((".jpg" , "PNG" , "HEIC" , "heic" , "jpeg" , "png" , "JPG")):
        if not os.path.exists("images"):
            os.mkdir("images")
        shutil.copy((filename), "images")
        os.remove(filename)
        print(' images Done')
    
    
for filename in os.listdir(current_forder):
    if filename.endswith((".MP4","mov" , "MOV" , "mp4")):
        if not os.path.exists("viedos"):
            os.mkdir("viedos")
        shutil.copy((filename), "viedos")
        os.remove(filename)
        print(' viedos Done')
        
        
for filename in os.listdir(current_forder):
    if filename.endswith((".doc","docx" , "pdf" , "pptx" , "pkg" , "ppt" , "exe" , "PDF" , "txt" , "dmg" , "zip" ,"csv" ,"odt" , "rtf" , "rar" )):
        if not os.path.exists("docs"):
            os.mkdir("docs")
        shutil.copy((filename), "docs")
        os.remove(filename)
        print(' docs Done')
        
        
for filename in os.listdir(current_forder):
    if filename.endswith((".html" , "svg" , "js" , "css" )):
        if not os.path.exists("vs_code"):
            os.mkdir("vs_code")
        shutil.copy((filename), "vs_code")
        os.remove(filename)
        print(' vs_code Done')
        

