import requests
import json
import pandas as pd

'''
这段代码的功能是获取天勤量化的主连期货代码
'''

def QA_fetch_get_future_domain():
    """
    获取快期的主连代码

    return [list]
    """
    res =  pd.DataFrame(json.loads(requests.get("https://openmd.shinnytech.com/t/md/symbols/latest.json").text)).T
    return res.loc[res.ins_name.str.contains('主连')].underlying_symbol.apply(lambda x: x.split('.')[1]).tolist()


if __name__ == "__main__":
    print(QA_fetch_get_future_domain())
