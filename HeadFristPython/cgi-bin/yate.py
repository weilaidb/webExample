# -*- coding: utf-8 -*-
from string import Template
# 从标准库string中导入Temlate类


def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')
    # 这个函数需要一个可选的字符串作为参数，用它来创建一个CGI“content-type：”行，参数缺省值为“text/html”

def include_header(the_title):
    with open('templates/header.html') as headf:
        # 打开模板文件，读入文件，换入所提供的标题
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
    # 这个函数需要一个字符串作为参数，用在html页面最前面的标题中。页面本身存储在一个单独的文件“templates/header.html”
    # 可以根据需要替换标题

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    # 换入链接字典
    for key in the_links:
        # 将链接字典转换为一个字符串，然后换入模板
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))
    # 与include_header函数一样，这个函数使用一个字符串作为参数，来创建htm页面的尾部
    # 页面本身存储在"template/footer"中，参数用于动态地创建一组html链接标记。从这些标记看，参数应该是一个字典

def start_form(the_url, form_type="POST"): # 这一般是post或者get
    return('<form action="' + the_url + '" method="' + form_type + '">')
    # 这个函数返回表单最前面的html，允许调用者指定url，还可以指定所要使用的方法

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')
    # 这个函数返回的表单末尾的html标记，同时还允许调用着制定表单“submit”按钮的文本

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')
    # 给定一个单选按钮名和值，创建一个html单选按钮（通常包括在一个html表单中）。注意：2个参数都是必要的

def u_list(items):
    u_string = '<ul>'
    for item in items:
        # 一个简单的for循环就可以达到目的
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)
    # 给定一个项列表，这个函数会把该列表转换为一个html无序列表。一个简单的for循环就可以达到目的

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')
    # 创建并返回一个html标题标记(h1,h2,h3等)，默认为h2级标题。“header_text”参数是必要的

def para(para_text):
    return('<p>' + para_text + '</p>') 
    # 文本

