from googlesearch import search

query = "How is the best programming language?"

for result in search(query, num_results=50):
    print(result)
