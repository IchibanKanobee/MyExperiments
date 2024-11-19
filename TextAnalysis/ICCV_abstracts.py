import sys
sys.path.append("../")
import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import json
from utils import file_op
from os.path import join

ICCV_2019_DATA_ROOT = "data/ICCV2019"
ICCV_2019_OPEN_ABSTRACT='http://openaccess.thecvf.com/ICCV2019.py'
#GLOVE_FILE = "data/glove.6B/glove.6B.300d.txt"
GLOVE_FILE = "data/glove.6B/glove.6B.50d.txt"
#GLOVE_FILE = "data/glove.840B/glove.840B.300d.txt"


ICCV_2019_MAIN_CONFERENCE="http://iccv2019.thecvf.com/program/main_conference"
ICCV_OPEN = "http://openaccess.thecvf.com/"


def remove_before_colon(title):
    new_title = title
    pos = title.find(":")
    if (pos != -1):
        new_title = title[pos+1:].lstrip()
    return new_title


def preprocess(text):
     new_text = remove_before_colon(text)

     # keep only words
     words_only_text = re.sub("[^a-zA-Z]", " ", new_text)

     # convert to lower case and split
     words = words_only_text.lower().split()

     # remove stopwords
     stopword_set = set(stopwords.words("english"))
     cleaned_words = list(set([w for w in words if w not in stopword_set]))

     return cleaned_words


def loadGloveModel(gloveFile):
    print ("Loading Glove Model")
    with open(gloveFile, encoding="utf8" ) as f:
        content = f.readlines()
    model = {}
    for line in content:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print ("Done.",len(model)," words loaded!")
    return model



def get_groups_titles_authors_from_table(table):
    groups = []
    titles = []
    authors = []

    current_group = ""

    rows = table.findAll("tr")
    row_count = len(rows)
    for i in range (2, row_count):
        cells = rows[i].findAll("td")
        group = cells[0].get_text()
        title = cells[3].get_text()
        author = cells[4].get_text()

        if len(group) > 0:
            current_group = group

        groups.append(current_group)
        titles.append(title)
        authors.append(author)

    return groups, titles, authors





def get_iccv_groups_titles_authors(iccv_url):
    page = urllib2.urlopen(iccv_url)
    soup = BeautifulSoup(page,'html.parser')

    tables = soup.find_all('table', {"class":"table program_table"})

    groups = []
    titles = []
    authors = []

    for table in tables:
        table_groups, table_titles, table_authors = get_groups_titles_authors_from_table(table)

    groups.extend(table_groups)
    titles.extend(table_titles)
    authors.extend(table_authors)

    return groups, titles, authors


def get_abstract_from_url(abstract_url):
    try:
        page = urllib2.urlopen(abstract_url)
        soup = BeautifulSoup(page,'html.parser')
        div_abstract = soup.find('div', {"id":"abstract"})
        abstract = div_abstract.text
        abstract = abstract.replace('\n', '')
        return abstract
    except:
        print(abstract_url + " not found")
        return ""



def get_titles_abstracts(iccv_url, titles):
    page = urllib2.urlopen(iccv_url)
    soup = BeautifulSoup(page,'html.parser')
    dt_ptitle = soup.find_all('dt', {"class":"ptitle"})
    abstracts = []
    titles_with_abstracts = []
    for dt in dt_ptitle:
        t = dt.get_text()
        if t in titles:
            cont = dt.find_next('a', href=True)
            url = cont.attrs['href']
            abstract_url = ICCV_OPEN + url
            abstract = get_abstract_from_url(abstract_url)
            if len(abstract) > 0:
                abstracts.append(abstract)
                titles_with_abstracts.append(t)
    return titles_with_abstracts, abstracts


def get_iccv_groups_titles_authors_abstracts_from_web(url_2019, url_abstract):
    groups, titles, authors = get_iccv_groups_titles_authors(url_2019)
    titles_with_abstracts, abstracts = get_titles_abstracts(url_abstract, titles)
    count = len (abstracts)
    gr = []
    tt = []
    au = []
    abst = []
    for i in range(count):
        ind = titles.index(titles_with_abstracts[i])
        gr.append(groups[ind])
        tt.append(titles_with_abstracts[i])
        au.append(authors[ind])
        abst.append(abstracts[i])
    return gr, tt, au, abst


def get_iccv_titles(iccv_url):
    page = urllib2.urlopen(iccv_url)
    soup = BeautifulSoup(page,'html.parser')

    dt_ptitle = soup.find_all('dt', {"class":"ptitle"})
    titles = []
    for dt in dt_ptitle:
        t = dt.get_text()
        tt = preprocess(t)
        titles.append(tt)
    return titles


def get_glov_embedding_for_title(model, title):
    emb = []
    title_preprocessed = preprocess(title)
    for word in title_preprocessed:
        try:
            word_emb = model[word]
            emb.append(word_emb)
        except:
            print ("No embedding for word " + word)
            continue
    embedding = np.mean(emb)
    return embedding



def get_titles_glov_embeddings(model, titles):
    embeddings = []
    for title in titles:
        emb = get_glov_embedding_for_title(model, title)
        embeddings.append(emb)
    return embeddings



def get_distance_matrix_between_titles(model, titles):
    count = len(titles)
    embeddings = []
    for i in range (count):
        emb = get_embedding_for_title(model, titles[i])
        embeddings.append(emb)
    return embeddings



def heat_map_matrix_between_titles(model, titles):
    distances = get_distance_matrix_between_titles(model, titles)
    return distances


def get_group_indices_from_groups(groups):
    indices = []
    indices.append(0)
    current_index = 0
    count = len(groups)
    for i in range(1, count):
        if (groups[i] == groups[i-1]):
            indices.append(current_index)
        else:
            current_index = current_index + 1
            indices.append(current_index)
    return indices


def get_index_from_interval(embedding, min, max, count):
    interval = (max - min) / count
    for i in range(count):
        if (embedding >= min + i * interval) and (embedding <= min + (i + 1) * interval):
            return i
    return -1


def get_glov_accuracy(group_indices, interval_indices):
    count = len(group_indices)
    correct = 0
    for i in range(count):
        if (group_indices[i] == interval_indices[i]):
            correct = correct + 1
    return float(correct) / count



def write_json_data_file(dir, name, groups, titles, authors , abstracts):
    file_op.ensure_dir_exists(dir)
    file_name = join(dir, name)
    count = len(groups)
    data = {}
    data["papers"] = []
    for i in range (count):
        data['papers'].append({
            'group': groups[i],
            'title': titles[i],
            'authors': authors[i],
            'abstract': abstracts[i]
        })
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)



def get_iccv_groups_titles_authors_abstracts_from_file(file_name):
    groups = []
    titles = []
    authors = []
    abstracts = []

    with open(file_name) as json_file:
        data = json.load(json_file)
        papers = data["papers"]
        count = len (papers)

        for i in range(count):
            groups.append(papers[i]["group"])
            titles.append(papers[i]["title"])
            authors.append(papers[i]["authors"])
            abstracts.append(papers[i]["abstract"])

    return groups, titles, authors, abstracts



def get_iccv_groups_titles_authors_abstracts(dir, name, conference_url, abstracts_url):
    file_name = join(dir, name)
    if file_op.if_file_exists(file_name):
        groups, titles, authors, abstracts = get_iccv_groups_titles_authors_abstracts_from_file(file_name)
    else:
        groups, titles, authors, abstracts = get_iccv_groups_titles_authors_abstracts_from_web(conference_url, abstracts_url)
        write_json_data_file(dir, name, groups, titles, authors , abstracts)
    return groups, titles, authors, abstracts


groups, titles, authors , abstracts = get_iccv_groups_titles_authors_abstracts(ICCV_2019_DATA_ROOT, "data.json", ICCV_2019_MAIN_CONFERENCE, ICCV_2019_OPEN_ABSTRACT)



group_indices = get_group_indices_from_groups(groups)

print(group_indices)

model = loadGloveModel(GLOVE_FILE)
title_embeddings = get_titles_glov_embeddings(model, titles)
#np_embeddings = np.array(title_embeddings).reshape(-1, 1)

group_count = len(set(groups))
print (group_count)

count = len(groups)

interval_indices = []
min_ = min(title_embeddings)
max_ = max(title_embeddings)
for i in range(count):
    interval = get_index_from_interval(title_embeddings[i], min_, max_, group_count)
    interval_indices.append(interval)
    print (groups[i] + " " + titles[i] + " " + authors[i] + " " + str(title_embeddings[i]))

print(interval_indices)

accuracy = get_glov_accuracy(group_indices, interval_indices)
print (accuracy)


