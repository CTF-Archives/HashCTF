import sys
import json
import uuid
from hashlib import md5


if __name__ == "__main__":
    # python Registration.py actor username email biography
    if len(sys.argv) != 5:
        sys.exit(1)
    actor, username, email, biography = sys.argv[1:]
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
            "Email-Address": email,
            "User-Biography": biography,
        }

    with open("./users.json", "w") as f:
        f.write(json.dumps(users_data, ensure_ascii=False, indent=4))

    sys.exit(0)
