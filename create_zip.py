import zipfile
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
zip_path = os.path.join('..', 'submit-widget.zip')

if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f == 'create_zip.py':
                continue
            filepath = os.path.join(root, f)
            arcname = filepath[2:].replace(os.sep, '/')
            zf.write(filepath, arcname)
            print(f'Added: {arcname}')

print('ZIP created successfully!')
