# Websocketサーバ環境構築

* pipインストール  

    ``` bash
    > sudo apt -y install python3-pip
    ```  

* pip設定(PEP 686対策)  

    ``` bash
    > mkdir ~/.pip  
    > vi ~/.pip/pip.conf
    ```

    * 設定内容（pip.conf）  
  
          > [global]  
          > break-system-packages = true

* openCVインストール  

    ``` pip
    > pip install opencv-python
    ```

* Websocket Serverインストール  

    ``` pip
    > pip install websocket-server
    ```

    * 実行するとエラーが発生するので、該当箇所を以下の通りに変更

        lib/python3.12/site-packages/websocket_server/websocket_server.py: 341行目

        ``` python
        opcode_handler(self, message_bytes.decode('utf8'))
        ```
        ↓
        ``` python
        try:
            opcode_handler(self, message_bytes.decode('utf8'))
        except:
            pass
        ```

* pymongoインストール  

    ``` pip
    > pip install pymongo
    ```

* pytorchインストール  
    * CPU  
        
        ``` pip  
        > pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu  
        ```

     * GPU  

        ``` pip  
        > pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
        ```

* YOLOインストール  

    ``` pip
    > pip install ultralytics
    ```

* ImportError: libGL.so.1: cannot open shared object file の対策

    ``` bash
    > apt -y install libopencv-dev
    ```
