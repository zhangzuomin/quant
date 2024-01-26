from configparser import ConfigParser


# QACfg.py 模块的主要功能是处理配置文件。
# QA_util_cfg_initial函数的目的是初始化配置文件，但是函数体为空，所以实际上并没有实现任何功能


def QA_util_cfg_initial(CONFIG_FILE): 
    """[summary]

    Arguments:
        CONFIG_FILE {[type]} -- [description]
    """

    pass



# QA_util_get_cfg函数用于获取配置信息
def QA_util_get_cfg(__file_path, __file_name):
    """
    explanation:
        获取配置信息

    params:
        * __file_path ->
            含义: 配置文件地址
            类型: str
            参数支持: []
        * __file_name ->
            含义: 文件名
            类型: str
            参数支持: []

    """
    __setting_file = ConfigParser()
    try:
        return __setting_file.read(__file_path + __file_name)
    except:
        return 'wrong'
