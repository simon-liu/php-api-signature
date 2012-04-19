#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse_php_api(content):
    className = parse_class_name(content)
    methods = parse_php_methods(content)
    if not className:
        return methods

    return [className + '::' + method for method in methods]

def parse_class_name(content):
    start = content.find('<strong class="classname">')
    if -1 == start:
        return None

    end = content.find('</strong>', start)
    if -1 == end:
        raise Exception

    return remove_extra_spaces(remove_html_tags(content[start: end]))

def parse_php_methods(content):
    methods = []
    start, end = 0, 0
    while True:
        start = content.find('<div class="methodsynopsis dc-description">', end)
        if -1 == start:
            break

        end = content.find('</div>', start)
        if -1 == end:
            raise Exception

        methods.append(remove_extra_spaces(remove_html_tags(content[start: end])).strip())

    return methods

def remove_html_tags(data):
    import re
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def remove_extra_spaces(data):
    import re
    p = re.compile(r'\s+')
    return p.sub(' ', data)

if __name__ == '__main__':
    import sys, os
    name = sys.argv[1]
    if os.path.isdir(name):
        print "%s is a dir"
    else:
        f = open(name)
        methods = parse_php_api(f.read())
        if len(methods) > 0:
            print "\n".join(methods)
