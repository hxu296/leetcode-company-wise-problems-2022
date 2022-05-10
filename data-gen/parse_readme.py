from markdown2csv import md_to_df
import re
import pandas as pd

parsed_list = []
df = md_to_df('../data/leetcode_repo_readme.md')
for _, row in df.iterrows():
    name_and_link = row['Title']
    difficulty = row['Difficulty']
    solution = row['Solutions'].replace('..', 'https://github.com/fishercoder1534/Leetcode/blob')
    m = re.search(r'\[(.*)\]\((.*)\)', name_and_link)
    name = m[1]
    link = m[2]
    parsed_list.append((name, link, difficulty, solution, ))

parsed_df = pd.DataFrame(parsed_list, columns=['name', 'link', 'difficulty', 'solution'])
parsed_df.to_csv('../data/leetcode_problems.csv', index=False)


