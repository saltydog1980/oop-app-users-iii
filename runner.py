
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

bob = PremiumUser('Bob', 42, '(123)-222-4444', 'bob@mail.com', 'Premium')
cindy = FreeUser('Cindy', 55, '(123)-222-4444', 'cindy@mail.com', 'Free')
# tim = User('Tim', 32, '(123)-222-4444', 'tim@mail.com')
# chuck = User('Chuck', 59, '(123)-222-4444', 'chuck@mail.com')

print(bob.user_type)
# tim.post("I love this ability in the new app")
bob.post("YIPEE kiyay MF")
# tim.post("this really is the stuff")
# tim.post_del(0)
# print(User.post_dict)
# tim.post_get(1)
bob.post_get(0)
cindy.post("first post")
cindy.post("second post")
cindy.post("third Post")
print(PremiumUser.post_dict)











