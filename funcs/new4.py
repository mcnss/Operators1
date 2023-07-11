def checkPassword(my_password):
    big_letters = 'ABCDERWQZXCVBNMKLJPOIUYGHFS'
    count_big_letters = 0
    if len(my_password) <= 5:
        return False
    for i in my_password:
        if i in big_letters:
            count_big_letters += 1
            if count_big_letters >= 2:
                return False
    return True


a = checkPassword('password123')
print(a)



