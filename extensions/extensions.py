name = input("File name: ").strip().lower()
if('gif' in name):
        print("image/gif")
elif('png' in name):
        print("image/png")
elif('jpg' in name or 'jpeg' in name):
        print("image/jpeg")

elif('pdf' in name):
        print("application/pdf")
elif('zip' in name):
        print("application/zip")
elif ('txt' in name):
    print("text/plain")
else:
    print("application/octet-stream")