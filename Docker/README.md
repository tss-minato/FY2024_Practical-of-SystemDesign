# Docker環境構築

* インストール

    ``` bash
    > curl -fsSL https://get.docker.com -o get-docker.sh
    > sudo sh get-docker.sh
    ```

* ユーザ権限で実行できるように設定

    ``` bash
    > sudo gpasswd -a $USER docker
    > newgrp docker
    ```

上記実行後、再起動を行う
