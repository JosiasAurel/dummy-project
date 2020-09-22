import mammoth
 
file = open("your_file_name.docx", 'rb')
b = open('converted.html', 'wb')
document = mammoth.convert_to_html(file)
b.write(document.value.encode('utf8'))
file.close()
b.close()
 
'''instructions :
   //change "your_file_name" to 
   //the file to be converted
   // with *.docx extension
   //place program in the 
   // directory containing your
   // *.docx file and run it
   // the output file is an html
   // file
   
'''
