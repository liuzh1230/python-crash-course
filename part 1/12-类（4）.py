#python标准库

from collections import OrderedDict #导入Ordereddict类——有序字典

favourite_languages=OrderedDict()

favourite_languages['jen']='python'
favourite_languages['sarah']='c'
favourite_languages['edward']='ruby'

for name,language in favourite_languages.items():
    print(name.title()+"'s favourite language is "+
          language.title()+".")
