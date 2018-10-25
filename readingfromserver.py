#!/usr/bin/python
import urllib2
import json
contents = urllib2.urlopen("http://35.242.150.40:9000/info.json").read()
json_contents = json.loads(contents)
print(json_contents["host_name"])