# 0x11. Python - Network #1

## Resources
- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
- [Requests package](https://pypi.org/project/requests/)
- [GitHub API](https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28)

## General
>How to fetch internet resources with the Python package urllib
>
>How to decode urllib body response
>
>How to use the Python package requests #requestsiswaysimplerthanurllib
>
>How to make HTTP GET request
>
>How to make HTTP POST/PUT/etc. request
>
>How to fetch JSON resources
>
>How to manipulate data from an external service

## Tasks
0	Write a Python script that fetches https://alx-intranet.hbtn.io/status
> You must use the package urllib
>
> You are not allowed to import any packages other than urllib
>
> The body of the response must be displayed like the following example (tabulation before -)
>
> You must use a with statement

```
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
```


