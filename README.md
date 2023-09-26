1. unittest 和 pytest 都是 python 的測試框架，unittest 需要定義模組和類別，pytest 只需要定義函數並 assert 其中的條件
2. pytest 的程式碼較簡單、緊湊、高效
3. 測試左移 : 產品一開始做軟體開發的時候，就要開始寫單元測試
4. no test cases, no quality!
5. 測試方法
   * 寫成測試自動化(best, 修改新版程式可以快速跑看有沒有 bugs)
   * reusable
   * 寫成一個 hackmd 文件，請一群人全部測一遍
   * 桌面錄音錄影
6. test cases 管理
   * redmine
   * gitlab
7. 如何做好的測試
   * 程式的每個地方都應該都跑過至少一個 test case
   * 多種 test case 的組合都應該被測試 as much as possible
   * show 你的 code 可以處理 bad input
8. 有時候測試沒過，不見得是你的程式出錯，是準備的正確答案出錯
9. statement coverage
    * testing 的最低標
10. 套件安裝
    * pip install pytest
    * python -m pip install pytest-cov
11. 測試語法
    * python -m pytest
    * python -m pytest --cov .
    * python -m pytest --cov-report html --cov .
    * python -m pytest --cov-branch --cov .
12. 產生的 htmlcov 資料夾裡面的 html file 可以看 coverage reports
    * missing 代表 statement 沒有測到
    * 需要改到 100%
13. coverage
    * branch : 每個分支(if、loop)在測試期間至少被執行一次
    * path : 所有可能性都參考(impossible)
    * 困難度 : path > branch > statement
15. branch coverage 已經是金管會證交系統驗收標準
16. boundary testing 邊界測試
17. negative testing 無效輸入、錯誤處理
