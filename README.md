# passwd-parser
This utility parses the UNIX /etc/passwd and /etc/group files and combines the data into a single json output. It is a toy treated as a real utility program that could be run in a cron job.
## Getting Started
The output is a json object where each key is a username and each value is an object containing the field “uid”, “full_name”, and “groups”. Groups contain a list of all groups the user is a member of.
### Prerequisites
Be sure you have the latest Python 3 on your UNIX-like system.
### Installing
From source:
```
$ git clone https://github.com/anleo6/passwd-parser.git && cd passwd-parser
```
Use pip or pip3:
```sh
$ sudo pip3 install .
```
To uninstall:
```sh
$ sudo pip3 uninstall passwd-parser
```
### Usage
You can just run:
```sh
$ passwd-parser
```
and see the data from your local /etc/passwd and /etc/group files:
```sh
$ passwd-parser
{
    "sshd": {
        "uid": "112",
        "full_name": "",
        "groups": []
    },
    "root": {
        "uid": "0",
        "full_name": "root",
        "groups": []
    },
    "sync": {
        "uid": "4",
        "full_name": "sync",
        "groups": []
    },
    "daemon": {
        "uid": "1",
        "full_name": "daemon",
        "groups": []
    }, ...,
}
```
If you want to parse other passwd and group files you can use -p and -g to enter custom paths:
```sh
$ passwd-parser -p "path/to/passwd" -g "path/to/group"
```
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
