from app import add_user, count_users

def test_add_user():
    add_user("alice")
    assert count_users() >= 1
