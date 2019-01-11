# A simple Python3 script all user added modules available in the system
try:
    from pip._internal.utils.misc import get_installed_distributions
except ImportError:  # pip<10
    from pip import get_installed_distributions

installed_packages = get_installed_distributions()
installed_packages_list = sorted(["%s == %s" % (i.key, i.version)
    for i in installed_packages])
print(*installed_packages_list, sep='\n')
