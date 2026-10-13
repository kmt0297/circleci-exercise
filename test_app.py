from app import add_user, count_users, get_conn

def test_add_user_saves_the_name():
    add_user("alice")
    with get_conn() as c:
        rows = c.execute("SELECT name FROM users").fetchall()
    assert rows == [("alice",)]      # exactly one row, and it's "alice"
    assert count_users() == 1        # exactly 1, not "1 or more"
