# Websocketクライアント環境構築
Clientフォルダ内のファイルおよびフォルダを一つ上の階層に移動する  

WebSocketクライアントで使用するパッケージは、一括でインストールを行うファイルがあるので、以下のコマンドを実行すること
なお、個々でインストールが行えるようにインストールコマンドについても記載を行う
> [!CAUTION]
> プログラム実行時、openCV関連ライブラリに関するエラーが発生が発生した場合、以下のライブラリをインストール
> ``` bash
> > sudo apt -y install libopencv-dev
> ```

* openCVインストール  
    ``` pip
    > pip install opencv-python
    ```
* Websocketインストール  
    ``` pip
    > pip install websockets
    ```
