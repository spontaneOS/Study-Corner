class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("Test of sending order '{}' to '{}'.".format(order, self.name))

c = Contact("Someone", "someone@a.com")
s = Supplier("Merchant", "merchant@b.com")

print(c.name, c.email, s.name, s.email)
# c.order("Order #1") # This will result in error.

s.order("Order #1") # method working in inherited class

c1 = Contact("User A", "a@xyz.com")
c2 = Contact("B", "b@xyz.com")
c3 = Contact("User C", "c@xyz.com")

l = [c.name for c in Contact.all_contacts.search("User")]
print(l)
