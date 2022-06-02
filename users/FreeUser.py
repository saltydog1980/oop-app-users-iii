from users.User import User

class FreeUser(User):
    def post(self, post):
        if self.post_count == 0:
            User.post_dict[self.name][0] = post
            self.post_count += 1
        elif self.post_count == 2:
            print("Free users are limited to 2 posts ")
        else:
            User.post_dict[self.name][self.post_count] = post
            self.post_count += 1