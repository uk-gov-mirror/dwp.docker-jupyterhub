import os
import sys

from hybridcontents import HybridContentsManager
from s3contents import S3ContentsManager
import getpass

username = getpass.getuser()

c = get_config()

c.NotebookApp.terminals_enabled = False

c.NotebookApp.contents_manager_class = HybridContentsManager

c.HybridContentsManager.manager_classes = {
    's3home': S3ContentsManager,
    's3shared': S3ContentsManager
}

c.HybridContentsManager.manager_kwargs = {
    's3home': {
        "bucket": os.environ.get('S3_BUCKET'),
        "prefix": "home/" + os.path.join(username, "jupyter_notebooks"),
        "sse": "aws:kms",
        "kms_key_id": os.environ.get('KMS_HOME'),
    },
    's3shared': {
        "bucket": os.environ.get('S3_BUCKET'),
        "prefix": "shared/jupyter_notebooks",
        "sse": "aws:kms",
        "kms_key_id": os.environ.get('KMS_SHARED'),
    },
}

def no_spaces(path):
    return ' ' not in path

c.HybridContentsManager.path_validators = {
}