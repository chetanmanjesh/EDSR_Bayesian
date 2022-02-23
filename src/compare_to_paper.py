import os
for sc in [4]:
    print(sc)
    os.system("python main.py --data_test Demo --scale "+str(sc)+" --pre_train download --test_only --save_results")
