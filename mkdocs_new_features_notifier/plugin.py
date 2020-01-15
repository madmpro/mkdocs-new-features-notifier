import datetime
import json

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


def draft_update_message(added_pages_paths, version):
    update_title = "# New in version " + version + ": \n\n--------"
    items_text = ''
    for page in added_pages_paths:
        with open(page) as documentation_file:
            documentation_content = documentation_file.read()
        description = get_document_description(documentation_content)
        path = get_document_path(documentation_content)
        title = get_document_title(documentation_content)
        items_text += "\n- [" + title + "](" + path + ")" + "\n\t- _" + description + "_"
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
		print("files are ")
		for file_name in files:
			print(file_name)
        return files

    def on_nav(self, nav, config, files):
        return nav

    def get_version_number(self):
        version_num = self.config['doc_version']
        return version_num
