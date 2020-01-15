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
        ('param', config_options.Type(mkdocs_utils.string_types, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_serve(self, server):
        return server

    def on_pre_build(self, config):
        return

    def on_files(self, files, config):
		print("files are ")
		for file_name in files:
			print(file_name)
        return files

    def on_nav(self, nav, config, files):
        return nav

    def on_env(self, env, config, site_nav):
        return env
    
    def on_config(self, config):
        return config

    def on_post_build(self, config):
        return

    def on_pre_template(self, template, template_name, config):
        return template

    def on_template_context(self, context, template_name, config):
        return context
    
    def on_post_template(self, output_content, template_name, config):
        return output_content
    
    def on_pre_page(self, page, config, site_nav):
        return page

    def on_page_read_source(self, page, config):
        return ""

    def on_page_markdown(self, markdown, page, config, site_nav):
        return markdown

    def on_page_content(self, html, page, config, site_nav):
        return html

    def on_page_context(self, context, page, config, nav):
        return context

    def on_post_page(self, output_content, page, config):
        return output_content
        
	


