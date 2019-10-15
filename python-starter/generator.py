class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

hsbc = Bank()
corner_street_atm = hsbc.create_atm()
print(next(corner_street_atm))




# def multi_yield():
#      yield_str = "This will print the first string"
#      yield yield_str
#      yield_str = "This will print the second string"
#      yield yield_str

# multi_obj = multi_yield()
# while True:
#     try:
#         print(next(multi_obj))
#     except StopIteration:
#         print("Exception, Yeild finish")
#         break

