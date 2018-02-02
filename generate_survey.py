import os

dir_path = os.getcwd() + "/"
# Set number of pages with prompts in study

num_pages = 1

survey_template = None
with open(dir_path + "survey_template.html", "r") as f:
    survey_template = f.read()

page_template = None
with open(dir_path + "page_template.html", "r") as f:
    page_template = f.read()
    
if survey_template is None or page_template is None:
    print "Error reading html template."

# Create prompt pages, substituting values into each page

pages = ""
for i in range(num_pages):
    page = page_template.replace("[PAGE_ID]", str(i+2))
    page = page.replace("[PROMPT_ID]", str(i+1))

    pages += page + "\n"

# Make substitutions into survey template

html = survey_template.replace("[PAGES]", pages)
html = html.replace("[PAGES_PLUS_TWO]", str(num_pages + 2))
html = html.replace("[PAGES_PLUS_THREE]", str(num_pages + 3))
html = html.replace("[TOTAL_PAGES]", str(num_pages))
html = html.replace("[START_RANDOM_PAGE]", str(1))
html = html.replace("[END_RANDOM_PAGE]", str(1))

# Write output to file

with open(dir_path + "output/survey.html", "w") as f:
    f.write(html)