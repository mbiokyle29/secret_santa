# secret_santa

This module handles picking secret santas for a group of people
who can't draw names from a hat, it also handles the issue
of couples not wanting to get eachother.

## Setup

A few things are needed to get up and running.

1. A gmail account to connect to google smtp and send the results emails. You will also want to follow this [link](https://www.google.com/settings/security/lesssecureapps) to enable remote smtp logins for your gmail account.
2. A `local_settings.py` file with the following constants defined: `SANTA_EMAIL` and `SANTA_PASSWORD` as the email and password for the above account
3. A "couples" file, which is a tab delimited file of couples, one per line. It seems to work with having a couple of one person, but your mileage my vary on that.
4. An "emails" file, which is also tab delimited. Each line must have 2 and only two elements, first a name (which maps back to a person in the couples file) and then an email

## Running

simply run:
```
python -c /path/to/your/couples.tsv -e /path/to/your/emails.tsv
```