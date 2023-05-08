from compas.plugins import plugin
import rhinoinside

from rhinoinside import Rhino

@plugin(category="install")

def installable_rhino_packages():
    return["ar_rhino"]