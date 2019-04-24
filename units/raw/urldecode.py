from unit import BaseUnit
from collections import Counter
import sys
from io import StringIO
import argparse
from pwn import *
import subprocess
import units.raw
import units
import utilities
import os
from units import NotApplicable
import binascii
import traceback
import urllib.request

class Unit(units.PrintableDataUnit):

	def evaluate(self, katana, case):
		
		try:
			new_result = urllib.request.unquote(self.target)

		# If this fails, it's probably not something we can deal with...
		except (UnicodeDecodeError, binascii.Error):
			return None

		# We only want to work with this if it something new. 
		if new_result != self.target:
			katana.recurse(self, new_result)
			katana.locate_flags(self, new_result )
			katana.add_results(self, new_result )
