import os, re, sys

"""
    UTF-BOM Remover
    Usage: python bom.py [dir]
"""

bom = b"^\xEF\xBB\xBF"
pattern = r"^(.*)\.(js|css|txt|html|htm|cs|razor|cshtml|xaml|csproj|sln|json|xml)$"
cleaned_files = total_files = 0

if len(sys.argv) == 2:
    rundir = sys.argv[1]
else:
    rundir = '.'

if os.path.isdir(rundir):
    for root, dirs, files in os.walk(rundir):
        for name in files:
            if re.match(pattern, name):
                filename = os.path.abspath(os.path.join(root, name))
                buffer = open(filename, 'rb').read()
                file = re.search(bom, buffer)
                if file:
                    print("UTF-BOM Remover: Removing marker from %s" % name)
                    cleaned_files+= 1
                    open(filename, 'wb').write(buffer[:file.start()] + buffer[file.end():])
        total_files+= len(files)
    print ("UTF-BOM Remover: There are was %d files with BOM in %d files" % (cleaned_files, total_files))
else:
    print ("UTF-BOM Remover: You must set a valid directory.")
    