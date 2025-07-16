import os
import sys
import tarfile

if sys.version_info[0] < 3:
    import urllib2 as urllib
    from StringIO import StringIO
else:
    import urllib.request as urllib
    from io import BytesIO as StringIO

baseURL = "http://www.cerc.utexas.edu/~zixuan/"
target_dir = os.path.dirname(os.path.abspath(__file__))
filenames = ["ispd2005dp.tar.xz"]

for filename in filenames:
    file_url = baseURL + filename
    path_to_file = os.path.join(target_dir, filename)
    
    print("Download from %s to %s" % (file_url, path_to_file))
    response = urllib.urlopen(file_url)
    content = response.read()
    with open(path_to_file, 'wb') as f:
        f.write(content)
    
    print("Uncompress %s to %s" % (path_to_file, target_dir))
    # 使用 tarfile 替代 Archive
    try:
        if filename.endswith('.tar.xz'):
            with tarfile.open(path_to_file, 'r:xz') as tar:
                tar.extractall(target_dir)
        elif filename.endswith('.tar.gz'):
            with tarfile.open(path_to_file, 'r:gz') as tar:
                tar.extractall(target_dir)
        elif filename.endswith('.tar'):
            with tarfile.open(path_to_file, 'r') as tar:
                tar.extractall(target_dir)
        else:
            print("Warning: Unknown file format for %s" % filename)
        print("Extraction completed successfully!")
    except Exception as e:
        print("Error during extraction: %s" % str(e))
        # 如果出错，继续执行，不删除文件
        continue
    
    print("remove downloaded file %s" % (path_to_file))
    os.remove(path_to_file)