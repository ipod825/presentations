#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess

def append_pdf(dirname):
    res = ''
    for fname in os.listdir(dirname):
        if '.pdf' in fname:
            if not os.path.isfile(os.path.join(dirname, 'thumbnail.jpg')):
                subprocess.call("convert -density 150 {0}/{1}\[0\] {0}/thumbnail.jpg".format(dirname, fname), shell=True)
            res+= '\n<a href="../presentations/{}/main.pdf" target=" blank">'.format(dirname)
            res+= '\n<img src="../presentations/{}/thumbnail.jpg" alt="" class="img-thumbnail" style="width:280px;height:185px" />\n'.format(dirname)
            res+="</a>"
            return res

    assert False, "Can not find pdf file in {}".format(dirname)
        
if __name__ == "__main__":
    root = './'
    count=0
    res=''
    for diretory in os.listdir(root):
        if os.path.isdir(diretory) and diretory!='.git':
            if count % 3 ==0:
                res += '<div class="row">\n'
            res += '<div class="col-md-4 col-sm-4 col-xs-12">\n<div class="text-center">'
            res += append_pdf(diretory)
            res+='\n</div>\n</div>\n'

            if count % 3 ==2:
                res+='</div>\n'
            count += 1

    if count % 3 !=0:
        res+='</div>\n'

    with open('index.html', 'w') as f:
        f.write(res)
