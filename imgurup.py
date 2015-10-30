#!/usr/bin/python2
# coding: utf-8
# Author: David Davidson
# Twitter: @dailydavedavids
# Licence: WTFPL
# Version: 20150731.1
from __future__ import print_function, unicode_literals
import requests
import base64
import json
import sys
import os


def upload(image_path, client_id):
    try:
        f = open(image_path, "rb")  # open file for reading, binary mode
    # I should do something with the exception.
    # Later I will add logging for these
    except Exception:
        sys.exit("{!} That file does not exist!")  # for now, just bail
    # base64 encode the image data
    b64image = base64.standard_b64encode(f.read())
    # set the client id in auth header
    headers = {'Authorization': 'Client-ID ' + client_id}
    # make post data
    data = {'image': b64image,
            'title': '{}'.format(os.path.basename(image_path))}
    try:
        # send request
        r = requests.post(url="https://api.imgur.com/3/upload.json",
                          data=data, headers=headers)
    except Exception as e:  # catch the exception if something goes wrong
        # bail.
        print("{-} Image Upload Failed. Printing stack trace and exiting...")
        # print the stacktrace.
        # Later, I should figure out what kind of exceptions happen
        # and handle them and log them
        sys.exit(str(e))
    lol = json.loads(r.text)  # get the json...
    print(lol['data']['link'])  # print the link
    return lol['data']


def upload_album(directory, client_id):
    if not os.path.isdir(directory):
        sys.exit('{!} "%s" does not exist. '
                 'Please enter an existing directory' % directory)
    extensions = ['.png', '.jpg', '.gif', '.bmp', '.tif', '.jpeg']
    images = ''
    # directory path without the trailing '/' is still a valid path, accept it
    if not directory.endswith('/'):
        directory += '/'

    for dir_file in os.listdir(directory):
        # only get images
        if any(dir_file.endswith(extension) for extension in extensions):
            # ids must be delineated with commas in order to send to album api
            images += upload(directory + dir_file, client_id)['id'] + ','
    headers = {'Authorization': 'Client-ID ' + client_id}
    # removing trailing comma
    images = images[:-1]
    data = {'ids': images,
            'title': '{}'.format(directory)}
    try:
        r = requests.post(url='https://api.imgur.com/3/album.json',
                          data=data, headers=headers)
    except Exception as e:
        print('{-} Album upload failed.')
        sys.exit(str(e))
    result = json.loads(r.text)
    print('Album link:\nhttp://i.imgur.com/a/' + result['data']['id'])


def main(args):
    # some of the logic in here is a bit backwards.
    # I should probably fix this to make it more nice
    if len(args) != 3:  # only 2 args needed
        # exit with usage
        sys.exit("use: {} /path/to/image/file.ext -i/-a".format(args[0]))
    else:
        pass  # we can continue
    client_id_env_var = 'IMGUR_CLIENT_ID'
    if client_id_env_var in os.environ.keys():  # check if env var exist
        client_id = os.environ[client_id_env_var]  # get it and save it
    else:
        sys.exit("{!} Set environmental variable IMGUR_CLIENT_ID"
                 " to your client_id :)")
    if args[2] == '-i':
        upload(image_path=args[1], client_id=client_id)
    elif args[2] == '-a':
        upload_album(args[1], client_id=client_id)
    else:
        print('Error: Invalid argument "%s" \n'
              'Use "-i" to upload an image or '
              '"-a" to upload the given directory to an album' % args[2])


if __name__ == "__main__":
    main(args=sys.argv)
