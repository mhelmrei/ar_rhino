from compas.plugins import plugin

import os
from compas.plugins import plugin
from compas_ghpython.components import install_userobjects


@plugin(category="install")

def installable_rhino_packages():
    return["ar_rhino"]

@plugin(category="install")
def after_rhino_install(installed_packages):
    import ar_rhino

    install_folder = os.path.dirname(ar_rhino.__file__)
    userobjects = os.path.join(install_folder, "ghpython", "components", "ghuser")

    installed_objects = install_userobjects(userobjects)

    return [
        (
            "ar_rhino",
            "Installed {} GH User Objects".format(len(installed_objects)),
            True,
        )
    ]