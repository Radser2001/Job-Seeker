import time
from bs4 import BeautifulSoup
import requests
import os
import shutil

os.system("")


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


print(style.CYAN + '''

  _    _______                         __      __            _            __      __       _____           __            
 ( )  /_  __(_____ ___  ___  _____    / ____  / /_  _____   ( )          / ____  / /_     / ___/___  ___  / /_____  _____
 |/    / / / / __ `__ \/ _ \/ _____  / / __ \/ __ \/ ___/   |/      __  / / __ \/ __ \    \__ \/ _ \/ _ \/ //_/ _ \/ ___/
      / / / / / / / / /  __(__  / /_/ / /_/ / /_/ (__  )           / /_/ / /_/ / /_/ /   ___/ /  __/  __/ ,< /  __/ /    
     /_/ /_/_/ /_/ /_/\___/____/\____/\____/_.___/____/            \____/\____/_.___/   /____/\___/\___/_/|_|\___/_/     
                                                                                                                         
''')


main_skill = input(style.BLUE + "\n\nEnter your the main skill: ")
print('')
no_of_skills = int(input("How many skils are you familiar with?: "))
familiar_skills = []

print("\nEnter all the skills (including the main skill): ")
for x in range(no_of_skills):
    skill = input('> ')
    familiar_skills.append(skill)


def find_jobs():

    # response status will be the default
    # to get only the text request.get().text
    print(style.RED + "\nSearching for jobs....This may take a while :)\n\n")

    for page in range(1, 11):

        html_text = requests.get(
            'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=' + main_skill + '&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=' + main_skill + '&pDate=I&sequence=' + str(page) + '&startPage=1').text
        # print(html_text)

        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        # print(job)
        # find for h3 tags only inside the job
        # .replace() remove unnecessary spaces
        # enumerate - iterate over the index of the jobs list and jobs content
        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text

            if 'few' in published_date:
                company_name = job.find(
                    'h3', class_='joblist-comp-name').text
                skills = job.find(
                    'span', class_='srp-skills').text.replace(' ', '')
                more_info = job.header.h2.a['href']
                for skill in familiar_skills:
                    if skill in skills:
                        if not os.path.isdir('posts'):
                            os.mkdir('posts')

                        try:
                            with open(f'posts/{company_name.strip()}.txt', 'a') as f:
                                # print(published_date)
                                # print(skills)
                                # print(company_name)
                                # strip() will remove unnecessary details
                                # print(job_title.strip())
                                f.write(
                                    '---------------------------------------------------------------------------------------------------------------------------------------------------\n')
                                f.write(
                                    f'Company Name: {company_name.strip()}\n')
                                f.write(f'Required Skills: {skills.strip()}\n')
                                f.write(f'More info: {more_info}\n\n')
                            print(style.RESET +
                                  f'File saved: {company_name.strip()}')
                            # print('')
                        except OSError:
                            with open(f'posts/{index}.txt', 'a') as f:
                                # print(published_date)
                                # print(skills)
                                # print(company_name)
                                # strip() will remove unnecessary details
                                # print(job_title.strip())
                                f.write(
                                    '---------------------------------------------------------------------------------------------------------------------------------------------------\n')
                                f.write(
                                    f'Company Name: {company_name.strip()}\n')
                                f.write(f'Required Skills: {skills.strip()}\n')
                                f.write(f'More info: {more_info}\n\n')
                            print(style.RESET + f'File saved: {index}')


if __name__ == '__main__':
    while True:

        find_jobs()
        choice = input(style.BLUE +
                       "\n\nSet a time to search the website again (Stay Updated :) )? (click 'enter' to continue / quit' to stop): ").lower()
        if choice == 'quit':
            break
        hours = int(input('\nHours: '))
        minutes = int(input('Minutes: '))
        seconds = int(input('Seconds: '))
        time_wait_seconds = hours * 60 * 60 + minutes * 60 + seconds
        print(f'\nWaiting {hours} hr: {minutes} min: {seconds} sec')
        time.sleep(time_wait_seconds)
        shutil.rmtree('posts')

print(style.CYAN + '''\n\n\n


   ______                __   __              __      __
  / ________  ____  ____/ /  / /  __  _______/ /__   / /
 / / __/ __ \/ __ \/ __  /  / /  / / / / ___/ //_/  / / 
/ /_/ / /_/ / /_/ / /_/ /  / /__/ /_/ / /__/ ,<    /_/  
\____/\____/\____/\__,_/  /_____\__,_/\___/_/|_|  (_)   
                                                        
''')
