# ShowerThoughts
Display a random shower thought from /r/showerthoughts.  Best when paired with cowsay.

Not limited to just /r/showerthoughts.  Use `config subreddit newsub` to change to a new subreddit.

Example: `python3 shower_thoughts.py config subreddit LifeProTips`


*Note: This will be a mess while I remember how to write proper python.*

## TODO

- Change the name
- Add proper login support with voting

## Install
Requires Python 3, [Requests](http://docs.python-requests.org/en/master/) and [docopt](https://github.com/docopt/docopt).

```pip3 install requests docopt```

## Usage
Running without aruments will display a random post from the cached database. 

```python3 shower_thoughts.py```

### Options

```python3 shower_thoughts.py (update|open|config)```

```update```  Update local database of shower thoughts

```open```   Open comments section of last post

```config``` Get or set config `sort|limit|timeframe|subreddit`

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