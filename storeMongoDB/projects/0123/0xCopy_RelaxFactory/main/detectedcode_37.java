    public BlobSendActionBuilder to() {
      assert 5 <= parms.size() : "required parameters are: [blob, db, docId, rev, attachname]";
      return new BlobSendActionBuilder();
    }
