# imgurup

"imgurup", the commandline imgur uploader, was written for a very simple reason. I wanted to be able to upload images (usually screenshots, though not always - see [imgurscrot](https://github.com/0x27/imgurscrot) for my "take screenshot and upload" tool :D) to imgur without needing to open a web browser or whatever.

## Use
Put it somewhere in $PATH as an executable (chmod +x) file named "imgurup" and just do "imgurup /path/to/file" to upload the file in question.

## API keys needed
Get an API key from [api.imgur.com](https://api.imgur.com) and set the environmental variable "IMGUR_CLIENT_ID" to the client id you get. Just pick one of the anonymous tokens as I was not arsed linking screenshots 
to accounts just yet.

## Requirements
imgurup requires only standard python2 libraries, with the exception of the [requests](https://pypi.python.org/pypi/requests) module, as I was not arsed using urllib for the HTTP stuff.  
To install requests:
```
$ pip install requests
```

## Licence
Licenced under the [WTFPL](http://www.wtfpl.net/).

## computational cycles accepted for beer
If you want, throw bitcoins at 13wUj3ZMut6uJAZKgZ4jCGz6tfqRvUzRgj and I will spend them on beer to fuel further stuff liek this.

## Todo
* Multiple image upload (album creation)
* Tying it to imgur account
* Refactoring and stuff (maybe even PEP-8 compliance!!!)
* Replace requests stuff with stdlib only for fun
* pip-compatible setuputils setup.py stuff
