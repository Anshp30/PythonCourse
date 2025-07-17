# f =open("ansh.txt","r")
# content = f.read()
# print(content)
# f.close()

with open("ansh.txt","r") as f: #context manager
    content = f.read()
    print(content)
    # No need to write f.close() because file is already close when using a with syntax.