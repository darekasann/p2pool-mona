# 自分用ノードの立てかた

とりあえず、 README.mdを参考になんとかビルド、インストールしてください。

monacoin-qtかmonacoindを起動させておいてくだだい。

monacoin.confの位置が標準通りなら、だいたい

    run_p2pool.py --net monacion
    
だけで起動できます。

## マイニング

stratum+tcp://localhost:9456
user: コイン受け取りアドレス
pass: 何でも

で掘れます

## webインターフェイス

http://localhost:9456/ からノードやネットワークの状態が見られます。

代替webインターフェイス

