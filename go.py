import argparse
import re
import os

import markdown

此處 = os.path.dirname(os.path.abspath(__file__))

參數 = argparse.ArgumentParser(description='md生成svg')
參數.add_argument('--md', type=str, required=True)
參數 = 參數.parse_args()

md文件名 = 參數.md
html文件名 = md文件名.split('.')[0]+'.html'
svg文件名 = md文件名.split('.')[0]+'.svg'

    

with open(md文件名, encoding='utf8') as f:
    html = markdown.markdown(f.read(),extensions=['tables','attr_list','fenced_code'])
        
    html = f"<link rel='stylesheet' href='{此處}/my.css' />" + html
        
    html = '<meta charset="utf-8">' + html
    
with open(html文件名, 'w', encoding='utf8') as f:
    f.write(html)
    
os.system(f'wkhtmltoimage --width 882 --disable-smart-width {html文件名} {svg文件名}')
    