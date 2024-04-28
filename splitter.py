import PyPDF2
import os

# 1,10, 10, 
# 1- 20

file= input("Enter File Name like Myfile: ")
filename=file if file.endswith(".pdf") else file+".pdf"
fileData=PyPDF2.PdfReader(open(filename,'rb'))
output= PyPDF2.PdfWriter()
text= input('Enter Page Range Eg. 1-5 1 2,5: ')
if(text.find(",")>=0):
    sample=text.split(",")
    try:
        for num in sample:
            output.add_page(fileData.pages[int(num)-1])
            with open('output.pdf','wb') as f:
                output.write(f)
    except IndexError:
        print("Invalid Page Number Found ")
    except ValueError:
        print("Suspicious Value Found")
    except Exception:
        print("Couldn't Process")

# 1-10 
elif(text.find("-")>=0):
    sample=text.split("-")
    try:
        for num in range(int(sample[0]),int(sample[1])+1):
            output.add_page(fileData.pages[int(num)-1])
            with open('output.pdf','wb') as f:
                output.write(f)
    except IndexError:
        print("Invalid Page Number Found ")
    except ValueError:
        print("Suspicious Value Found")
    except Exception as e:
        print("Couldn't Process"+e)

    
