from os import listdir
from os.path import isfile, join
import sys


path = sys.argv[1]

files = [f for f in listdir(path) if isfile(join(path, f))]
names = [file[:-4].replace('_', ' ') for file in files]
header_lines = [f'{i+1}. [{action}](#action{i+1})\n' for i, action in enumerate(names)]
md_content = [f'![{file[:-4]}]({join(path, file)})\n' for file in files]
md_action_bindings = [f'## <a name="action{i+1}"></a>{action}\n' for i, action in enumerate(names)]

with open(join(path, 'bpmn.md'), 'w+') as f:
        f.writelines(header_lines)
        for binding, content in zip(md_action_bindings, md_content):
                f.write(binding)
                f.write(content)