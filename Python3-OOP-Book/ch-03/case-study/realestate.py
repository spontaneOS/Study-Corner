class Property:
    def __init__(self, square_feet='', beds = '', baths = '', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.numbeds = beds
        self.numbaths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.numbeds))
        print("bathrooms: {}".format(self.numbaths))

    def prompt_init():
        return dict(square_feet=input("Enter sqft: "), beds=input("Enter Beds: "), baths=input("Enter Baths: "))
    
    prompt_init = staticmethod(prompt_init)
    