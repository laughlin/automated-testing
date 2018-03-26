from bs4 import BeautifulSoup
import urllib.request

SSL = "https"
NON_SSL = "http"
NONE_SET = "n/a"
OK = "OK"

def check_matching(expected, actual):
    if actual == expected:
        match_result = OK
    else:
        match_result = "Expected and actual do not match"
    return match_result

#--- Parsing the url output to get a tag or link ---#
def return_tag(url, tag):
    ''' This function parses the html of the parameter url and returns the url of a canonical if set.'''
    f = urllib.request.urlopen(url)
    soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Find all html elements that are of type link. Then, for each of these elements, if it is a canonical
    # link, set this to be the canonical and break out of the loop. There can only be one canonical set so no need
    # to check the rest of the links.
    result = "None set"
    if tag == "title":
        for link in soup.find(tag):
            result = link
    else:
        for link in soup.findAll('meta'):
            if link.get('name') == tag:
                result = link.get('content')
    return result

def return_canonical(url):
    ''' This function parses the html of the parameter url and returns the url of a canonical if set.'''
    f = urllib.request.urlopen(url)
    soup = BeautifulSoup(f.read(), 'html.parser')

    # Originally set canonical to be none. Need to override this if it does exist.
    canonical = NONE_SET
    
    # Find all html elements that are of type link. Then, for each of these elements, if it is a canonical
    # link, set this to be the canonical and break out of the loop. There can only be one canonical set so no need
    # to check the rest of the links.
    for link in soup.findAll('link'):
        if link.get("rel")[0] == "canonical":
            canonical = link.get('href')
            break
    return canonical

#--- Checking SEO ---#
def check_seo_length(tag, min_length, max_length):
    if len(tag) >= min_length and len(tag) <= max_length:
        seo_result = OK
    elif len(tag) < min_length:
        seo_result = "Too short, should be >= "+str(min_length)
    else:
        seo_result = "Too long, should be <= "+str(max_length)
    return seo_result

def check_seo_hops(hops):
    "Response is based on seo accepted number of hops"
    if hops >= 3:
        seo_check = "Correct redirect, but hopped three times or more."
    else:
        seo_check = OK
    return seo_check


#--- Involves adjusting urls for environment or parsing---#
def change_env(url, is_ml_review, is_ssl):
    url = return_full_clean_path(url, is_ssl)
    if is_ml_review:
        url = change_to_review(url) 
    else:
        url = change_to_prod(url)
    return url

def change_to_prod(url):
    if 'review.masterlock' in url or 'review.sentrysafe' in url:
        split_url = url.split('review')
        url = "".join([split_url[0],"www", split_url[1]])
    return url

def change_to_review(url):
    basic_path = url.split('www', 1)
    review_url = "".join([basic_path[0],'review', basic_path[1]])
    return review_url

def get_base(is_ssl):
    if is_ssl: base = SSL
    else: base = NON_SSL
    return base

def return_full_clean_path(url, is_ssl):
    '''Adds the full url path if none was defined on the input file.'''
    base = get_base(is_ssl)
    url = url.strip().rstrip('/')
    if "//" not in url:
        url = "".join([base,"://",url])
    return url

#--- Getting constant results ---#
def get_okay():
    return OK
