
class User:
    # dicto log user posts
    post_dict = {}
    #added a post count to keep track of user post numbers and initialized each users
    # dict when they are added to the class
    def __init__(self, name, age, phone_number, email_address, user_type):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email_address = email_address
        self.user_type = user_type
        self.post_count = 0
        User.post_dict[self.name] = {}

    def post_get(self, post_num):
        print(f"{self.name} said \"{User.post_dict[self.name][post_num]}\"")
    
    def post(self, post):
        if self.post_count == 0:
            User.post_dict[self.name][0] = post
            self.post_count += 1
        else:
            User.post_dict[self.name][self.post_count] = post
            self.post_count += 1

    def post_del(self, post_num):
        del User.post_dict[self.name][post_num]

## Requirements
# 1. Your `User` class will now become a base class.
# 2. Create two subclasses `PremiumUser` and `FreeUser` that will inherit from `User`.
# 3. Override the `add_post` method for `FreeUser` so that an instance of `FreeUser` is only able to make two posts.
# 4. In the `runner.py` file, import `FreeUser` and `PremiumUser` and create at least one instance of each.
# 5. Add tests.

# class PremiumUser(User):
#     pass

# class FreeUser(User):

#     def post(self, post):
#         if self.post_count == 0:
#             User.post_dict[self.name][0] = post
#             self.post_count += 1
#         elif self.post_count == 2:
#             print("Free users are limited to 2 posts ")
#         else:
#             User.post_dict[self.name][self.post_count] = post
#             self.post_count += 1

# bob = PremiumUser('Bob', 42, '(123)-222-4444', 'bob@mail.com', 'PremiumUser')
# cindy = FreeUser('Cindy', 55, '(123)-222-4444', 'cindy@mail.com')
# # tim = User('Tim', 32, '(123)-222-4444', 'tim@mail.com')
# # chuck = User('Chuck', 59, '(123)-222-4444', 'chuck@mail.com')


# # tim.post("I love this ability in the new app")
# # bob.post("YIPEE kiyay MF")
# # tim.post("this really is the stuff")
# # tim.post_del(0)
# # print(User.post_dict)
# # tim.post_get(1)
# # bob.post_get(0)
# print(bob.PremiumUser)