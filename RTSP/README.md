# RTSP

# 1. クライアント環境構築
## 1.1. RTSPサーバ構築
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
> [!NOTE]
> 以下のコマンドを実行することで、RTSPサーバを起動することができる  
> オプション指定がない場合、**rtps://<URL・IPアドレス>:8554/unicast**でアクセスできる
> ``` bash
> > sudo systemctl start v4l2rtspserver
> ```
> or
> ``` bash
> > sudo v4l2rtspserver
> ```
> また、下記のコマンドにより、自動起動が可能となる
> ```bash
> > sudo systemctl enable v4l2rtspserver.service
> ```

# 2. サーバ環境構築
## 2.1. ffmpeg
* ffmpegインストール
     ``` bash
     > sudo apt -y install ffmpeg
     ```
## 2.2. nginx
* nginxインストール
     ``` bash
     > sudo apt -y install nginx
     ```
