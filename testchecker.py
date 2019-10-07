"""
A class which run tests.
"""

from readingproc import ReadingProc, TotalTimeout


class TestError(Exception): pass
class TestTimeoutError(Exception): pass


class TestChecker:
	_CMD_INSTALL = 'cd {src_dir} && {python_cmd} setup.py install'
	_CMD_TEST = 'cd {src_dir} && {python_cmd} setup.py test'

	def __init__(self, *, src_dir, python_cmd, max_test_time):
		self._src_dir = src_dir
		self._python_cmd = python_cmd
		self._max_test_time = max_test_time		


	def _do(self, cmd, fail_msg):
		proc = ReadingProc(cmd.format(src_dir=self._src_dir, python_cmd=self._python_cmd))
		proc.start()
		try:
			for data in proc.iter_run(total_timeout=self._max_test_time):
				yield data.stdout.decode() + data.stderr.decode()
			if proc.return_code != 0:
				raise TestError(fail_msg)
		except TotalTimeout:
			raise TestTimeoutError('Test lasts more than {} seconds. Fix it or set up more time.'.format(self._max_test_time))


	def install(self):
		for msg in self._do(self._CMD_INSTALL, 'Build in "{}" has failed.'.format(self._src_dir)):
			yield msg


	def test(self):
		for msg in self._do(self._CMD_TEST, 'Test in "{}" has failed.'.format(self._src_dir)):
			yield msg