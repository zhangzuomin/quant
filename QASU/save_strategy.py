from QUANTAXIS.QAUtil import DATABASE
from QUANTAXIS.QASetting.QALocalize import strategy_path
import datetime
import os
import sys
import requests


"""
对于策略的存储
"""

'''
QA_SU_save_strategy` 函数的主要作用是保存策略。函数接收七个参数：
- `name`：策略的名称。
- `portfolio_cookie`：投资组合的标识，默认为 'default'。
- `account_cookie`：账户的标识，默认为 'default'。
- `version`：策略的版本，默认为 1。
- `if_save`：是否保存策略到本地文件，默认为 False。
- `if_web_request`：是否通过网络请求保存策略，默认为 False。
- `webreuquestsurl`：网络请求的 URL，默认为 'http://localhost:8010/backtest/write'。
'''


def QA_SU_save_strategy(name, portfolio_cookie='default', account_cookie='default', version=1, if_save=False, if_web_request=False, webreuquestsurl='http://localhost:8010/backtest/write'): 

    """ 
  Save a strategy to the database and optionally to a file. 
  Args: 
      name (str): The name of the strategy. 
      portfolio_cookie (str, optional): The portfolio cookie. Defaults to 'default'.
      account_cookie (str, optional): The account cookie. Defaults to 'default'.
      version (int, optional): The version of the strategy. Defaults to 1.
      if_save (bool, optional): Whether to save the strategy to a file. Defaults to False.
      if_web_request (bool, optional): Whether to make a web request. Defaults to False.
      webreuquestsurl (str, optional): The URL for the web request. Defaults to 'http://localhost:8010/backtest/write'. 
  Returns: 
      None 
  Raises: 
      None
  
  Examples:
      # Save a strategy to the database and file
      QA_SU_save_strategy('my_strategy', if_save=True)
  
      # Save a strategy to the database without saving to a file
      QA_SU_save_strategy('my_strategy', if_save=False) 
"""

  
    absoult_path = '{}{}strategy_{}.py'.format(strategy_path, os.sep, name)
    with open(sys.argv[0], 'rb') as p:
        data = p.read() 
        if if_web_request:
            try:
                requests.get(webreuquestsurl, {'strategy_content': data})
            except:
                pass

        collection = DATABASE.strategy
        collection.insert({'name': name, 'account_cookie': account_cookie,
                           'portfolio_cookie': portfolio_cookie, 'version': version,
                           'last_modify_time': str(datetime.datetime.now()),
                           'content': data.decode('utf-8'),
                           'absoultpath': absoult_path})
        if if_save:
            with open(absoult_path, 'wb') as f:
                f.write(data)


# print(os.path.basename(sys.argv[0]))
if __name__ == '__main__':
    QA_SU_save_strategy('test', if_save=True, if_web_request=True)
