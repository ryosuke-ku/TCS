	public RecordFactory getRecordFactory() {
		if (recordFactory == null) {
			return recordFactory = InjectorSingleton.get().getInstance(RecordFactory.class);
		} else {
			return recordFactory;
		}
	}
