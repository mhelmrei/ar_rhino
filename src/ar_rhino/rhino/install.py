from compas.plugins import plugin


@plugin(category="install")

def installable_rhino_packages():
    return["ar_rhino"]