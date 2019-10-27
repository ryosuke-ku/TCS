          public String json() {
            String r = null;
            try {
              ByteBuffer visit = future.get();
              r = null == visit ? null : UTF_8.decode(avoidStarvation(visit)).toString();
            } catch (Exception e) {
              e.printStackTrace();
            }
            return r;
          }
