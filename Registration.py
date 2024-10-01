import sys
import json
from hashlib import md5
from urllib.parse import quote


if __name__ == "__main__":
    # python Registration.py ā actor ā username ā email ā biography
    user_input = [i.strip() for i in " ".join(sys.argv[1:]).split("ā")[1:]]
    user_input = [i for i in user_input if i != ""]
    if len(user_input) != 4:
        sys.exit(1)
    actor, username, email, biography = user_input
    print(actor, username, email, biography)

    with open("./users.json", "r") as f:
        users_data: dict = json.load(f)

    username_md5 = md5(username.encode()).hexdigest()
    if username_md5 in users_data.keys():
        sys.exit(2)
    else:
        users_data["Users"][username_md5] = {
            "Github-Actor": actor,
            "Username": username,
            "Email-Address": quote(email),
            "User-Biography": biography,
        }

    with open("./users.json", "w") as f:
        f.write(json.dumps(users_data, ensure_ascii=False, indent=4))

    sys.exit(0)
