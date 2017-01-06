# Borrowed liberally from awscli.
"""
AWS-NMAP
----
A Universal Command Line Environment for Amazon Web Services.
"""
import os

__version__ = '0.0.1'

#
# Get our data path to be added to botocore's search path
#
_awscli_data_path = []
if 'AWS_DATA_PATH' in os.environ:
    for path in os.environ['AWS_DATA_PATH'].split(os.pathsep):
        path = os.path.expandvars(path)
        path = os.path.expanduser(path)
        _awscli_data_path.append(path)
_awscli_data_path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
)
os.environ['AWS_DATA_PATH'] = os.pathsep.join(_awscli_data_path)


EnvironmentVariables = {
    'ca_bundle': ('ca_bundle', 'AWS_CA_BUNDLE', None, None),
    'output': ('output', 'AWS_DEFAULT_OUTPUT', 'json', None),
}


SCALAR_TYPES = set([
    'string', 'float', 'integer', 'long', 'boolean', 'double',
    'blob', 'timestamp'
])
COMPLEX_TYPES = set(['structure', 'map', 'list'])
