# RTSPサーバ構築

* 設定関連
    **/etc/modules** に以下の内容を追記し、再起動を行う
    ```
    bcm2835-v4l2
    ```

* 必要モジュールのインストール

    ``` bash
    > sudo apt -y install git
    > sudo apt -y install cmake
    > sudo apt -y install liblivemedia-dev 
    ```

* コンパイル及びインストール

    ``` bash
    > git clone https://github.com/mpromonet/h264_v4l2_rtspserver.git
    > cd h264_v4l2_rtspserver
    > sudo cmake .
    > sudo make install
    ```

    インストール後、再起動を行う

* 実行

    ``` bash
    sudo v4l2rtspserver
    ```

    デフォルトの場合、**rtps://<IPアドレス>:8554/unicast**でアクセスできる
