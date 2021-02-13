import re
from urllib.request import urlopen

def get_regex(git_branch='master'):
    """
    Parameters
    ----------
    git_branch : :obj:`str`
        Branch or tag of the DCMLab/standards repo from which to retrieve regex.
    """
    url = f"https://raw.githubusercontent.com/DCMLab/standards/{git_branch}/harmony.py"
    glo, loc = {}, {}
    exec(urlopen(url).read(), glo, loc)
    return re.compile(loc['regex'], re.VERBOSE)

old_version = get_regex('v2.0.0')   # uses a version tag
pre_release = get_regex('develop')  # uses a branch name
