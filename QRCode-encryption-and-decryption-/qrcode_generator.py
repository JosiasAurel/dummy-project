import qrcode

data = "Hello World"

file_name = "hello.png"

image = qrcode.make(data)

image.save(file_name)