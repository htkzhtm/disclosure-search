# Summary of this repo
Search the lastest timely disclosure of particular listed company, using by EDINET API.

This source works by specifying the stock code.

For now, it covers quarterly reports and securities reports.

This content is mainly for **investors who can programming to some extent**.

And, **This application is for me. So, There are some restrictions for running**.

# EDINET API Specification
https://disclosure.edinet-fsa.go.jp/EKW0EZ0015.html

and rule
https://disclosure.edinet-fsa.go.jp/download/ESE140191.pdf

# Requires
- Python3
 ```
 $ brew install python3
 ```
- Macintosh
  - There are strong restrictions due to file operations. It will be compatible with Windows, Linux in the future.
- poetry
  - This repo also runs on a it. If you have a particular package, You can execute directly.

```
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

# How to use
As mentioned above, there are strong restrictions due to file operations.

So, you have to clone this repo to your home directory.

This specification going to be modified.

```
$ cd ~
$ git clone git@github.com:htkzhtm/disclosure-search.git
$ cd disclosure-search
$ poetry install
$ poetry run python main.py StockCode(4 digits number)
```

For example.
```
$ poetry run python main.py 7974
```

PDF, Zip, and Unzip files are generated at the following path.
```
~/disclosure-search/disclosureFiles
```

# What is a securities(stock?) code?
A stock code is the identification number of a listed company in Japan.

In USA, calls this, "Ticker Symbol" (e.g. $APPL, $AMZN).

In Japan, uses 4 digits number. The representative companies are as following.


| Stock Code | Company Name | Company Name(in English) |
| ------------- | ------------- | ------------- |
| 4063  | 信越化学工業株式会社  | Shin-Etsu Chemical Co., Ltd.  |
| 4519  | 中外製薬株式会社  | Chugai Pharmaceutical Co., Ltd.  |
| 4661  | 株式会社オリエンタルランド  | Oriental Land Co., Ltd.  |
| 6098  | 株式会社リクルートホールディングス  | Recruit Holdings Co.,Ltd  |
| 6367  | ダイキン工業株式会社  | Daikin Industries, Ltd.  |
| 6501  | 株式会社日立製作所  | Hitachi, Ltd.  |
| 6594  | 日本電産株式会社  | Nidec Corporation  |
| 6758  | ソニーグループ株式会社  | Sony Group Corporation  |
| 6861  | 株式会社キーエンス  | KEYENCE CORPORATION  |
| 6902  | 株式会社デンソー  | DENSO Corporation  |
| 7203  | トヨタ自動車株式会社  | Toyota Motor Corporation  |
| 7741  | HOYA株式会社  | HOYA Corporation  |
| 7974  | 任天堂株式会社  | Nintendo Co., Ltd  |
| 8035  | 東京エレクトロン株式会社  | Tokyo Electron Limited  |
| 8306  | 株式会社三菱UFJフィナンシャル・グループ  | Mitsubishi UFJ Financial Group, Inc.  |
| 9432  | 日本電信電話株式会社  | Nippon Telegraph and Telephone Corporation  |
| 9433  | KDDI株式会社  | KDDI CORPORATION  |
| 9434  | ソフトバンク株式会社  | SoftBank Corp.  |
| 9983  | ソフトバンクグループ株式会社  | SoftBank Group Corp.  |
| 9984  | 株式会社ファーストリテイリング  | FAST RETAILING CO., LTD.  |



