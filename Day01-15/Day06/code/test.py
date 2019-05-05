from module1 import foo
foo()

from module2 import foo  # later will override earlier
foo()

import module3  # 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__

from toy import toyFoo
toyFoo()

from toyB import BB
BB()
