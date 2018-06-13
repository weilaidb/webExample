#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi

import cgitb
cgitb.enable()
#这两行代码启用python的CGI跟踪技术

import athletemodel
import yate





athletes = athletemodel.get_from_store()
# 从模型获得数据

form_data = cgi.FieldStorage()
#所有表单数据，并放到一个字典中

athlete_name =form_data['which_athlete'].value
#从表单数据中访问一个指定的数据

print(yate.start_response())
print(yate.include_header("Coach Yj's Timing Data"))
print(yate.header("Athlete: " + athlete_name + ", DOB: " +
                      athletes[athlete_name].dob + "."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({'Home':"/index.html",
                           "Select anthor athlete:":"generate_list.py"}))