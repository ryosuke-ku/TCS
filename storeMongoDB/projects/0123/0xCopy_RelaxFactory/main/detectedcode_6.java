    public String getAttachment(String fileName) {
      return new DocFetch().db(db).docId(id + "/" + fileName).to().fire().json();
    }
