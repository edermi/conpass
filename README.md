# ConPass

**Disclaimer**: This is a personal fork. It is adapted to my needs and I won't give any support.

Python tool for continuous password spraying taking into account the password policy.

Associated blogposts
* English: https://en.hackndo.com/password-spraying-lockout/
* French: https://www.login-securite.com/2024/06/03/spray-passwords-avoid-lockouts/

## Installation

**conpass** works with python >= 3.7
Make sure to have `libldap2-dev` and `libsasl2-dev` installed on your kali

### pipx (Recommended)

```bash
pipx install .
```

### From source for development

```
pip install .
```

## Usage

**conpass** will get all domain users and try a list of password provided in a password file. When a user can be locked out, the tool will wait for the lockout reset period before trying another password.

```bash
conpass -d domain -u pixis -p P4ssw0rd -P /tmp/passwords.txt
```

All passwords and NT hashes provided in `/tmp/passwords.txt` will be added to a testing Queue, and will be tested against all users, whenever it is possible without locking users out.
