#!/usr/bin/python3
"""
3. Count
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """List containing the titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'AngentMEGO'},
                       params={'after': after})

    if after is None:
        return hot_list

    if res.status_code == 200:
        res = res.json()
        after = res.get('data').get('after')
        hots = res.get('data').get('children')
        hot_list += list(map(lambda elm: elm.get('data').get('title'), hots))
        return recurse(subreddit, hot_list, after)
    return None


def my_sorted(my_dict):
    """definition"""
    result = []
    items_list = my_dict.items()
    items_list = sorted(items_list, key=lambda item: item[1])
    items_list = list(reversed(items_list))
    i = 0
    j = 0
    while len(result) < len(items_list):
        if j <= len(items_list) - 2 and\
                items_list[j][1] == items_list[j + 1][1]:
            while j <= len(items_list) - 2 and\
                    items_list[j][1] == items_list[j + 1][1]:
                j += 1
            sub = sorted(items_list[i:j + 1], key=lambda item: item[0])
            result += sub
            i = j + 1
            j += 1
            continue
        result.append(items_list[j])
        i += 1
        j += 1
    return dict(result)


def count_words(subreddit, word_list):
    """
    parses the title of all hot articles, and prints a sorted count of
    given keywords
    """
    dict_word = {}
    word_list = list(map(lambda word: word.lower(), word_list))

    for word in word_list:
        dict_word[word] = 0
    titles = recurse(subreddit, [])
    titles = (' '.join(titles)).lower()
    titles = titles.split(" ")

    for word in word_list:
        dict_word[word] += titles.count(word)
    sort_dict = my_sorted(dict_word)

    for key, value in sort_dict.items():
        if value > 0:
            print(f"{key}: {value}")
