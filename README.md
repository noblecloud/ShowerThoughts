# ShowerThoughts (WIP)
Display a random shower thought from /r/showerthoughts.  Best when paired with cowsay.

*Note: This will be a mess while I remember how to write proper python.*

## Install
Requires Python 3 and [Requests](http://docs.python-requests.org/en/master/) library.

```pip3 install requests```

## Usage
Running without aruments will display a random post from the cached database. 

```python3 shower_thoughts.py```

### Options

```python3 shower_thoughts.py (update|open|config)```

```update```  Update local database of shower thoughts

```open```   Open comments section of last post

```config``` Get or set config (not quite working yet)

##cowsay

`python3 shower_thoughts.py | cowsay`

``` 
 _________________________________________
/ I mostly use my driver's license to buy \
| stuff that impairs my ability to drive. |
|                                         |
\ -mozezus                                /
 ----------------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```