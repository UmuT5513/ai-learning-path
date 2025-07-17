import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
try:
    if response.status_code:
        html = response.content
        soup = BeautifulSoup(html, "html.parser")
except Exception as e:
    print(e)

movies = soup.find_all('h3', class_="title")
print(len(movies))
movies_ordered = []
for movie in movies:
    movies_ordered.append(movie.get_text())

    
i = len(movies_ordered) - 1      
for movie in movies_ordered:
    with open('C:/Users/Umut/Desktop/ai-learning-path/web-scraping-4/udemy-Angela-course-project/outputs-udemy/100_movies.txt', 'a') as f:
        f.write(f"{movies_ordered[i]}\n")
    i-=1

    
