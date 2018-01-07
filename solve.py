# -*- coding: utf-8 -*- 
import angr

p = angr.Project('./test', load_options={'auto_load_libs': False})

addr_main = p.loader.main_object.get_symbol('main').rebased_addr
base = addr_main - 0x876
succeed = base + 0x91a
failed = base + 0x926

print("base = 0x%x" % base)
print("succeed = 0x%x" % succeed)
print("failed = 0x%x" % failed)

initial_state = p.factory.blank_state(addr=addr_main) #開始アドレス
pg = p.factory.simgr(initial_state) #パス分析クラスのインスタンス作成
e = pg.explore(find=(succeed,), avoid=(failed,)) # 走査

if len(e.found) > 0:
    print('Dump stdin at succeeded():')
    for x in e.found:
        s = x.state
        print("stdout: " + repr(s.posix.dumps(1)))
        print("stdin: " + repr(s.posix.dumps(0)))
