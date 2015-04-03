#!/usr/bin/python
from scapy.all import *

def http_header(packet):
    #http_packet=str(packet)
    #return packet.getlayer(Raw)
    
    #load = packet.getlayer(Raw).load
    load = packet.getlayer(Raw).fields.get('load')
    return http_parser(load)

def get_url(host, get, post):
    if host:
        if post:
            return host + post
        if get:
            return host + get

def get_get(header_lines):
    for l in header_lines:
        searchGet = re.search('GET /', l)
        if searchGet:
            try:
                return l.split('GET ')[1].split(' ')[0]
            except Exception:
                return

def http_parser(load):
    try:
        headers, body = load.split(r"\r\n\r\n", 1)
    except Exception:
        headers = load
        body = ''
    header_lines = headers.split(r"\r\n")

    host = get_host(header_lines)
    post = get_post(header_lines)
    get = get_get(header_lines)
    url = get_url(host, get, post)
    return url

def get_post(header_lines):
    for l in header_lines:
        searchPost = re.search('POST /', l)
        if searchPost:
            try:
                return l.split(' ')[1].split(' ')[0]
            except Exception:
                return

def get_host(header_lines):
    for l in header_lines:
        searchHost = re.search('[Hh]ost: ', l)
        if searchHost:
            try:
                return l.split('Host: ', 1)[1]
            except Exception:
                try:
                    return l.split('host: ', 1)[1]
                except Exception:
                    return

sniff(iface='en0', prn=http_header, filter="host 10.232.48.75")