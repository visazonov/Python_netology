from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def address_book(contacts_list):
  pattern = r'(\+7|8)\s*\(*(\d{1,3})\)*(\s|\-)*(\d{1,3})(\s|\-)*(\d{1,2})(\s|\-)*(\d{1,2})\s*\(*[доб]*\.*\s*(\d{4,4})*.*'
  substitution_dob = r'+7(\2)\4-\6-\8 доб.\9.'
  substitution = r'+7(\2)\4-\6-\8'
  contacts_res = []
  for c in contacts_list:
    # con = ",".join(c)
    full_name = " ".join(c[:3]).rstrip().split(' ')
    if 'доб' in c[5]:
      phone = re.sub(pattern, substitution_dob, c[5])
    else:
      phone = re.sub(pattern, substitution, c[5])
    if len(full_name) < 3:
      contacts = [full_name[0], full_name[1], c[2], c[3], c[4], phone, c[6]]
    else:
      contacts = [full_name[0], full_name[1], full_name[2], c[3], c[4], phone, c[6]]
    # print(contacts)
    contacts_res.append(contacts)
  # print(contacts_res)
  return contacts_res


def filter(contacts):
  res = []
  for c in contacts:
    first_name = c[0]
    last_name = c[1]
    for new_c in contacts:
      new_first_name = new_c[0]
      new_last_name = new_c[1]
      if first_name == new_first_name and last_name == new_last_name:
        if c[2] == '':
          c[2] = new_c[2]
        if c[3] == '':
          c[3] = new_c[3]
        if c[4] == '':
          c[4] = new_c[4]
        if c[5] == '':
          c[5] = new_c[5]
        if c[6] == '':
          c[6] = new_c[6]
    if c not in res:
      res.append(c)
  # print(res)
  return res

## записываем данные в файл в формате CSV
def write():
  with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(filter_contacts)


if __name__ == '__main__':
  contacts_res = address_book(contacts_list)
  filter_contacts = filter(contacts_res)
  write()


