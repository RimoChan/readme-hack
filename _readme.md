# github-readme-hack

衆所周知，github不讓我在readme裏加css，所以就想了這个hack的辦法。

## 原理

把readme轉成html再轉成svg再存進一個新的readme就好啦。

## 使用方法

python3.6

wkhtmltopdf

```
pip install markdown
python go.py --md readme.md
```
