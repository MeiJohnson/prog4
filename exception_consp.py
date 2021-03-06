# BaseException — базовый класс для встроенных исключений в Python. 
# Находится на самом верху иерархии исключений. Не стоит его отлавливать, так как 
# в нем находятся и полезные исключения 
# (например, останов программы для ввода данных с клавиатуры).

# ! Чем конкретнеее исключение мы отлавливаем, тем лучше.
# ! Необходимо стараться минимизировать блок кода try.
# ! используйте встроенные в Python типы исключений для работы с ошибками;
# ! при написании бизнес-логики (?) создавайте собственные классы для 
# исключений, наследуя базовый класс Exception;


# Исключения, связанные с подключением модулей:
# 1-ый вид связан именно с модулями

import foo
"""
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-1-34d390fb3acc> in <module>()
----> 1 import foo

ModuleNotFoundError: No module named 'foo'

"""

# 2-ой вид относится к ошибке импорта конкретного элемента
# из данного модуля


from math import xyz

"""
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-2-0f297399a0bd> in <module>()
----> 1 from math import xyz

ImportError: cannot import name 'xyz'

"""

# Исключение относящееся к ошибке типов

"""

    [1, 100, 10] + 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-e35bb6f24bb1> in <module>()
----> 1 [1, 100, 10] + 2

TypeError: can only concatenate list (not "int") to list

"""



try:
    pass
    # 1 open file 
    # 2 read from f
    # 3 close file 
except (ValueError, SomeError """Выражение, возвращающее тип или кортеж типов. """):
    pass

except (TypeError) as e """Опциональное имя для перехваченного исключения (as e:) """:
    print(e)
    
# Все остальные встроенные исключения, а также исключения, объявленные
#  пользователем, должны наследоваться от класса Exception.    
    