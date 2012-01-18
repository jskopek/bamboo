"""
http://djangosnippets.org/snippets/186/
"""
import sys
import tempfile
import hotshot
import hotshot.stats
from django.conf import settings
from cStringIO import StringIO
import random
import string
import os

class ProfileMiddleware(object):
    """
    Displays hotshot profiling for any view.
    http://yoursite.com/yourview/?prof

    Add the "prof" key to query string by appending ?prof (or &prof=)
    and you'll see the profiling results in your browser.
    It's set up to only be available in django's debug mode,
    but you really shouldn't add this middleware to any production configuration.
    * Only tested on Linux
    """

    def generate_logfile_path(self):
        try:
            PROFILE_LOG_BASE = settings.PROFILE_LOG_BASE
        except:
            PROFILE_LOG_BASE = "/logs"


        random_filename = ''.join(random.choice(string.letters) for i in range(100))
        log_file = os.path.join(PROFILE_LOG_BASE, random_filename)
        return log_file

    def should_run_profiler(self):
        try:
            PROFILE_PROBABILITY = settings.PROFILE_PROBABILITY
        except:
            PROFILE_PROBABILITY = 0.1

        if not random.random() < PROFILE_PROBABILITY:
            return False
        #elif not settings.DEBUG or not request.GET.has_key('prof'):
            #return False
        else:
            return True

    def process_request(self, request):
        if self.should_run_profiler(): 
            self.prof = hotshot.Profile( self.generate_logfile_path() )
        else:
            self.prof = None

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.prof: #settings.DEBUG and request.GET.has_key('prof'):
            return self.prof.runcall(callback, request, *callback_args, **callback_kwargs)

    #def process_response(self, request, response):
        #if settings.DEBUG and request.GET.has_key('prof'):
            #self.prof.close()

            #out = StringIO()
            #old_stdout = sys.stdout
            #sys.stdout = out

            #stats = hotshot.stats.load(self.tmpfile.name)
            ##stats.strip_dirs()
            #stats.sort_stats('time', 'calls')
            #stats.print_stats()

            #sys.stdout = old_stdout
            #stats_str = out.getvalue()

            #if response and response.content and stats_str:
                #response.content = "<pre>" + stats_str + "</pre>"

        #return response
