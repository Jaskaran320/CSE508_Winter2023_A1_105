import os
import random
import lxml
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from typing import List, Dict, Tuple, Union
import string
# nltk.download('punkt')
# nltk.download('stopwords')

ORIGINAL_PATH = os.path.join(os.getcwd(), 'Dataset')
ALTERED_PATH = os.path.join(os.getcwd(), 'DatasetAlter')



print("--- Boolean Queries ---")
print("Enter the full query: ")
print()

n = int(input("Enter the number of queries: "))
bq = BooleanQueries(os.path.join(os.getcwd(), 'DS2'))

for i in range(n):
	print("Enter the search term: ")
	search_term = input()
	print("Enter operations: ")
	operations = input()

	search_term = word_tokenize(search_term.lower())
	search_term = [s for s in search_term if s not in stopwords.words("english")]
	search_term = [s.translate(str.maketrans("", "", string.punctuation)) for s in search_term]
	search_term = [s for s in search_term if s.strip()]

	if operations:
		operations = [s.strip() for s in operations.split(",")]
		operations = [s for s in operations if s in ["AND", "OR", "OR NOT", "AND NOT"]]

	if len(search_term) == 0 or len(operations) != len(search_term) - 1:
		print("Invalid query")
		continue

	query = ""
	for j in range(len(search_term)):
		query += search_term[j]
		if j < len(operations):
			query += " " + operations[j] + " "

	print("Query: ", query)

	result, comparisons = bq.queryProcess(query)
	print("Result: ", result)
	print("Frequency: ", len(result))
	print("Comparisons: ", comparisons)
	print()
