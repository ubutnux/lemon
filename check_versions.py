#! /usr/bin/env python

def version_to_str(version):
    """ From (0, 2, 4) to '0.2.4' for example """
    return '.'.join(str(x) for x in version)

def str_to_version(version):
    """ From '0.2.4' to (0, 2, 4), for example """
    return tuple(int(x) for x in version.split('.'))

class RequireModuleVersionHook(object):

    def __init__(self, fullname, min_version, vfunc):
        """ Instantiation method for the RequireModuleVersionHook class.

        The 'fullname' parameter is the a fully qualified name of the module
        that we want to import, such as 'pyfits' or 'scipy'. 'min_version' is a
        tuple of integers specifying the minimum version of the module, such as
        (1, 2, 1). Finally, 'vfunc' is a hook function that will be passed the
        module object, after it is imported, and that must return its version
        as a tuple of integers.

        """

        self.fullname = fullname
        self.min_version = min_version
        self.vfunc = vfunc

    def find_module(self, fullname, path=None):
        """ The module finder.

        Receive the fully qualified name of the module to be imported, along
        with, optionally, the path where it is supposed to be found. Return
        None if the module cannot be found by this particular finder and self
        (since this class also implements the module loader) otherwise.

        """

        if fullname == self.fullname:
            self.path = path
            return self
        return None

