# 開発環境構築
   ここでの開発環境については、UbuntuおよびRaspberry Pi OSのLinux環境をベースに記載する



## 1. Python
### 1.1. Pythonのバージョン指定

* 必要なプログラムをインストール
   ``` bash
   > sudo apt update
   > sudo apt install software-properties-common
   ```
* Repositoryを登録
   ``` bash
   > sudo add-apt-repository ppa:deadsnakes/ppa
   ```
* 指定バージョンをインストール（20250128現在の最新は、3.13）
   ``` bash
   > sudo apt install python3.xx
   ```
* 指定バージョンを使用する
   ``` bash
   > python3.xx --version
   ```    
> [!NOTE]
> 以下の通りにコマンド実行を行うと、デフォルトバージョンのPythonで実行される
> ``` bash
> > python3 --version
> ```

### 1.2. 仮想環境構築
Pythonは、仮想環境を使用することを推奨している  
ここでは、venvという仮想環境を使用する  
なお、ここでのPythonのバージョンは3.5以降のものとする
* 仮想環境の作成
   ``` bash
   > mkdir 仮想環境構築ディレクトリ
   > cd 仮想環境構築ディレクトリ
   > python3 -m venv 仮想環境名
   ```
* 仮想環境の有効化
   ``` bash
   > cd 仮想環境構築ディレクトリ
   > source 仮想環境名/bin/activate
   ```
* 仮想環境の無効化
   ``` bash
   > deactive
   ```
> [!NOTE]
> 仮想環境の作成コマンドを実行した際、エラーが発生した場合は以下のライブラリをインストール
> ``` bash
> > sudo apt install python3-venv
> ```

### 1.3. pip関係
pipは、Pythonのパッケージ管理システムである  
下記の内容については、必要に応じて実行すること

* pipインストール  
    ``` bash
    > sudo apt -y install python3-pip
    ```
* pip設定(PEP 686対策)  
    ``` bash
    > mkdir ~/.pip  
    > vi ~/.pip/pip.conf
    ```
    * pip.conf  
        > [global]
        > break-system-packages = true
* パッケージ一括インストール
パッケージを一括でインストールを行うファイル(ex. requirements.txt )が用意されている場合は、以下のコマンドを実行するとまとめてパッケージインストールできる
    ``` bash
    > pip install -r requirements.txt
    ```


## 2. node.js
### 2.1. node.jsのインストール
Ubuntuのパッケージソフトのnode.JSおよびnode.jsのパッケージ管理システムのnpmのバージョンが最新ではないため、以下のコマンドでインストールを行う
* 現行バージョンをインストール
    ``` bash
    > sudo apt install -y nodejs npm
    ```
* nをインストール（バージョン管理）
    ``` bash
    > sudo npm install n -g
    ```
* 最新のnode.jsとnpmをインストール
    ``` bash
    > sudo n stable
    ```
* 最初にインストールしたものをアンインストール
    ``` bash
    > sudo apt purge -y nodejs npm
    > sudo apt autoremove -y
    ```
