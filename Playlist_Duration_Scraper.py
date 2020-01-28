import re
from bs4 import BeautifulSoup
from selenium import webdriver


def scrape():
    url = input("Enter Spotify playlist URL\n")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')            # run browser in headless mode aka without visual feedback

    browser = webdriver.Chrome(options=options)
    browser.get(url)
    html = browser.execute_script("return document.documentElement.outerHTML")
    # entire HTML source code correctly returned
    browser.quit()

    soup = BeautifulSoup(html, "html5lib")
    data = soup.find_all('div', attrs={'class': 'tracklist-duration tracklist-top-align'})   
    # tag containing song individual song duration

    dlist = []
    for items in data:
       dlist.append(items.text)
    return dlist


def proc(dlist):
    r = re.compile("[0-9]+:[0-9]+")
    new = list(filter(r.match, dlist))
    sec = []
    mins = []
    for items in new:
        mins.append(int(items[0]))
        sec.append(int(items[2:]))

    min_sum = sum(mins)
    sec_sum = sum(sec)

    s = sec_sum % 60
    m = (min_sum + int(sec_sum/60))
    h = int(m / 60)
    m = m % 60

    print("Total playlist duration: {}h {}m {}s".format(h, m, s))
    totsongs = len(mins)
    avg = (h*3600 + m*60 + s)/totsongs

    s = round(avg % 60)
    m = int(avg/60)
    print("Average song duration: {}m {}s".format(m, s))
    print("Total songs detected: {}".format(totsongs))


def main():
    d = scrape()
    proc(d)


if __name__ == "__main__":
    main()
