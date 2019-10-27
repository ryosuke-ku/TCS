          public CouchResultSet rows() {
            CouchResultSet r = null;
            try {
              r =
                  CouchMetaDriver.gson().fromJson(
                      UTF_8.decode(avoidStarvation(future.get())).toString(),
                      new ParameterizedType() {
                        public Type getRawType() {
                          return CouchResultSet.class;
                        }

                        public Type getOwnerType() {
                          return null;
                        }

                        public Type[] getActualTypeArguments() {
                          Type key = get(etype.keyType);
                          return new Type[] {
                              null == key ? Object.class : key, (Type) get(etype.type)};
                        }
                      });
            } catch (Exception e) {
              e.printStackTrace();
            }
            return r;
          }
