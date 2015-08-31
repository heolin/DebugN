#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys, re
import argparse
import socket
import urllib
import datetime

backlog = 5
size = 1024


def run(port, file_path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", port))
    s.listen(backlog)
    print "Server is running at: {}".format(port)
    while 1:
        client, address = s.accept()
        data = client.recv(size)
        if data:
            for d in data.split('\n'):
                if "LOG" not in d:
                    continue
                print urllib.unquote(d.replace('+', ' '))
            client.send('HTTP/1.1\n\n 200 OK Content-Type: text/html')
            client.close()
            output_file = open(file_path, 'a')
            output_file.write(data+"\n")
            output_file.close()

        client.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port for HTTP server.", default=50000)
    parser.add_argument("-f", "--file", help="Path to output file.")

    args = parser.parse_args(sys.argv[1:])

    if args.file:
        output_path = args.file
    else:
        output_path = "data.log"

    run(args.port, output_path)

if __name__ == "__main__":
    main()