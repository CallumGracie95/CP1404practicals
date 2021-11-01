import wikipedia
from wikipedia import WikipediaPage

search = input("Enter page title: ")
print(wikipedia.summary(search))


try:
    print(wikipedia.search('Monty'))
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)
