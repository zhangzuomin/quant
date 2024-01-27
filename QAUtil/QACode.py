# 该模块的主要功能是处理股票代码

# QA_util_code_tostr函数用于将股票代码转换成标准的6位格式
def QA_util_code_tostr(code):
    """
    explanation:
        将所有沪深股票从数字转化到6位的代码,因为有时候在csv等转换的时候,诸如 000001的股票会变成office强制转化成数字1,
        同时支持聚宽股票格式,掘金股票代码格式,Wind股票代码格式,天软股票代码格式

    params:
        * code ->
            含义: 代码
            类型: str
            参数支持: []
    """
    if isinstance(code, int):
        return "{:>06d}".format(code)
    if isinstance(code, str):
        # 聚宽股票代码格式 '600000.XSHG'
        # 掘金股票代码格式 'SHSE.600000'
        # Wind股票代码格式 '600000.SH'
        # 天软股票代码格式 'SH600000'
        if len(code) == 6:
            return code
        if len(code) == 8:
            # 天软数据
            return code[-6:]
        if len(code) == 9:
            return code[:6]
        if len(code) == 11:
            if code[0] in ["S"]: 
                return code.split(".")[1]
            return code.split(".")[0]
        raise ValueError("错误的股票代码格式")
    if isinstance(code, list):
        return QA_util_code_to_str(code[0])



# QA_util_code_tolist函数用于将股票代码转换成列表
def QA_util_code_tolist(code, auto_fill=True):
    """
    explanation:
        将转换code==> list

    params:
        * code ->
            含义: 代码
            类型: str
            参数支持: []
        * auto_fill->
            含义: 是否自动补全(一般是用于股票/指数/etf等6位数,期货不适用) (default: {True})
            类型: bool
            参数支持: [True]
    """

    if isinstance(code, str):
        if auto_fill:
            return [QA_util_code_tostr(code)]
        else:
            return [code]

    elif isinstance(code, list):
        if auto_fill:
            return [QA_util_code_tostr(item) for item in code]
        else:
            return [item for item in code]



# QA_util_code_adjust_ctp函数用于在ctp和通达信之间来回转换股票代码
def QA_util_code_adjust_ctp(code, source):
    """
    explanation:
        此函数用于在ctp和通达信之间来回转换

    params:
        * code ->
            含义: 代码
            类型: str
            参数支持: []
        * source->
            含义: 转换至目的源
            类型: str
            参数支持: ["pytdx", "ctp"]

    demonstrate:
        a = QA_util_code_adjust_ctp('AP001', source='ctp')
        b = QA_util_code_adjust_ctp('AP2001', source = 'tdx')
        c = QA_util_code_adjust_ctp('RB2001', source = 'tdx')
        d =  QA_util_code_adjust_ctp('rb2001', source = 'ctp')
        print(a+"\n"+b+"\n"+c+"\n"+d)

    output:    
        >>AP2001
        >>AP001
        >>rb2001
        >>RB2001
    """
    if source == 'ctp':
        if len(re.search(r'[0-9]+', code)[0]) <4:
            return re.search(r'[a-zA-z]+', code)[0] + '2' + re.search(r'[0-9]+', code)[0]
        else:
            return code.upper()
    else:
        if re.search(r'[a-zA-z]+', code)[0].upper() in ['RM', 'CJ', 'OI', 'CY', 'AP', 'SF', 'SA', 'UR', 'FG', 'LR', 'CF', 'WH', 'IPS', 'ZC', 'SPD', 'MA', 'TA', 'JR', 'SM', 'PM', 'RS', 'SR', 'RI']:
            return re.search(r'[a-zA-z]+', code)[0] + re.search(r'[0-9]+', code)[0][1:]
        else:
            return re.search(r'[a-zA-z]+', code)[0].lower() + re.search(r'[0-9]+', code)[0]
