#importing pandas as pd
import pandas as pd
import os
import sys

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    for filename in files:
        if filename.endswith((".xls", ".xlsx")):
            file_path = os.path.join(root, filename)
            to_filename = filename.replace(".xls",".csv")
            to_filename = "c_" + filename.replace(".xlsx",".csv")
            to_file_path = os.path.join(root, to_filename)
            print('\t- file %s (full path: %s)' % (filename, file_path))
            data_xls = pd.read_excel(file_path,  dtype=str, index_col=None)
            data_xls.to_csv(to_file_path, encoding='utf-8', index=False)
