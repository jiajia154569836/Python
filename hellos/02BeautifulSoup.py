from bs4 import BeautifulSoup

html='''
<html><head><title id='id_title' class='class_title1 class_title2'>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div><!-- comment test --></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())

print('title type:', type(soup.title))
print('title name:', soup.title.name)
print('title attrs:', soup.title.attrs)

print('soup.p.string type:', type(soup.p.string))
print('soup.p.string contents:', soup.p.string)

#
print('soup type:', type(soup))
print('soup.name:', soup.name)
print('soup.attrs:', soup.attrs)

print('soup.div.string:', soup.div.string)
print('soup.div.string type:', type(soup.div.string))
print('soup.p.string type:', type(soup.p.string))

print('soup.p.string:', soup.p.string)
print('soup.div.string:', soup.div.string)

print('soup.p.strings:',soup.p.strings)
print('soup.p.strings list:', list(soup.p.strings))
print('----------------------------------------')
print('soup.p.stripped_strings:', soup.p.stripped_strings)
print('soup.p.stripped_strings list:', list(soup.p.stripped_strings))

print('soup.div.contents:', soup.div.contents)
print('soup.div.contents list:', list(soup.div.contents))
print('----------------------------------------')
print('soup.div.children:', soup.div.children)
print('soup.div.children list:', list(soup.div.children))

html = '''
<html><head></head>
<body>
<p><b>p-content</b></p>
<div>div-content<span>span-content</span></div>
'''

soup = BeautifulSoup(html, 'lxml')
print('soup.div.contents:', soup.div.contents)
print('soup.div.contents list:', list(soup.div.contents))
print('----------------------------------------')
print('soup.div.descendants:', soup.div.descendants)
print('soup.div.descendants list:', list(soup.div.descendants))

html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(id='panda'))


html='''
<html><head></head>
<body>
<p><b>p-content1</b></p>
<p>p-content2</p>
<p>p-content3</p>
<p>p-content4</p>
<p>p-content5</p>
<p>p-content6</p>
<p>p-content7</p>
<panda id='panda'>panda-content</panda>
<panda id='panda'>panda-content</panda>
<div>div-content<span>span-content</span></div>
<div>div-content<span>span-content</span></div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('p'))
print('-----------------------------------')
print(soup.find_all('p', limit=3))
print(soup.select('p'))
print(soup.select('.p-class'))
print(soup.select('p #panda'))
print(soup.select('div #panda'))

