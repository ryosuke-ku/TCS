        public void close() throws IOException {
          JsonSendActionBuilder actionBuilder =
              new JsonSend().opaque(db + "/" + id + "/" + fileName + "?rev=" + rev).validjson(
                  getBuffer().toString()).to();
          actionBuilder.hdr().headerString(HttpHeaders.Content$2dType, contentType);
          CouchTx tx = actionBuilder.fire().tx();
          if (!tx.ok()) {
            throw new IOException(tx.error());
          }
          rev = tx.rev();
        }
