# writing on files
print("printing for the first time")
with open("test2.txt", "w") as f: # if you choose a file that alrady exists, it will be overwritten
    f.write("Hello World")

print("printing for the second time")
with open("test2.txt", "w") as f: # if you choose a file that alrady exists, it will be overwritten
    f.write("Hello World")

# the first hello world will be over written

    # use "a" to append instead of overwriting. 
with open("test2.txt", "a") as f: # if you choose a file that alrady exists, it will be overwritten
    f.write("\nHello Again!")

# writing files using seek():
print("\nwriting files using seek()")
with open("tests3.txt" , 'w') as f:
    f.write("Test")
    f.seek(0)
    f.write('R') # will only overwrite T in test. Test becomes --> Rest


# reading and writing multiple files
with open("test.txt", "r") as rf: # rf --> read file
    with open("test_copy.txt", "w") as wf: # wf --> write file
        for line in rf:
            wf.write(line) # this will copy the contents of test.txt to test_copy.txt
            

# working with images:
with open("image.jpeg", "rb") as rf: # rb --> read binary
    with open("image_copy.jpeg", "wb") as wf: # wb --> write binary
        for line in rf:
            wf.write(line)

# writing images in chunks:
# with open("image.jpeg", "rb") as rf: # rb --> read binary
#     with open("image_copy.jpeg", "wb") as wf: # wb --> write binary
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)  
