# Online Judge

## 環境

- Rubyのバージョン管理：`rbenv`
- Pythonパッケージ：`.venv`に`online-judge-tools`をインストール
- Python自体のバージョン管理：`pyenv`
- 自動テスト：vccodeの`tasks.json`でRUNする

### `cpsub`

提出用のシェルスクリプト。拡張子に応じて言語を判別し提出する。
`_no-open`は提出後のブラウザオープンをさせない（虚無埋めに使っていた）。

### `cptest`

拡張子で言語を判別しテストを実行。
`_eps`は小数誤差あり問題用。

