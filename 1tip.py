# import os
# import time
# import multiprocessing
#
# # print(os.getcwd())
# # print(os.listdir(os.getcwd()))
# # print(os.path.isabs('D:\Python_project'))
# # print(os.name)
# # i=open('url.txt','a+')
# # print(type(i))
# # # print(i.readline())
# # print('-------------')
# # # print(i.read())
# # i.write('mamule2')
# # i.flush()
# # i.close()
# # # print(type(i))
# # # try :
# # #     i = open('url23.txt', 'r')
# # #     print(i.read())
# # # finally:
# # #     if i:
# # #         i.close()
# # # with open('')
# # def main():
# #     return
# # 多线程模拟
#
#
#     # 定义两个间隔0.5s执行3次的函数
# def fun_a():
#         for i in range(3):
#              print("f_a()")
#              time.sleep(0.5)
#
#
# def fun_b():
#         for i in range(3):
#             print("f_b()")
#             time.sleep(0.5)
#
# def run_proc(name):
#     print(name,os.getppid())
#
#
#
# if __name__ == "__main__":
#     # 使用进程类创建进程对象
#     fun_a_process = multiprocessing.Process(target=fun_a)
#     fun_b_process = multiprocessing.Process(target=fun_b)
#
#
#
#
#     # 启动多进程执行任务
#     fun_a_process.start()
#     fun_b_process.start()
#
#     # # print(os.getpid())
#     # p=Process(target=run_proc,args=(str(1)))
#     # p2=Process(target=run_proc,args=(str(2)))
#     #
#     # print('start')
#     # p.start()
#     # p2.start()
#     # print('end')
#
#
#
#
#
