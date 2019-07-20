# github-readme-hack

衆所周知，github不讓我在readme裏加css，所以就想了這个hack的辦法。

## 原理

把readme轉成html，再轉成svg。

僅僅將svg放進github用的readme就好了。

## 好处

svg文件一般只有幾十KB，不會把落後地區的人民卡成SB。

然後可以按行diff，更新readme的時候也不怎麼佔空間。

## 使用方法

python3.6

wkhtmltopdf

```
pip install markdown
python go.py --md readme.md
```

## 注意

wkhtmltopdf有一些奇怪的性癖……

要不是沒有別的可用的我纔不會用它啦！
