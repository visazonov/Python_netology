# from secretary import Secretary
#
#
# sec = Secretary('Kolya', 'qwerty')
#
# if __name__ == '__main__':
#     print('good evning', sec.name)

parsed = []
time_parsed = 'a'
header_parsed = 'b'
link_absolute = 'c'
habr_article_text = 'd'

item = {
  'time': time_parsed,
  'header': header_parsed,
  'link': link_absolute,
  'text': habr_article_text
}

parsed.append(item)
print(parsed)