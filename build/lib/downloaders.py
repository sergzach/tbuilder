"""
Various downloaders to download sources for tbuilder.py before build and test.
"""
from contextlib import contextmanager
from os import makedirs
from io import BytesIO
from shutil import rmtree
import requests
import zipfile

class DropboxDownloader:
	_MSG_DOWNLOADING_START = 'Downloading: "{}".'
	_MSG_DOWNLOADING_OK = 'Downloading is OK. Extracting.'
	_MSG_EXTRACTING_OK = 'Extracting is OK.'

	@staticmethod
	def _clean(download_to):
		rmtree(download_to, ignore_errors=True)


	@staticmethod
	def _makedirs(download_to):
		makedirs(download_to)


	@staticmethod
	def _fix_link(download_to):
		"""
		Fixes Dropbox folder link (must ends with ?dl=1) to download correct zip archive of shared folder.
		"""
		query = '?'
		end = '?dl=1'
		return download_to if query not in download_to else '{}{}'.format(download_to[:download_to.find(query)], end)

	def _download_iterator(self, src, download_to):
		def inner():
			new_src = self._fix_link(src)
			yield self._MSG_DOWNLOADING_START.format(new_src)		
			r = requests.get(new_src, stream=True)
			z = zipfile.ZipFile(BytesIO(r.content))		
			yield self._MSG_DOWNLOADING_OK
			z.extractall(path=download_to)
			yield self._MSG_EXTRACTING_OK
		return inner


	@contextmanager
	def start_download(self, *, src, download_to):
		self._clean(download_to)
		self._makedirs(download_to)

		try:
			yield self._download_iterator(src, download_to)
		finally:
			self._clean(download_to)



