from os import environ
import json

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
sample_participants = []
with open('sample_participants.json') as sample_participants:
    sample_participants=json.load(sample_participants)
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="",
    data_pages_enabled=True,
    sample_participants=sample_participants,
    num_sample_participants=10,
    round_values = ["0.50","0.75","1.00","1.25","1.50","1.75","2.00","2.25","2.50"],
    seconds_for_counting_task=90
)


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

ROOMS = []

SESSION_CONFIGS = [
    dict(
        name='Matching_Game',
        num_demo_participants=1,
        app_sequence=[
            # 'Introduction',
            # 'Introduction_Practice',
            # 'Game_1',
            # 'Game_1_Game',
            # 'Game_1_Data',
            # 'Game_2',
            # 'Game_2_Game',
            # 'Game_2_Data',
            # 'Game_3',
            # 'Game_3_Game',
            # 'Game_3_Data',
            # 'Game_4',
            # 'Game_4_Data',
            'Game_5',
            'Game_5_Game',
            'Game_5_Data',
            'Performance_Guesses',
            'Survey',
            'Summary']
    ),
]

# STATICFILES_DIRS = [
#     path.join(".", "_static/javascript")
# ]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '$n1yiypa)xa!2(q+xcb#-b5os0@8hmur!42-w*nq!mmuk06$c7'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'custom_templates']
