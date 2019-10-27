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
