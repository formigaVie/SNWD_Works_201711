import example_2_methods as CLASS


def check_get_younger():

    age = 12
    test_guy = CLASS.human(age, "jeremy")
    test_guy.getyounger()

    assert test_guy.age == age-2

if __name__ == '__main__':
    check_get_younger()
    print "Tests passed full"

    #add tests fuer andere Tests in diesem File