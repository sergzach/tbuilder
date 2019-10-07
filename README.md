A python-based builder to build and test projects.

# Examples of usage
`tbuilder.py --test='cd ~/files/django && python3.6 runtests.py'` (meaning only cd to existing directory and testing)
`tbuilder.py --source='https://www.dropbox.com/sh/3u1wts6em61wkis/AADf3vhMSE16tam7yBLxyEZ9a?dl=0'` (meaning downloading all files in the web path, if --test is omitted then go to downloaded directory and run )
`tbuilder.py --source='https://github.com/sergzach/readingproc/archive/master.zip' --test='cd readingproc && python setup.py test'` (meaning downloading and unzipping the clone)
`tbuilder.py --source='https://github.com/django/django.git' --test='cd django && python3.6 runtests.py'` (meaning `git clone https://github.com/django/django.git` then testing)

# Current supported options
Currently not all behaviouristic variants of downloading and install are supported.

Supported: downloading from dropbox.com and default install (no --test option yet). E.g.:
`tbuilder.py --source='https://www.dropbox.com/sh/3u1wts6em61wkis/AADf3vhMSE16tam7yBLxyEZ9a?dl=0'`