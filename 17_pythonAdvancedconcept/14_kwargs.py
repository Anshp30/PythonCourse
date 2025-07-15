def marks(**kwargs):
    # kwargs is dictionary with all the key value pair which were   passed it marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(sujal=34,ansh=54,jack=65,marie=45)