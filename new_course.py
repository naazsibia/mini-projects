import requests
from bs4 import Tag, NavigableString, BeautifulSoup
import re

url = "https://utm.calendar.utoronto.ca/course-search?page="
LAST_PAGE = 17




def page_prereqs(cur_page: int):
    new_page = cur_page
    homepage = requests.get(url + f'{cur_page}')
    soup = BeautifulSoup(homepage.content, 'html.parser')
    courses = soup.find_all("h3", class_="js-views-accordion-group-header")
    prereqs = {}
    next_pages = soup.find_all("li", class_="pager__item")

    num_pages = []
    for page in next_pages:
        all_pages = page.findChildren("a")
        for page in all_pages:
            clean = page.text.strip().replace(' ', '').replace('Page\n', '')
            if clean.isdigit():
                num_pages.append(int(clean))

    num_pages.sort()

    for num in num_pages:
        if num > cur_page:
            new_page = num - 1
            break
    

    for course in courses:
        pre = course.find_next('strong')
        if pre.text.startswith('Prerequisites: '):
            code = course.text.strip().split(' ')[0]
            if not code.startswith('CSC'):
                continue
            temp = pre.find_next('span').contents
            prereqs[code] = clean_contents(temp)
    return new_page, prereqs


def clean_contents(contents) -> None:
    p = r'(\w{3,}\d{3,}(H|Y)5)|or|and'
    lst = []
    for i, element in enumerate(contents):
        if type(element) is Tag:
            contents[i] = element.text
        m = re.search(p, contents[i])
        if m:
            text = m.group(0)
            contents[i] = text
            if text in ['or', 'and']:
                continue
            if i + 1 < len(contents) and contents[i + 1] == 'or':
                text = '(' + text 
            if i - 1 > -1 and contents[i - 1] == 'or':
                lst[-1] = '(' + lst[-1] + ' or ' + text
                if i + 1 == len(contents) or contents[i + 1] != 'or':
                    lst[-1] += ')'
                continue
            lst.append(m.group(0))
    if lst == ['and']:
        return []
    return lst




if __name__ == '__main__':
    current_page = 15
    pre = {}
    while current_page <= LAST_PAGE:
        prereqs = page_prereqs(current_page)
        pre.update(prereqs[1])
        current_page = prereqs[0]
    
    with open('prereqs.json', 'w+') as f:
        f.write(str(pre))
