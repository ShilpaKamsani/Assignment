import configparser
from utils import read_file

# Read source and destination file names from config file
config = configparser.ConfigParser()
config.read('config.ini')

source_file = config['FILES']['source_file']
destination_file = config['FILES']['destination_file']

# Read content from source file
source_content = read_file(source_file)

# Parse source content into a dictionary
source_dict = {}
for line in source_content.splitlines():
    key, value = line.split(': ')
    source_dict[key] = value

# Write keys and values to destination file
with open(destination_file, 'w') as f:
    f.write('\n'.join(source_dict.keys()) + '\n')
    f.write('\n'.join(str(v) for v in source_dict.values()) + '\n')
