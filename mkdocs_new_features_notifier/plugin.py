import datetime
import json
import os

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


def set_version_number():
    date_time = datetime.datetime.today()
    year = date_time.year
    month = date_time.month
    day = date_time.day
    today_date = str(year) + '.' + str(month) + '.' + str(day)
    return today_date


def get_document_description(documentation_content):
    try:
        description = documentation_content.split('description:')[1].split('\n')[0].strip()
    except IndexError:
        description = ""
    return description


def get_document_path(documentation_content):
    try:
        path = documentation_content.split('permalink:')[1].split('\n')[0].strip()
    except IndexError:
        path = ""
    return path

def get_document_title(documentation_content):
    try:
        title = documentation_content.split('title:')[1].split('\n')[0].strip()
    except IndexError:
        title = ""
    return title

def get_document_authors(documentation_content):
    try:
        title = documentation_content.split('authors:')[1].split('\n')[0].strip()
    except IndexError:
        title = ""
    return title

def get_document_date(documentation_content):
    try:
        title = documentation_content.split('date:')[1].split('\n')[0].strip()
    except IndexError:
        title = ""
    return title

def draft_update_message(added_pages_paths, version):
    update_title = "# New in version " + version + ": \n\n--------"
    items_text = ''
    for page in added_pages_paths:
        with open(page) as documentation_file:
            documentation_content = documentation_file.read()
        description = get_document_description(documentation_content)
        path = get_document_path(documentation_content)
        title = get_document_title(documentation_content)
        authors = get_document_authors(documentation_content)
        docdate = get_document_date(documentation_content)
        if title:
            items_text += "\n- [" + title + "](../../" + path + ")" + "\n Date: " + docdate + " Authors: " + authors
    return update_title + items_text

def update_features_listing(new_features_file, added_pages_paths, version):
    with open(new_features_file, 'w') as features_file:
        message = draft_update_message(added_pages_paths, version)
        features_file.write(message)

class NewFeaturesNotifier(BasePlugin):
    config_scheme = (
        ('doc_version', config_options.Type(str, default=set_version_number())),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0
        self.new_features_introduced = False

    def on_files(self, files, config):
        current_pages = []
        new_features_file = ''
        for file in files:
            if file.src_path.split('.')[-1] in ['markdown', 'mdown', 'mkdn', 'mkd', 'md']:
                relative_file_path = file.src_path
                current_pages.append(relative_file_path)
            if file.src_path.split('/')[-1] == "new-features.md":
                new_features_file = config["docs_dir"] + "/" + file.src_path
        initial_pages = []
        try:
            with open(config["docs_dir"] + "/" + "versions.json") as version_file:
                json_data = version_file.readlines()
                data = json.loads(json_data[-1])
                print("initial version is " + data["version"])
                initial_pages = json.loads(json_data[-1])['pages']

        except FileNotFoundError:
            versions_file = open(config["docs_dir"] + "/" + "versions.json", 'w')
            file_names = str(current_pages).replace("\'", "\"")
            versions_file.write('{"version":"' + self.get_version_number() + '","pages":' + file_names + '}')
            versions_file.close()
        added_pages_paths = []
        for page in current_pages:
            if page not in initial_pages:
                added_pages_paths.append(config["docs_dir"] + "/" + page)
                self.new_features_introduced = True
        if added_pages_paths:
            versions_file = open(config["docs_dir"] + "/" + "versions.json", 'a')
            str_current_pages = str(current_pages).replace("\'", "\"")
            versions_file.write('\n{"version":"' + self.get_version_number() + '","pages":' + str_current_pages + '}')
            versions_file.close()
            update_features_listing(new_features_file, added_pages_paths, str(self.get_version_number()))
        return files

    def get_version_number(self):
        version_num = self.config['doc_version']
        return version_num
