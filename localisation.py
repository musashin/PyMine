__author__ = 'Nicolas'

import locale
__frenchDialogs__ = {'worldFolderSelection': 'Choisis le dossier ou se trouvent tes mondes:'}
__englishDialogs__ = {'worldFolderSelection': 'Select the folder where your worlds are located:'}
__localisation__ = {'fr_CA': __frenchDialogs__, 'en': __englishDialogs__}

def get_dialog(key):
    lang, notUse = locale.getdefaultlocale()

    try:
        dialog = __localisation__[lang]
    except:
        dialog = __localisation__['en']

    try:
        string = dialog[key]
    except:
        string = 'None'

    return string