      public BlobSendTerminalBuilder fire() {
        return new BlobSendTerminalBuilder() {
          Future<ByteBuffer> future = RpcHelper.EXECUTOR_SERVICE.submit(new Callable<ByteBuffer>() {
            final DbKeysBuilder dbKeysBuilder = (DbKeysBuilder) DbKeysBuilder.get();

            public ByteBuffer call() throws Exception {
              DbKeysBuilder.currentKeys.set(dbKeysBuilder);

              CouchMetaDriver.BlobSend.visit(dbKeysBuilder, BlobSendActionBuilder.this);
              return payload();
            }
          });

          public KouchTx tx() {
            KouchTx r = null;
            try {
              r =
                  CouchMetaDriver.gson().fromJson(UTF_8.decode(future.get()).toString(),
                      CouchTx.class);
            } catch (Exception e) {
              if (!RpcHelper.DEBUG_SENDJSON)
                return r;
              e.printStackTrace();
            }
            return r;
          }

          public Future<ByteBuffer> future() {
            return future;
          }

          @Deprecated
          public void oneWay() {
            final DbKeysBuilder dbKeysBuilder = DbKeysBuilder.get();

            RpcHelper.EXECUTOR_SERVICE.submit(new Runnable() {
              public void run() {
                try {
                  DbKeysBuilder.currentKeys.set(dbKeysBuilder);

                  future.get();
                } catch (Exception e) {
                  e.printStackTrace();
                }
              }
            });
          }
        };
      }
