	public Long move(final byte[] key, final int dbIndex) {
		return pipeline.move(key, dbIndex).get();
	}
