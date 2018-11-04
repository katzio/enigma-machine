import cProfile

def performance_test():
    return True

cProfile.run(statement='performance_test()', sort=1) # 1 = time