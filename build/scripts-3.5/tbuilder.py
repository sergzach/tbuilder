'''
A project to build and test custom python packages. 

Use it in docker prematurely having create base docker image with installed Python 3 and tbuilder.
'''

import os
import sys
from tempfile import gettempdir
import argparse
from downloaders import DropboxDownloader
from testchecker import TestChecker

_DOWNLOAD_DIR = os.path.join(gettempdir(), '.tbuilder')
_MSG_TEST_OK = 'Test OK.'
_DEFAULT_PYTHON_CMD = 'python'
_DEFAULT_MAX_TEST_TIME = 600


class TBuilderOptionError(Exception): pass
class TBuilderTestError(Exception): pass


def _create_arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--source', type=str, required=True, help='a source of a project')
	parser.add_argument('--python_cmd', type=str, default=_DEFAULT_PYTHON_CMD, help='a python cmd')
	parser.add_argument('--max_test_time', type=int, default=_DEFAULT_MAX_TEST_TIME, help='a test command to test a project')
	return parser.parse_args()


def _log(msg):
	sys.stdout.write('{}\n'.format(msg.strip()))
	sys.stdout.flush()


def main():
	arg_parser = _create_arg_parser()
	downloader = DropboxDownloader()
	# download, clean before and clean after
	with downloader.start_download(src=arg_parser.source, download_to=_DOWNLOAD_DIR) as download_iterator:
		for msg in download_iterator():
			_log(msg)
		test_checker = TestChecker(src_dir=_DOWNLOAD_DIR, python_cmd=arg_parser.python_cmd, max_test_time=arg_parser.max_test_time)
		# install before testing
		for msg in test_checker.install():
			_log(msg)
		# find setup.py and run 'python setup.py test'
		for msg in test_checker.test():
			_log(msg)		
		_log(_MSG_TEST_OK)



if __name__ == '__main__':
	main()

