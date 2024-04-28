import PyPDF2
import os

def ArrangeFiles(input_data,output_data=""):
    files= os.listdir(os.path.join(input_data[0]))

    for file in files:
        if(file.endswith('.pdf')):
            merger= PyPDF2.PdfMerger()
            for i in input_data:
                os.chdir(os.path.join(os.getcwd(),i))
                if(os.path.exists(file)):
                    merger.append(file)
                os.chdir(os.path.join(os.getcwd(),'..'))
            try:
                os.chdir(os.path.join(os.getcwd(),'output'))
            except:
                os.mkdir('output')
                os.chdir(os.path.join(os.getcwd(),'output'))                
            merger.write(output_data+file)
            os.chdir(os.path.join(os.getcwd(),'..'))                

            merger.close()
            merger=[]
        else:
            print("Files Must be PDF")


input_data= input('Enter Folder to Accept Data , Seperated: assignments,cover,questions: ').split(",")
output_data=input('Add Prefixs (Optional): ')

try:
    ArrangeFiles(input_data,output_data)
except: 
    print("Something Went Wrong")
    