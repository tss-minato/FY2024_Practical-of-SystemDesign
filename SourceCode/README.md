# 開発環境構築
   ここでの開発環境については、UbuntuおよびRaspberry Pi OSのLinux環境をベースに記載する
## Python
* Pythonのバージョン指定
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
        
        > [!CAUTION]
        > aaa

* 仮想環境構築
  

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


## Angulr
