import yaml
from subprocess import run
import re
import os

zk_folder = '~/Dropbox/zk/'

script_path = os.path.dirname(os.path.abspath(__file__))


def main():
    for root, dirs, files in os.walk(script_path+'/../content/'):
        for file in files:
            if file.endswith('.yaml'):
                content_folder = os.path.join(root)
                yaml_filename = file

                create_content_file(content_folder, yaml_filename)


def create_content_file(content_folder, yaml_filename):

    with open(f'{content_folder}/{yaml_filename}') as f:
        spects = yaml.safe_load(f)

    # Search for the content file and read its text
    query = spects['zk_file']
    print(query)
    filename = (run(query, capture_output=True, shell=True)
                .stdout
                .splitlines()[0]
                .decode('utf-8')
                .replace("'", ""))
    file_path = zk_folder + filename
    file_path = file_path.replace('~/', '/home/bersp/')

    with open(file_path, 'r') as f:
        text = f.read()

    # Change title
    old_title = re.search(r'^#\s+(.*)$', text, re.MULTILINE).group(0)
    text = text.replace(old_title+'\n', '')

    if spects['transformations']['title']:
        exec(spects['transformations']['title'], globals())
        title = t(old_title).replace('# ', '')
    else:
        title = old_title

    # Change md metadata
    match = re.search(r'^---\n(.*?)\n---', text, flags=re.DOTALL)

    summary = spects['summary']

    new_metadata = '\n'.join([
        f'title: "{title}"',
        f'summary: "{summary}"',
        'math: true',
    ])
    text = text[:match.start(1)] + new_metadata + text[match.end(1):]

    # Math in ketex is more stable using \\ inested of \
    text = re.sub(r'\\', r'\\\\', text)

    # One less level in heading
    m = re.findall(r'(#+ .*)', text)
    for m in re.findall(r'(#+ .*)', text):
        text = re.sub(m, m[1:], text)

    # Replace all links with just the link text
    text = re.sub(r'\[(.*?)\]\((?!#)(.*?)\)', r'\1', text)

    # Write new file
    with open(f'{content_folder}/{title}.md', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    main()
